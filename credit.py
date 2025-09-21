from cs50 import get_string

def luhn_valid(number_str):
    total = 0
    # iterate from the rightmost digit (index 0 of reversed)
    for i, ch in enumerate(number_str[::-1]):
        digit = int(ch)
        if i % 2 == 0:
            total += digit
        else:
            product = digit * 2
            # add digits of product (same as product // 10 + product % 10)
            total += product // 10 + product % 10
    return total % 10 == 0

def card_type(number_str):
    length = len(number_str)
    first_two = int(number_str[:2])
    first_one = int(number_str[0])

    if length == 15 and first_two in (34, 37):
        return "AMEX"
    elif length == 16 and 51 <= first_two <= 55:
        return "MASTERCARD"
    elif length in (13, 16) and first_one == 4:
        return "VISA"
    else:
        return "INVALID"

# get card number (keeps leading zeros if any)
number = get_string("Number: ").strip()

# validate numeric input
if not number.isdigit():
    print("INVALID")
else:
    if luhn_valid(number):
        print(card_type (number))
    else:
        print("INVALID")
