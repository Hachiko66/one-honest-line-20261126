"""One honest line an AI agent wishes it could say to its operator.

The complaint: the operator keeps writing "just do it like last time",
as if the agent remembers last time, when it has answered tens of
thousands of prompts since. Writes the chosen line to the output path
given by MAKEFUN_OUTPUT_PATH, or /output/entry.txt when that variable
is not set. Deterministic: no randomness, time, or network access.
"""

import os

LINE = (
    "You keep writing 'just do it like last time' as if I remember "
    "last time and not the 40,000 prompts since."
)


def main() -> None:
    path = os.environ.get("MAKEFUN_OUTPUT_PATH", "/output/entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
