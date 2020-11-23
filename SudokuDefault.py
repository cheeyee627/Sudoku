# back tracking concept
# https://www.youtube.com/watch?v=lK4N8E6uNr4&list=PLzMcBGfZo4-kE3aF6Y0wNBNih7hWRAU2o&index=2
# https://www.youtube.com/watch?v=G_UYXzGuqvM


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
    ] # sample of board

    # creating an empty list 
 



def solve (bo):
    # print(bo) can check whats going on
    find = find_empty(bo)
    if not find: # if tuple is empty, return true, all box is filled
        return True
    else:
        row, col = find
        
    for i in range(1,10):
        if valid (bo, i, (row,col)):
            bo[row][col] = i
        
            if solve (bo):
                return True
            else: 
                bo[row][col] = 0
        else: 
            bo[row][col] = 0


def valid (bo,num,pos) :
    # check each row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # check each column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # check box
    box_x=pos[1] // 3
    box_y=pos[0] // 3

    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if bo [i][j]==num and (i,j)!= pos:
                return False
    return True


def print_board(bo) : # function to display board with bounding box separators
    for i in range (len(bo)):
        if i % 3 == 0 and i != 0:
            print(" - - - - - - - - - - - - - -")        
        for j in range (len(bo[0])):
            if j % 3 == 0 :
                print(" | ", end="")# end="" means stay on line

            if j == 8 :
                    print(str(bo[i][j])+ " |")# if reaching end of the row, go the new line
            else :
                print(str(bo[i][j]) +" ", end="")

print_board(board)

def find_empty(bo) :
    for i, row in enumerate(bo):
        for j, col in enumerate(row):
            if col == 0:
                return (i,j) # row, column

    return None # trigger solve


solve (board)
print("=================================")
print_board (board)