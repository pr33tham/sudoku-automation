sudoku =    [[8, 1, 0, 0, 3, 0, 0, 2, 7], 
            [0, 6, 2, 0, 5, 0, 0, 9, 0], 
            [0, 7, 0, 0, 0, 0, 0, 0, 0], 
            [0, 9, 0, 6, 0, 0, 1, 0, 0], 
            [1, 0, 0, 0, 2, 0, 0, 0, 4], 
            [0, 0, 8, 0, 0, 5, 0, 7, 0], 
            [0, 0, 0, 0, 0, 0, 0, 8, 0], 
            [0, 2, 0, 0, 1, 0, 7, 5, 0], 
            [3, 8, 0, 0, 7, 0, 0, 4, 2]]

            
def printsudoku():
    print("\n\n\n")
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i][j])+" "
        print(line)

def find_next_cell_to_fill(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return -1, -1


def is_valid(sudoku, i, j, e):
    row_ok = all([e != sudoku[i][x] for x in range(9)])
    if row_ok:
        column_ok = all([e != sudoku[x][j] for x in range(9)])
        if column_ok:
            sec_topx, sec_topy = 3*(i//3), 3*(j//3)
            for x in range(sec_topx, sec_topx + 3):
                for y in range(sec_topy, sec_topy+3):
                    if sudoku[x][y] == e:
                        return False
            return True
    return False

def solve_sudoku(sudoku, i = 0, j = 0):
    i, j = find_next_cell_to_fill(sudoku)
    if i == -1:
        return True
    for e in range(1, 10):
        if is_valid(sudoku, i, j, e):
            sudoku[i][j] = e
            if solve_sudoku(sudoku, i, j):
                return True
            sudoku[i][j] = 0
    return False
    
if __name__ == "__main__":
    solve_sudoku(sudoku)
    printsudoku()
