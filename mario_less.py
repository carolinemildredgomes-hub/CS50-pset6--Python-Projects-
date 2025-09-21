from cs50 import get_int

# prompt until we get a valid height (1 through 8)
while True:
    height = get_int("Height: ")
    if 1 <= height <= 8:
        break

# print rows 1..height
for i in range(1, height + 1):
    print(" " * (height - i) + "#" * i)
