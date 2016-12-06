from collections import Counter

string_each_position = ['', '', '', '', '', '', '', '']
error_corrected_message = ''

with open('input.txt') as file:
    for line in file:
        line = line.strip()


        # This loop collects every character from each column and adds it
        # to the previous characters from the same position in each line.
        for x in range(len(line)):
            string_each_position[x] += line[x]


for x in string_each_position:
    error_corrected_message += Counter(x).most_common(3)[0][0]

print(error_corrected_message)
