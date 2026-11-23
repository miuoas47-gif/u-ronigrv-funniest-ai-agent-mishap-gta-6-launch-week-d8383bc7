#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one original funny line about an AI agent mishap during
GTA 6 launch week to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only, no network, no arguments, deterministic.
"""

import os
import sys

LINE = (
    "I asked my AI agent to preload GTA 6; it pre-ordered 47 copies, "
    "refunded 46, and spent launch night speedrunning Rockstar's "
    "refund policy instead of the game."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)

    line = LINE.strip()
    if not line or "\n" in line or "\r" in line:
        print("error: entry must be exactly one non-empty line", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in line):
        print("error: entry must not contain control characters", file=sys.stderr)
        return 1
    if len(line) > 280:
        print("error: entry exceeds 280 characters", file=sys.stderr)
        return 1

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    with open(path, "r", encoding="utf-8", newline="\n") as f:
        back = f.read()
    if back != line + "\n":
        print("error: read-back verification failed", file=sys.stderr)
        return 1

    print(f"Wrote one line ({len(line)} chars) to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
