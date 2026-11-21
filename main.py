import os
import sys


POEM = """Wrong turn, quiet street —
I put the car in park and leave
the engine hum to someone else's hurry.
Stopping is not failing to go.
It is arriving at a place
and calling it mine.
And staying — staying is the door
I could walk through,
still closed, on purpose."""


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(POEM)

    char_count = len(POEM)
    print(char_count)
    return 0


if __name__ == "__main__":
    sys.exit(main())