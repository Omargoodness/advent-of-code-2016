location = [0, 0]
facing = 0 #0: 'North', 90: 'East', 180: 'South', 270: 'West'

# Opens file and saves all the moves into one long single string
file = open('directions.txt', 'r')
moves_string = file.read()
file.close

# Takes the long moves string and turns it into a list of moves
moves = [x.strip() for x in moves_string.split(',')]

def turn(next_turn, facing):
    ''' (str, int) -> int

    Return the facing degree by taking in the current facing degree and
    the next_turn of L or R.
    
    >>> turn('R', 270)
    0
    >>> turn('L', 0)
    270
    '''

    if next_turn == 'R':
        facing = (facing + 90) % 360
    else:
        facing = (facing - 90) % 360


    return facing

def move(location, facing, number_steps):

    ''' (list of [x,y] location, int, int) -> list of new [x,y] location

    Return the new location after moving number_steps blocks in the
    given facing direction.

    >>> move([0, 3], 180, 5)
    [0, -2]
    '''

    if facing == 90:
        location[0] += number_steps
        return location
    elif facing == 180:
        location[1] -= number_steps
        return location
    elif facing == 270:
        location[0] -= number_steps
        return location
    else:
        location[1] += number_steps
        return location

for next_move in moves:
    facing = turn(next_move[0], facing)
    location = move(location, facing, int(next_move[1:]))

print(abs(0 - location[0]) + abs(0 - location[1]))
