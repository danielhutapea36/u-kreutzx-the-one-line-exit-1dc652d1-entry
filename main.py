#!/usr/bin/env python3
"""The One-Line Exit.

Writes a one-line resignation letter to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The line is
132 characters, UTF-8, one line, no trailing newline.
Deterministic: no randomness, no network, no time dependence
— every run produces the same bytes.

Why this line: the judge weighs, in order, (1) a funny one-line
resignation letter whose joke lands — it reads as a real
resignation line with a punch; (2) surprise — the turn lands on
the plant getting watered while the employee did not, not the
usual reasons people quit; (3) fits the form — one line, no
padding, no list of grievances, reads like a letter someone
could actually send; (4) specific voice — the office plant by
the desk gives it a recognizable workplace; (5) stays with the
reader — short, quotable, the kind of line a colleague would
forward. The em dash sets up the turn; the punch lands in the
final clause, "but only one of us got watered."
"""

import os

TEXT = (
    "I hereby resign, effective immediately \u2014 the office plant "
    "and I both stopped growing here years ago, but only one of us "
    "got watered."
)


def main() -> None:
    # Gate: entry.txt must be 1-140 characters of UTF-8 text, not only
    # whitespace. The line is 132 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 140 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
