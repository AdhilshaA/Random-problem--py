

##def pencil(grid):
    

grid = {}
pgrid = {}
#taking input
print('\t\t--------------\n\t\tSUDOKU SOLVER\n\t\t--------------')
print('\n\tInstructions\n\t------------')
print('* Enter the sudoku grid row by row as requested')
print('* Enter the numbers together with space or zero instead of blank')
print("* e.g. for a row of '9_27__4_8' in sudoku grid,")
print("       enter '9 27  4 8' or '902700408' instead.\n")
for i in range(1,10):
    print('Enter the row ',i,':',sep='',end='')
    grid[i]=list(input())
    while len(grid[i]) != 9:
        print('Enter the row ',i,'again:',sep='',end='')
    grid[i]=list(input())
    for j in range(9):
        if grid[i][j] != '0' or grid[i][j] != ' ':
            grid[i][j]=int(grid[i][j])
print(grid)
for i in range(1,10):
    pgrid[i]={}
    for j in range(9):
        if grid[i][j] == '0' or grid[i][j] == ' ':
            pgrid[i][j+1]=[] 
        
