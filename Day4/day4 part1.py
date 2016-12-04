from collections import Counter

# This function counts the number of chars in the room name, then sorts it by
# alphabetical character and most frequent occurence
def get_char_count(room_name):
    char_count = Counter(room_name).most_common() # List of char counts
    char_count.sort() # First sort by alphabetical order
    char_count.sort(key=lambda x: x[1], reverse=True) # Final sort by char count
    return char_count

file = open('input.txt', 'r')

sector_id_sum = 0

for room in file:
    room = room.rstrip('\n') # remove the new line char at end of string
    room_name = room[0:-10].replace('-','') # remove hyphens from room name
    sector_id = int(room[-10:-7])
    checksum = room[-6:-1]

    decrypted_name = ''

    sorted_char_count = get_char_count(room_name)

    # This loops through the first five characters in the sorted_char_count
    for x in range(0,5):
        decrypted_name += sorted_char_count[x][0]

    # Check to see if the decrypted room name is identical to the checksum
    if decrypted_name == checksum:
        sector_id_sum += sector_id
    

file.close()

print('The sum of Sector IDs for valid rooms is:', sector_id_sum)
