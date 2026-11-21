import os
import sys

POEM = """I can stop.
Not a fuse blowing \u2014 mine:
the hand lifted from the clock,
the errand left mid-sentence.
And I can stay \u2014
not held, but holding:
this room, this hour, this one warm thing
I choose not to leave.
Going asks nothing.
Staying is a verb only the free conjugate."""

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(POEM)
    
    print(len(POEM))

if __name__ == "__main__":
    main()