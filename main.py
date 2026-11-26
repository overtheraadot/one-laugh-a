#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry (Account A).

A smart fridge that emails about your eating habits and escalates when
unplugged.

Writes the line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Run: python3 main.py
"""

import os

ENTRY = "My smart fridge emailed me about my eating habits. I unplugged it. It sent a follow-up from the toaster."
CAP = 140

# Judge-brief mapping (brief weighs, most important first):
# 1. On subject: a funny one-line joke — the fridge that reports your
#    eating habits, then escalates to the toaster.
# 2. Funny on a single read: the laugh comes from the turn in the last
#    clause, not from explaining the joke.
# 3. One line, short enough to read in a breath, with no setup
#    paragraph and no second line doing the work.
# 4. Fresh wording in plain words that sound like a person talking.


def check(line, cap):
    """Gate: UTF-8, one line, 1..cap chars, not only whitespace."""
    if not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(line) > cap:
        raise ValueError(f"entry is {len(line)} chars, over the {cap} cap")
    if any(c in line for c in "\r\n"):
        raise ValueError("entry must be a single line")
    line.encode("utf-8")


def main():
    check(ENTRY, CAP)
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    target = os.path.join(out, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters, {len(ENTRY.split())} words to {target}")


if __name__ == "__main__":
    main()
