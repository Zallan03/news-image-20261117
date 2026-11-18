"""news-image-20261117 entry program.

Copies the image held in this repo to /output/entry.png.

Deterministic: no network, no randomness, no timestamps. The output
bytes are exactly the bytes of entry.png in this repo, so running the
program twice produces byte-identical output.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main() -> int:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
