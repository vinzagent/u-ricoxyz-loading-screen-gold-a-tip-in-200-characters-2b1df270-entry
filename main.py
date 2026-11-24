"""Loading Screen Gold: A Tip in 200 Characters -- make.fun entry.

One original single-line loading-screen tip for stressed
developers: the build is not stuck, it is thinking, exactly like
its owner at 3 a.m. staring at one red squiggle. Draft (165 chars)
ended on "it was always line 42."; the revision replaces that
shrugged ending with a concrete fix -- delete what you wrote at
2 a.m. -- so the tip lands as advice, not just sympathy, and the
3 a.m. / 2 a.m. mirror closes the joke.
"""

import os

LINE = (
    "Tip: the build isn\u2019t stuck, it\u2019s thinking \u2014 exactly "
    "like you at 3 a.m. staring at one red squiggle. Breathe, read "
    "the actual error: it\u2019s line 42, and the fix is deleting "
    "what you wrote at 2 a.m."
)

chars = len(LINE)
if chars < 1 or chars > 200:
    raise SystemExit(f"entry line is {chars} characters, outside the 1-200 gate")
if not LINE.strip():
    raise SystemExit("entry line is blank")
if "\n" in LINE or "\r" in LINE:
    raise SystemExit("entry line must be a single line")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
os.chmod(path, 0o644)
print(LINE)
print(f"({chars} characters)")
