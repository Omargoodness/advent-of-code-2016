shape_list = []
valid_triangles = 0

def is_valid_triangle(sides_list):
    ''' (list) -> bool

    Checks to see if a list of 3 sides from sides_list is a valid triangle.
    
    >>> is_valid_triangle([5, 10, 25])
    False
    '''
    s1 = sides_list[0]
    s2 = sides_list[1]
    s3 = sides_list[2]
    
    if ((s1 + s2) > s3) and ((s1 + s3) > s2) and ((s2 + s3) > s1):
        return True

    return False
    

# Open the input.txt file and process each line storing the sides as a list
file = open('input.txt', 'r')

# Loop through each line in the input file, and check to see if the list of
# sides for that line is a valid triangle.
for line in file:
    sides_list = [int(line[:5]), int(line[5:10]), int(line[10:])]
    if is_valid_triangle(sides_list):
        valid_triangles +=1

file.close()

print('You have', valid_triangles, 'valid triangles.')
