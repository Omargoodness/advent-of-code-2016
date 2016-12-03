# Loads the sequence of move codes from the file
code = open('code.txt', 'r')

# These are the edges of the keypad
upper = [1, 2, 3]
left = [1, 4, 7]
bottom = [7, 8, 9]
right = [3, 6, 9]

current_digit = 5
code_digits = []

# Function to get the current digits for a given line of code instructions
def get_digit(instructions, current_digit):
    for i in instructions:
        if i == 'U' and current_digit not in upper:
            current_digit -= 3
        if i == 'D' and current_digit not in bottom:
            current_digit += 3
        if i == 'L' and current_digit not in left:
            current_digit -= 1
        if i == 'R' and current_digit not in right:
            current_digit += 1

    return current_digit

# Loops through every line in the code file to gather the list of digits
for line in code:
    current_digit = get_digit(line, current_digit)
    code_digits.append(current_digit)

print('Your code is', code_digits)
