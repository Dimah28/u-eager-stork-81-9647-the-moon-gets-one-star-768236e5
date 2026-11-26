#!/usr/bin/env python3
"""The Moon Gets One Star: one one-star review of the Moon (1-120 chars).

Writes the review to /output/entry.txt. Deterministic, Python stdlib only,
no network. The review is a genuine one-star grievance: the Moon drags the
ocean around twice a day (the tides), wakes the reviewer's dog at 3 a.m.,
never apologizes, and earns a "would not orbit again".
"""

import os
import sys

ENTRY = (
    "\u2605\u2606\u2606\u2606\u2606 It drags the ocean around twice a day, "
    "wakes my dog at 3 a.m., and never once apologized. "
    "Would not orbit again."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Validate the raw ENTRY before any normalization: a leading/trailing
    # space or an embedded newline would silently change the submitted text,
    # so reject it loudly instead of stripping it away.
    if ENTRY != ENTRY.strip():
        print(
            "error: entry must not start or end with whitespace",
            file=sys.stderr,
        )
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print(
            "error: entry must be exactly one line "
            "(no newline characters inside the text)",
            file=sys.stderr,
        )
        return 1
    text = ENTRY
    if not 1 <= len(text) <= 120:
        print(
            f"error: entry is {len(text)} characters, must be 1-120",
            file=sys.stderr,
        )
        return 1
    if not text or text.isspace():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
