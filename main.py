"""Write one one-line joke about working beside an AI coding agent."""

import os
import sys
from pathlib import Path

JOKE = "I spent an hour reviewing my AI agent's pull request before realising its brilliant fix was the exact code I'd deleted that morning, returned with a confident comment explaining why it works now."


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or str(Path(__file__).resolve().parent)
    output_path = Path(output_dir) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Sealed gate requires entry.txt to be 1-280 chars; never write an
    # out-of-range or blank joke (len() counts Unicode code points).
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        print("error: JOKE must be 1-280 non-whitespace characters", file=sys.stderr)
        return 1
    output_path.write_text(JOKE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
