"""
Did I Finish my Sudoku?


Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter. If the board is valid return 'Finished!', otherwise return 'Try again!'

Sudoku rules:

Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only once.

Rows:
[image]

There are 9 rows in a traditional Sudoku puzzle. Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9.
There may not be any duplicate numbers in any row. In other words, there can not be any rows that are identical.

In the illustration the numbers 5, 3, 1, and 2 are the "givens". They can not be changed. The remaining numbers in
black are the numbers that you fill in to complete the row.

Columns:
[image]

There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain the
numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Again, there may not be any duplicate numbers in any column. Each column will be
unique as a result.

In the illustration the numbers 7, 2, and 6 are the "givens". They can not be changed. You fill in the remaining
numbers as shown in black to complete the column.

Regions
[image]

A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.

Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8,
and 9. Duplicate numbers are not permitted in any region. Each region will differ from the other regions.

In the illustration the numbers 1, 2, and 8 are the "givens". They can not be changed. Fill in the remaining numbers as
shown in black to complete the region.

Valid board example:
[image]

For those who don't know the game, here are some information about rules and how to play Sudoku:
 http://en.wikipedia.org/wiki/Sudoku and http://www.sudokuessentials.com/
"""


def done_or_not(board):  # board[i][j]
    dont = 'Try again!'
    done = 'Finished!'

    print()
    print()
    for linha in board:
        print(linha)
    print()
    print()

    columms = [board[x][y] for y in range(9) for x in range(9)]
    columms = [columms[x:x + 9] for x in range(0, 81, 9)]

    for columm in columms:
        sum_verification = 0
        for col in columm:
            sum_verification += col
        if not sum_verification == 45:
            return dont
    for rows in board:
        sum_verification = 0
        for row in rows:
            sum_verification += row
        if not sum_verification == 45:
            return dont

    regions = [board[collum][row] for row in range(0, 9, 1) for collum in range(0, 9, 1)]
    region = [regions[x:x + 3] for x in range(0, 81, 3)]

    """
    (regiao[0])    +   (regiao[3])    +  (regiao[6])
    (regiao[1])    +   (regiao[4])    +  (regiao[7])
    (regiao[2])    +   (regiao[5])    +  (regiao[8])
    (regiao[9])    +   (regiao[12])   +  (regiao[15])
    (regiao[10])   +   (regiao[13])   +  (regiao[16])
    (regiao[11])   +   (regiao[14])   +  (regiao[17])
    (regiao[18])   +   (regiao[21])   +  (regiao[24])
    (regiao[19])   +   (regiao[22])   +  (regiao[25])
    (regiao[20])   +   (regiao[23])   +  (regiao[27])

    """
    for y in range(0, 20, 9):
        for x in range(0, 3, 1):
            z = x + y
            # print(z, z + 3, z + 6)
            # regi.append(regiao[z])
            # regi.append(regiao[z+3])
            # regi.append(regiao[z+6])
            sum_verification = sum(region[z]) + sum(region[z + 3]) + sum(region[z + 6])
            if sum_verification != 45:
                return dont

    return done
