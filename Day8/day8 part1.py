board = [[False for i in range(0, 50)] for i in range(0, 6)]

def draw_rect(draw_size_x, draw_size_y, board):
    for y in range(draw_size_y):
        for x in range(draw_size_x):
            board[y][x] = True

    return board

def rotate_col(col_num, by_amount, board):
    old_column = []
    # print(col_num)
    # print(by_amount)
    for row in board:
        old_column.append(row[col_num])

    for x in range(len(board)):
        board[x][col_num] = old_column[(x - by_amount)]

    return board

def rotate_row(row_num, by_amount, board):
    old_row = []

    for col in board[row_num]:
        old_row.append(col)

    for x in range(len(board[row_num])):
        board[row_num][x] = old_row[x - by_amount]

    return board

with open('input.txt') as file:
    for line in file:
        line = line.strip()
        if line.startswith('rect'):
            draw_size_x = int((line[5:].split('x'))[0])
            draw_size_y = int((line[5:].split('x'))[1])
            draw_rect(draw_size_x, draw_size_y, board)
        elif line.startswith('rotate row'):
            row_num = int((line[13:].split(' by '))[0])
            by_amount = int((line[13:].split(' by '))[1])
            rotate_row(row_num, by_amount, board)
        elif line.startswith('rotate column'):
            col_num = int((line[16:].split(' by '))[0])
            by_amount = int((line[16:].split(' by '))[1])
            rotate_col(col_num, by_amount, board)
        else:
            print('This should never happen')

count_pixels = 0
for row in board:
    print(row)
    for x in row:
        if x == True:
            count_pixels += 1

print(count_pixels)
