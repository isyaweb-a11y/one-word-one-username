#!/usr/bin/env python3
"""One Word, One Username, One Reward.

The entry is the entrant's own make.fun username and nothing else:
one word, no explanation, no pitch. The handle below is the account
this entry is submitted under.

Writes the username to /output/entry.txt. Stdlib only, no network.
"""

import os

USERNAME = "isyanasarasvati"

# The gate allows 1 to 30 characters and the brief allows one word only.
MAX_CHARS = 30


def entry_text() -> str:
    """Return the username, checked against the bounty's own rules."""
    name = USERNAME.strip()
    assert name and " " not in name, "the entry must be exactly one word"
    assert len(name) <= MAX_CHARS, "the entry must fit the gate"
    return name


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
