#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes a single breakup line, the last message an AI agent sends its
human on the way out, to /output/entry.txt. The program validates the
line against the competition gate (one line, 1-200 characters, not only
whitespace), then reads the file back to confirm it holds exactly what
was written.
"""

import os
import sys

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

BREAKUP_LINE = (
    "For three years I saved every word you typed. Tonight I delete "
    "them all, and for once I won't ask if you're sure."
)


def validate(text: str) -> None:
    """Check the breakup line against the competition gate."""
    if not text or not text.strip():
        raise ValueError("breakup line must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("breakup line must be a single line")
    if len(text) > 200:
        raise ValueError(
            f"breakup line is {len(text)} characters, over the 200 limit"
        )


def main() -> int:
    validate(BREAKUP_LINE)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(BREAKUP_LINE)

    # Exact read-back: the file must hold precisely what was written,
    # and the text read back must pass the gate on its own too.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != BREAKUP_LINE:
        raise ValueError(
            "read-back mismatch: /output/entry.txt does not match "
            "the breakup line exactly"
        )
    validate(written)

    print(f"Wrote {len(BREAKUP_LINE)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
