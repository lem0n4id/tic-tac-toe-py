'''CLI tic-tac-toe game

This script allows the user to play a 2 player agme of tic-tac-toe
on the command line. The board is 0-indexed.

This script requires no extra modules to be installed within the Python
environment you are running this script in.
'''

# nested list to store X & O
positions = [[' ' for i in range(3)], [' ' for i in range(3)], [
    ' ' for i in range(3)]]

welcomeMessage = '''
Welcome to cli tic-tac-toe!
     columns
 r  1 | 2 | 3 
 o ---|---|---
 w  4 | 5 | 6
 s ---|---|---
    7 | 8 | 9
Valid inputs are from 0,0 <- 1st cell to 2,2 <-9th cell

Example- 2,1 <- 8th cell (2 is row index, 0 in column index)

Good Luck!
'''


def isAllThreeInRow() -> tuple:
    '''Checks if the game is won by having 3 marks in a column'''
    xRow = ['X' for i in range(3)]
    oRow = ['O' for i in range(3)]
    for row in positions:
        if row == xRow:
            return True, 'Player1 won!'
        elif row == oRow:
            return True, 'Player2 won!'
    return False, ''


def isAllThreeInColumn() -> tuple:
    '''Checks if the game is won by having 3 marks in a column'''
    xColumn = ['X']*3
    oColumn = ['O']*3
    columns = []
    for col in range(3):
        column = [positions[row][col] for row in range(3)]
        columns.append(column)
    if xColumn in columns:
        return True, 'Player1 won!'
    elif oColumn in columns:
        return True, 'Player2 won!'
    else:
        return False, ''


def isAllThreeDiagonal() -> tuple:
    '''Checks if the game is won by having 3 marks in a diagonal'''
    leftDiagonal = [positions[0][0], positions[1][1], positions[2][2]]
    rightDiagonal = [positions[0][2], positions[1][1], positions[2][0]]

    if (leftDiagonal == ['X']*3) or (rightDiagonal == ['X']*3):
        return True, 'Player1 won!'
    elif (leftDiagonal == ['O']*3) or (rightDiagonal == ['O']*3):
        return True, 'Player2 won!'
    return False, ''


def isDraw() -> tuple:
    '''Checks if the game is draw'''
    countOfMovesMade = 0
    for row in positions:
        for item in row:
            if item != ' ':
                countOfMovesMade += 1

    if countOfMovesMade == 9:
        return True
    return False


def isGameOver() -> tuple:
    '''Checks if the game is over'''

    # all three in a row
    if isAllThreeInRow()[0]:
        return isAllThreeInRow()
    # all three in a column
    elif isAllThreeInColumn()[0]:
        return isAllThreeInColumn()
    # all three in a diagonal
    elif isAllThreeDiagonal()[0]:
        return isAllThreeDiagonal()
    # draw
    elif isDraw():
        return True, 'It\'s a draw!'
    else:
        return False, ''


def isValidMove(row: int, column: int) -> bool:
    '''
    Checks if the position is already occupied or is within the 
    index of the tic-tac-toe board
    '''
    try:
        if positions[row][column] != ' ':
            return False
        return True
    except IndexError:
        return False


def makeMove(row: int, column: int, mark: str) -> None:
    '''Adds the mark of the player in the tic-tac-toe board '''
    positions[row][column] = mark


def takeInput(player: str) -> tuple:
    '''Takes imput from the user and returns the row and column'''
    move = input(f'{player} enter your play: ')
    row, column = [int(i) for i in move.split(',')]
    return row, column


def generateBoard(x: list) -> None:
    '''generates and prints the board from the stored positions'''
    board = f' {x[0][0]} | {x[0][1]} | {x[0][2]} \n---|---|---\n {x[1][0]} | {x[1][1]} | {x[1][2]} \n---|---|---\n {x[2][0]} | {x[2][1]} | {x[2][2]} '
    print(board)


def main() -> None:
    print(welcomeMessage)
    generateBoard(positions)
    players = {'X': 'Player1', 'O': 'Player2'}
    # Game loop
    moves = 0
    while not isGameOver()[0]:

        if moves % 2 == 0:
            # player1's move
            mark = 'X'
        else:
            # player2's move
            mark = 'O'

        player = players[mark]
        # User Input
        try:
            row, column = takeInput(player)
        except ValueError:
            print('Invalid input! Try again')
            continue

        if not isValidMove(row, column):
            print('Invalid move! Try again')
            continue

        makeMove(row, column, mark)
        generateBoard(positions)
        moves += 1
    else:
        print(isGameOver()[1])


if __name__ == "__main__":
    main()
