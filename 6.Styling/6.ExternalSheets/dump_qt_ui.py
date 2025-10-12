# dump_qt_ui.py
# Generates QSS skeleton only for widgets that have objectName.
# Usage:
#   from dump_qt_ui import generate_qss_skeleton
#   generate_qss_skeleton(app, out_path="qss_skeleton.qss")
#
# Requires PySide6 (or PyQt6 with small adaptions). Run in the same process as QApplication.

from __future__ import annotations

import sys

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QApplication, QWidget

_SKIP_CLASS_NAMES = {
    "QLayout",
    "QSpacerItem",
    "QAction",
    "QMenu",
    "QMenuBar",
    "QStatusBar",
    "QWidgetItem",
}


def _safe_object_name(obj: QObject) -> str:
    try:
        return obj.objectName() or ""
    except Exception:
        return ""


def dump_tree(
    root: QObject,
    indent: int = 0,
    out_lines: list[str] | None = None,
    selectors: set[str] | None = None,
    parent_name_selector: str | None = None,
) -> tuple[list[str], set[str]]:
    """
    Traverse widget tree from root.
    - Only generate selectors for widgets that have an objectName.
    - parent_name_selector: the parent's '#name' selector (or None). Only used if parent has objectName.
    """
    if out_lines is None:
        out_lines = []
    if selectors is None:
        selectors = set()

    cls_name = type(root).__name__
    if cls_name in _SKIP_CLASS_NAMES:
        return out_lines, selectors

    name = _safe_object_name(root)
    desc = f"{cls_name}{' #' + name if name else ''}"
    out_lines.append("  " * indent + desc)

    # Only create selectors if this widget has an objectName
    if name:
        sel_name = f"#{name}"
        sel_class_name = f"{cls_name}#{name}"
        # add both "#name" and "ClassName#name"
        selectors.add(sel_name)
        selectors.add(sel_class_name)
        # if parent has name, add descendant selector "parentName childName"
        if parent_name_selector:
            selectors.add(f"{parent_name_selector} {sel_name}")
            selectors.add(f"{parent_name_selector} {sel_class_name}")

        # next level parent selector for children becomes this widget's #name
        next_parent = sel_name
    else:
        # If this widget has no name, we won't generate selectors for it.
        next_parent = parent_name_selector  # propagate parent's named selector if any

    # recurse children
    try:
        children = list(root.children())
    except Exception:
        children = []

    for c in children:
        c_cls = type(c).__name__
        if c_cls in _SKIP_CLASS_NAMES:
            continue
        dump_tree(c, indent + 1, out_lines, selectors, parent_name_selector=next_parent)

    return out_lines, selectors


def generate_qss_skeleton(
    app: QApplication,
    out_path: str = "qss_skeleton.qss",
    include_top_level: bool = True,
    include_header_comment: bool = True,
) -> tuple[list[str], set[str]]:
    """
    Scan top-level widgets (or app children) and write a QSS skeleton file.
    Generates selectors only for widgets that have objectName.
    Returns (lines, selectors_set).
    """
    if not isinstance(app, QApplication):
        raise TypeError("app must be a QApplication instance")

    out_lines: list[str] = []
    selectors: set[str] = set()

    widgets = app.topLevelWidgets() if include_top_level else []
    if not widgets:
        # fallback: find QWidget children of app
        widgets = [w for w in app.children() if isinstance(w, QWidget)]

    for tw in widgets:
        dump_tree(tw, indent=0, out_lines=out_lines, selectors=selectors, parent_name_selector=None)

    # print to console for quick inspection
    print("=== Widget tree ===")
    print("\n".join(out_lines))
    print("\n=== Generated selectors ===")
    for s in sorted(selectors):
        print(s)
    print(f"\nWrote QSS skeleton to: {out_path}\nTotal selectors: {len(selectors)}")

    header = (
        [
            "/* Auto-generated QSS skeleton */",
            "/* QSS notes:",
            "   - Only selectors for widgets with objectName are generated.",
            "   - QSS does NOT support '>' child combinator — descendant uses a space.",
            "   - Fill in rule bodies below. */",
            "",
        ]
        if include_header_comment
        else []
    )

    # deterministic order: objectName-only selectors sorted
    def sort_key(s: str):
        # put '#name' first, then 'Class#name'
        if s.startswith("#"):
            p = 0
        else:
            p = 1
        return (p, s.lower())

    with open(out_path, "w", encoding="utf-8") as f:
        if header:
            f.write("\n".join(header) + "\n")
        for sel in sorted(selectors, key=sort_key):
            # empty body for user to fill
            f.write(f"{sel} {{\n\n}}\n\n")

    return out_lines, selectors


if __name__ == "__main__":
    app = QApplication.instance() or QApplication(sys.argv)
    generate_qss_skeleton(app, out_path="qss_skeleton.qss")
