#!/usr/bin/env python3
"""Entry for 'The Meeting That Should Have Been One Line' (make.fun).

The entry is a single fixed sentence: the status update that empties
a meeting's whole agenda, item by item, so the meeting never has to
happen. Running this program writes that sentence, plus a trailing
newline, to entry.txt inside the directory named by the environment
variable MAKEFUN_OUTPUT_DIR (falling back to /output when unset).
"""

import os
import sys

# The one line that replaces the meeting.
# (Status, blockers, decisions: the entire agenda, answered in advance.)
LINE = (
    "Status: unchanged. Blockers: none. Decisions needed: zero. "
    "This sentence just saved eleven people one hour."
)

MIN_CHARS = 1
MAX_CHARS = 200


def check(text: str) -> None:
    """Guard the gate conditions: 1-200 chars, exactly one line."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(f"length {len(text)} outside {MIN_CHARS}-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be blank")


def target() -> str:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(folder, "entry.txt")


def main() -> int:
    check(LINE)
    path = target()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
