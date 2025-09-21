import csv
import sys

# Usage check
if len(sys.argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    sys.exit(1)

# Load database
with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    database = list(reader)

# Load DNA sequence
with open(sys.argv[2]) as file:
    sequence = file.read().strip()

# Find STRs from the database header
strs = reader.fieldnames[1:]  # skip 'name'

# Function to compute longest run of an STR in the sequence


def longest_match(sequence, subsequence):
    longest = 0
    length = len(subsequence)
    for i in range(len(sequence)):
        count = 0
        while sequence[i + count*length: i + (count+1)*length] == subsequence:
            count += 1
        longest = max(longest, count)
    return longest


# Compute STR counts for the sequence
counts = {s: longest_match(sequence, s) for s in strs}

# Compare with each person in the database
for person in database:
    if all(int(person[s]) == counts[s] for s in strs):
        print(person["name"])
        sys.exit(0)

print("No match")
