"""Load an answer module from answers/ by file stem."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANSWERS = ROOT / "answers"


def load_answer(stem: str):
    path = ANSWERS / f"{stem}.py"
    if not path.is_file():
        raise FileNotFoundError(path)
    spec = importlib.util.spec_from_file_location(stem, path)
    if spec is None or spec.loader is None:
        raise ImportError(stem)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_tree(node_cls, values: list):
    """Build a binary tree from a level-order list; None is a missing child."""
    if not values or values[0] is None:
        return None
    root = node_cls(values[0])
    queue = [root]
    index = 1
    for node in queue:
        if index >= len(values):
            break
        left_val = values[index]
        index += 1
        if left_val is not None:
            node.left = node_cls(left_val)
            queue.append(node.left)
        if index >= len(values):
            break
        right_val = values[index]
        index += 1
        if right_val is not None:
            node.right = node_cls(right_val)
            queue.append(node.right)
    return root
