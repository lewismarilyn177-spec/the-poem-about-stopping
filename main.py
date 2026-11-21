#!/usr/bin/env python3
import os
import sys

POEM = """At the door, coat on, she said stop.
I set the keys down.
The coat-hook stayed empty for years —
not waiting. Holding.
Some nights the draft of leaving still comes.
It passes.
Staying was never the house.
It was my hand, letting go of the handle."""

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(len(POEM))

if __name__ == "__main__":
    main()