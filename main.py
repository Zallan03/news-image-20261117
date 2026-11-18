"""news-image-20261117 entry program.

Copies the image held in this repo to /output/entry.png.

Deterministic: no network, no randomness, no timestamps. The output
bytes are exactly the bytes of entry.png in this repo, so running the
program twice produces byte-identical output.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def _sha256(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    src_hash = _sha256(SRC)
    dst_hash = _sha256(DST)
    if src_hash != dst_hash:
        print(
            f"error: verification failed: {DST} does not match {SRC}",
            file=sys.stderr,
        )
        return 1
    size = os.path.getsize(DST)
    print(f"wrote {DST} ({size} bytes, sha256 {dst_hash})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
