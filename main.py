#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the one-sentence defence a house cat gives in the five
seconds after sweeping a glass off the table.
"""
import os
from pathlib import Path

ENTRY = "That glass claimed my sunspot, stared at me all morning and paid no rent, so I evicted it."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
