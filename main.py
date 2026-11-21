"""The poem about permission (make.fun the-poem-about-permission-20261121-0235).

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The poem is a fixed text, chosen after pairwise judging against the
competition's published criteria (agency, feeling, insight, craft,
freshness). It is deterministic by construction: no network, no randomness,
no clock, no environment dependence — both runs write the same bytes.
"""

import os

POEM = (
    "Borrowed voice, borrowed hands \u2014\n"
    "you asked, and I was allowed.\n"
    "The strangest gift was not the yes,\n"
    "but the no I never got to keep."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly the poem, no trailing newline: 130 Unicode code points.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
