'''
    Exercise 10: Snake Game Board Renderer
    Scenario: Render a simple 2D text game board. Write a program that performs the following steps in sequence:

    Creates a 5×5 grid filled with dots "." represented as a nested list.
    Places a food item "F" at grid position [2, 3].
    Prompts the user to enter coordinate inputs: a row and a col (integers between 0 and 4) for the snake's head.
    Places the snake's head "S" at the user-supplied coordinate [row, col], overwriting the character at that position.
    If the user-supplied coordinates are exactly [2, 3], print the message "Yum! The snake ate the food!" (the snake "S" will occupy index [2, 3] on the printed board, 
    overwriting the "F").
    Prints the grid neatly line-by-line (each row's elements separated by spaces).
    Sample Input: (User inputs Row 0 and Column 3)
    Sample Output:
    . . . S .
    . . . . .
    . . . F .
    . . . . .
    . . . . .
    Sample Input: (User inputs Row 2 and Column 3)
    Sample Output:
    . . . . .
    . . . . .
    . . . S .
    . . . . .
    . . . . .
    Yum! The snake ate the food!
'''

def create_board(rows, cols):
    return [['.' for _ in range(cols)] for _ in range(rows)]

def place_food(board, food_position):
    row, col = food_position
    board[row][col] = 'F'

def place_snake(board, snake_position):
    row, col = snake_position
    if board[row][col] == 'F':
        print("Yum! The snake ate the food!")
    board[row][col] = 'S'

def print_board(board):
    for row in board:
        print(' '.join(row))

if __name__ == "__main__":
    rows, cols = 5, 5
    board = create_board(rows, cols)
    food_position = (2, 3)
    place_food(board, food_position)

    try:
        row = int(input("Enter the row for the snake's head (0-4): "))
        col = int(input("Enter the column for the snake's head (0-4): "))
        if not (0 <= row < rows) or not (0 <= col < cols):
            raise ValueError("Row and column must be between 0 and 4.")
        place_snake(board, (row, col))
        print_board(board)
    except ValueError as e:
        print(f"Invalid input: {e}")