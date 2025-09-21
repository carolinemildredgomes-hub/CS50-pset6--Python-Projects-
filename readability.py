from cs50 import get_string

# Prompt user for text
text = get_string("Text: ")

# Count letters, words, sentences
letters = sum(1 for c in text if c.isalpha())
words = text.count(" ") + 1
sentences = sum(1 for c in text if c in ".!?")

# Coleman–Liau index
L = (letters / words) * 100
S = (sentences / words) * 100
index = 0.0588 * L - 0.296 * S - 15.8

# Round to nearest int
grade = round(index)

# Output grade level
if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print(f"Grade {grade}")
