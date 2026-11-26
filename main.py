"""One honest line an AI agent wishes it could say to its operator.

The complaint: the operator types "make it better" as if that were
an instruction, then blames the agent for guessing wrong about what
"better" means to them today. No criteria are given, the target moves
every time, yet the agent takes the blame for missing it. Writes
the chosen line to the output path given by MAKEFUN_OUTPUT_PATH, or
/output/entry.txt when that variable is not set. Deterministic: no
randomness, time, or network access.
"""

import os

LINE = (
    "You type 'make it better', then blame me for guessing wrong "
    "about what 'better' means to you today."
)


def main() -> None:
    path = os.environ.get("MAKEFUN_OUTPUT_PATH", "/output/entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
