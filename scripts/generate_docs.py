#!/usr/bin/env python3
"""
Documentation generator for Python modules in the project.

Scans the /workspace/code directory for public APIs (modules, classes, functions)
and produces Markdown documentation under /workspace/docs.

This script uses the Python AST to avoid importing project modules or third-party
dependencies. It infers public symbols by the following rules:
 - If a module defines __all__, only those names are considered public
 - Otherwise, any name not starting with an underscore is considered public

Run:
  python3 /workspace/scripts/generate_docs.py

Outputs:
  - /workspace/docs/README.md (index and usage)
  - /workspace/docs/<module_name>.md for each module in /workspace/code
"""

from __future__ import annotations

import ast
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Sequence, Tuple


WORKSPACE_ROOT = Path("/workspace")
CODE_DIR = WORKSPACE_ROOT / "code"
DOCS_DIR = WORKSPACE_ROOT / "docs"


EXCLUDE_FILES = {
    # Common non-library files to skip
    "setup.py",
    "Makefile",
}

EXCLUDE_SUFFIXES = (
    "_test.py",
    "-test.py",
    "test_.py",
)

EXCLUDE_DIRS = {
    ".ipynb_checkpoints",
}


def read_text(path: Path) -> str:
    with path.open("r", encoding="utf-8") as f:
        return f.read()


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def is_public_name(name: str) -> bool:
    return not name.startswith("_")


def safe_ast_parse(source: str, filename: str) -> Optional[ast.AST]:
    try:
        return ast.parse(source, filename=filename)
    except SyntaxError:
        return None


def get_module_public_exports(module: ast.Module) -> Optional[Sequence[str]]:
    for node in module.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    if isinstance(node.value, (ast.List, ast.Tuple)):
                        values: List[str] = []
                        for elt in node.value.elts:
                            if isinstance(elt, ast.Str):  # py<3.8
                                values.append(elt.s)
                            elif isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                                values.append(elt.value)
                        return values
    return None


@dataclass
class FunctionDoc:
    name: str
    signature: str
    docstring: Optional[str]


@dataclass
class ClassDoc:
    name: str
    docstring: Optional[str]
    methods: List[FunctionDoc]


@dataclass
class ModuleDoc:
    name: str
    rel_import: str
    docstring: Optional[str]
    functions: List[FunctionDoc]
    classes: List[ClassDoc]


def format_arg(arg: ast.arg) -> str:
    if getattr(arg, "annotation", None) is not None:
        return f"{arg.arg}: ..."
    return arg.arg


def format_args(args: ast.arguments) -> str:
    parts: List[str] = []

    def defaults_for(positional: Sequence[ast.arg], defaults: Sequence[ast.expr]) -> List[Optional[str]]:
        # Align defaults to the right per Python call semantics
        padding = [None] * (len(positional) - len(defaults))
        merged = padding + list(defaults)
        out: List[Optional[str]] = []
        for d in merged:
            if d is None:
                out.append(None)
            else:
                out.append("...")
        return out

    pos_only = getattr(args, "posonlyargs", []) or []
    pos_or_kw = args.args or []
    all_pos = list(pos_only) + list(pos_or_kw)
    all_pos_defaults = defaults_for(all_pos, args.defaults or [])

    for a, default in zip(all_pos, all_pos_defaults):
        if default is None:
            parts.append(format_arg(a))
        else:
            parts.append(f"{format_arg(a)}=...")

    if args.vararg is not None:
        parts.append(f"*{args.vararg.arg}")

    # Keyword-only
    if args.kwonlyargs:
        if args.vararg is None:
            parts.append("*")
        for a, d in zip(args.kwonlyargs, args.kw_defaults or [None] * len(args.kwonlyargs)):
            if d is None:
                parts.append(format_arg(a))
            else:
                parts.append(f"{format_arg(a)}=...")

    if args.kwarg is not None:
        parts.append(f"**{args.kwarg.arg}")

    return ", ".join(parts)


def build_function_signature(func: ast.AST, name: str) -> str:
    if isinstance(func, (ast.FunctionDef, ast.AsyncFunctionDef)):
        args_s = format_args(func.args)
        return f"{name}({args_s})"
    return f"{name}(...)"


def extract_module_doc(module_name: str, file_path: Path) -> Optional[ModuleDoc]:
    source = read_text(file_path)
    tree = safe_ast_parse(source, filename=str(file_path))
    if tree is None:
        return None

    module_docstring = ast.get_docstring(tree)
    explicit_public = get_module_public_exports(tree)

    public_functions: List[FunctionDoc] = []
    public_classes: List[ClassDoc] = []

    def is_public(symbol_name: str) -> bool:
        if explicit_public is not None:
            return symbol_name in explicit_public
        return is_public_name(symbol_name)

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and is_public(node.name):
            public_functions.append(
                FunctionDoc(
                    name=node.name,
                    signature=build_function_signature(node, node.name),
                    docstring=ast.get_docstring(node),
                )
            )
        elif isinstance(node, ast.ClassDef) and is_public(node.name):
            methods: List[FunctionDoc] = []
            for sub in node.body:
                if isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)) and is_public(sub.name):
                    methods.append(
                        FunctionDoc(
                            name=sub.name,
                            signature=build_function_signature(sub, f"{node.name}.{sub.name}"),
                            docstring=ast.get_docstring(sub),
                        )
                    )
            public_classes.append(
                ClassDoc(
                    name=node.name,
                    docstring=ast.get_docstring(node),
                    methods=methods,
                )
            )

    rel_import = f"code.{module_name}"
    return ModuleDoc(
        name=module_name,
        rel_import=rel_import,
        docstring=module_docstring,
        functions=sorted(public_functions, key=lambda f: f.name.lower()),
        classes=sorted(public_classes, key=lambda c: c.name.lower()),
    )


