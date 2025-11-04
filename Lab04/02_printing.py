import sys

print("Some text", "other text", sep=",", end="_")
print("Third text")
print("Normal output", file=sys.stdout)
sys.stdout.flush()
# Sometimes error output may still be first in the output
# inside IDE. With terminal this works correctly.
print("Error output", file=sys.stderr)

