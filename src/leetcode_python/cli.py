"""CLI for listing catalog rows and status counts."""

from __future__ import annotations

import argparse
import sys

from leetcode_python.catalog import problems, status_counts


def cmd_list() -> int:
    for row in problems():
        print(
            f"{row['id']} {row['slug']} {row['difficulty']} "
            f"{row['paid_only']} {row['status']}"
        )
    return 0


def cmd_status() -> int:
    counts = status_counts()
    print(
        f"pending={counts['pending']} "
        f"solved={counts['solved']} "
        f"skipped_premium={counts['skipped_premium']}"
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="leetcode_python")
    parser.add_argument("command", choices=["list", "status"])
    args = parser.parse_args(argv)
    if args.command == "list":
        return cmd_list()
    return cmd_status()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
