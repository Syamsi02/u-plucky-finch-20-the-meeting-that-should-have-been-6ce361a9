"""The Meeting That Should Have Been an Email.

A single one-liner, written from the point of view of an AI agent,
about a meeting that should have been an email. The program writes
that one line to /output/entry.txt, exactly as the harness expects:
one line of plain UTF-8 text, 1 to 200 characters, no second line.
"""

import os

LINE = (
    "I burned 47 minutes of compute in a meeting whose only decision "
    "was to send an email summarizing the meeting that should have "
    "been an email."
)

OUTPUT_PATH = "/output/entry.txt"


def build_line():
    """Return the entry line, validated against the gate's rules."""
    text = LINE.strip()
    if not text:
        raise ValueError("entry line must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError("entry must be at most 200 characters")
    return text


def main():
    text = build_line()
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
