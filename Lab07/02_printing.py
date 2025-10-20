import sys

print("Some text", "other text", sep=",", end="_")
print("Third text")
print("Normal output", file=sys.stdout)
print("Error output", file=sys.stderr)