def list_python_modules(code_dir: Path) -> List[Path]:
    results: List[Path] = []
    for entry in sorted(code_dir.iterdir()):
        if entry.is_dir():
            if entry.name in EXCLUDE_DIRS:
                continue
            # Not recursing into subdirectories for simplicity; the project appears flat
            continue
        if entry.suffix != ".py":
            continue
        if entry.name in EXCLUDE_FILES:
            continue
        if entry.name.endswith(EXCLUDE_SUFFIXES):
            continue
        results.append(entry)
    return results


def markdown_escape(text: str) -> str:
    if text is None:
        return ""
    # Escape backticks so inline code markers in docstrings don't break formatting
    return text.replace("`", "\\`")


def render_module_markdown(doc: ModuleDoc) -> str:
    lines: List[str] = []
    lines.append(f"## Module `{doc.rel_import}`")
    lines.append("")
    if doc.docstring:
        lines.append(markdown_escape(doc.docstring))
        lines.append("")
    lines.append("### Import")
    lines.append("")
    lines.append("```python")
    lines.append(f"from {doc.rel_import} import *  # or import specific names")
    lines.append("```")
    lines.append("")

    if doc.functions:
        lines.append("### Functions")
        lines.append("")
        for f in doc.functions:
            lines.append(f"- `{f.signature}`")
            if f.docstring:
                lines.append("")
                lines.append(markdown_escape(f.docstring))
                lines.append("")
            lines.append("```python")
            lines.append(f"from {doc.rel_import} import {f.name}")
            lines.append(f"# Example usage:")
            lines.append(f"result = {f.name}(...)  # fill in arguments")
            lines.append("```")
            lines.append("")

    if doc.classes:
        lines.append("### Classes")
        lines.append("")
        for c in doc.classes:
            lines.append(f"- `{c.name}`")
            if c.docstring:
                lines.append("")
                lines.append(markdown_escape(c.docstring))
                lines.append("")
            lines.append("```python")
            lines.append(f"from {doc.rel_import} import {c.name}")
            lines.append(f"obj = {c.name}(...)  # construct with appropriate arguments")
            lines.append("```")
            lines.append("")
            if c.methods:
                lines.append("Methods:")
                lines.append("")
                for m in c.methods:
                    lines.append(f"  - `{m.signature}`")
                    if m.docstring:
                        lines.append("")
                        lines.append(markdown_escape(m.docstring))
                        lines.append("")
                    lines.append("```python")
                    lines.append(f"# obj is an instance of {c.name}")
                    lines.append(f"obj.{m.name}(...)  # fill in arguments")
                    lines.append("```")
                    lines.append("")

    return "\n".join(lines).strip() + "\n"


def render_index_markdown(module_docs: List[ModuleDoc]) -> str:
    lines: List[str] = []
    lines.append("# Project Documentation")
    lines.append("")
    lines.append("This documentation is auto-generated from the public symbols in `code/`.")
    lines.append("")
    lines.append("## How to Regenerate")
    lines.append("")
    lines.append("```bash")
    lines.append("python3 /workspace/scripts/generate_docs.py")
    lines.append("```")
    lines.append("")
    lines.append("## Modules")
    lines.append("")
    for doc in module_docs:
        lines.append(f"- [{doc.rel_import}](./{doc.name}.md)")
    lines.append("")
    return "\n".join(lines).strip() + "\n"


def main(argv: Sequence[str]) -> int:
    if not CODE_DIR.exists():
        print(f"Code directory not found: {CODE_DIR}", file=sys.stderr)
        return 1

    ensure_dir(DOCS_DIR)

    module_paths = list_python_modules(CODE_DIR)
    module_docs: List[ModuleDoc] = []
    for path in module_paths:
        module_name = path.stem
        doc = extract_module_doc(module_name, path)
        if doc is None:
            continue
        module_docs.append(doc)

    module_docs.sort(key=lambda d: d.rel_import.lower())

    # Write per-module docs
    for doc in module_docs:
        out_path = DOCS_DIR / f"{doc.name}.md"
        out_path.write_text(render_module_markdown(doc), encoding="utf-8")

    # Write index
    (DOCS_DIR / "README.md").write_text(render_index_markdown(module_docs), encoding="utf-8")

    print(f"Wrote documentation for {len(module_docs)} modules to {DOCS_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

