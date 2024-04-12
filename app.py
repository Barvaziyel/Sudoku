import copy
import random
from flask import Flask, render_template

EMPTY_CELL_CHAR = 0
DEFAULT_DIFFICULTY = 20
GRID_SQUARE_SIZE = 3
GRID_SIZE = 9

app = Flask(__name__)


@app.route('/')
def fetch_sudoku():
    """
    Create a sudoku puzzle and solution and render the sudoku.html template
    return: the rendered template
    """
    puzzle, solution = create_puzzle()
    return render_template('sudoku.html', grid=puzzle, solution=solution)


def check_row(sudoku, row, num):
    """
    Check if a number is in a row
    @param sudoku: The sudoku puzzle
    @param row: The row to check
    @param num: The number to check for
    return: True if the number is in the row, False otherwise
    """
    return num in sudoku[row]


def check_column(sudoku, column, num):
    """
    Check if a number is in a column
    @param sudoku: The sudoku puzzle
    @param column: The column to check
    @param num: The number to check for
    return: True if the number is in the column, False otherwise
    """
    for row in range(GRID_SIZE):
        if num == sudoku[row][column]:
            return True
    return False


def check_square(sudoku, cur_row, cur_column, num):
    """
    Check if a number is in a 3x3 square
    @param sudoku: The sudoku puzzle
    @param cur_row: The row of the cell
    @param cur_column: The column of the cell
    @param num: The number to check for
    return: True if the number is in the 3x3 square, False otherwise
    """
    for row in range(GRID_SIZE):
        if not row // GRID_SQUARE_SIZE == cur_row // GRID_SQUARE_SIZE:
            continue
        for col in range(GRID_SIZE):
            if not col // GRID_SQUARE_SIZE == cur_column // GRID_SQUARE_SIZE:
                continue
            if num == sudoku[row][col]:
                return True
    return False


def add_number_to_grid(available_nums, row, col, proposed_num, sudoku):
    """
    Add a number to the sudoku grid
    @param available_nums: The list of available numbers
    @param row: The row to add the number to
    @param col: The column to add the number to
    @param proposed_num: The number to add
    @param sudoku: The sudoku puzzle
    return: the updated list of available numbers, the updated list of numbers that haven't been
    tried and a flag indicating that the number was successfully added to the grid
    """
    sudoku[row][col] = proposed_num
    # Remove the number from the list of available numbers
    available_nums = [num for num in available_nums if num != proposed_num]
    # Reset the list of numbers that haven't been tried
    not_tried_nums = available_nums
    return available_nums, not_tried_nums, True


def create_solved_sudoku():
    """
    Create a solved sudoku puzzle
    return: the solved sudoku puzzle
    """
    not_found = True
    while not_found:
        sudoku = [[EMPTY_CELL_CHAR for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        for row in range(GRID_SIZE):
            available_nums = [num for num in range(1, GRID_SIZE + 1)]
            for col in range(GRID_SIZE):
                success = False
                not_tried_nums = available_nums
                while not success:
                    # If there are no numbers left to try, break the loop
                    if not len(not_tried_nums):
                        break
                    # Pick a random number from the list of numbers that haven't been tried
                    proposed_num = not_tried_nums[random.randint(0, len(not_tried_nums) - 1)]
                    # Remove the number from the list of numbers that haven't been tried
                    not_tried_nums = [num for num in not_tried_nums if num != proposed_num]

                    # Check if the number is already in the row, column or square
                    if check_row(sudoku, row, proposed_num) or check_column(sudoku, col, proposed_num) \
                            or check_square(sudoku, row, col, proposed_num):
                        continue

                    # If number is safe to place in current cell, add it to the sudoku grid
                    available_nums, not_tried_nums, success = add_number_to_grid(available_nums, row, col, proposed_num, sudoku)
                # If there are available numbers but none that haven't been tried, break the loop
                if len(available_nums) and not len(not_tried_nums):
                    break
            if len(available_nums) and not len(not_tried_nums):
                break
            # If the last row has been reached, a valid sudoku has been found
            if row == GRID_SIZE - 1:
                not_found = False
    return sudoku


def check_if_solved(sudoku):
    """
    Check if a sudoku puzzle has been solved
    @param sudoku: The sudoku puzzle to check
    return: True if the sudoku puzzle has been solved, False otherwise
    """
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if sudoku[row][col] == EMPTY_CELL_CHAR:
                return False
    return True


def eliminate_options(sudoku, possible_nums, cur_row, cur_col):
    """
    Eliminate options from the list of possible numbers for a cell
    @param sudoku: The sudoku puzzle
    @param possible_nums: The list of possible numbers for each cell
    @param cur_row: The row of the cell
    @param cur_col: The column of the cell
    return: the updated list of possible numbers
    """
    orig_options_len = len(possible_nums)
    # Eliminate numbers that are in the row of the cell
    possible_nums = [num for num in possible_nums if num not in sudoku[cur_row]]
    # Eliminate numbers that are in the column of the cell
    for row in range(GRID_SIZE):
        possible_nums = [num for num in possible_nums if num != sudoku[row][cur_col]]
    # Eliminate numbers that are in the square of the cell
    for row in range(GRID_SIZE):
        if not row // GRID_SQUARE_SIZE == cur_row // GRID_SQUARE_SIZE:
            continue
        for col in range(GRID_SIZE):
            if not col // GRID_SQUARE_SIZE == cur_col // GRID_SQUARE_SIZE:
                continue
            possible_nums = [num for num in possible_nums if num != sudoku[row][col]]
    return len(possible_nums) < orig_options_len, possible_nums


def solve_sudoku(orig_sudoku):
    """
    Solve a sudoku puzzle
    @param orig_sudoku: The sudoku puzzle to solve
    return: either the solved sudoku puzzle or None if the puzzle can't be solved
    """
    # Create a list of possible numbers for each cell
    sudoku = copy.deepcopy(orig_sudoku)
    possible_nums = [[[i for i in range(1, GRID_SIZE + 1)] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    changed = True
    not_solved = True
    while not_solved and changed:
        changed = False
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                # If the cell is already filled, skip it
                if sudoku[row][col] != EMPTY_CELL_CHAR:
                    continue
                # Eliminate options from the list of possible numbers for the cell
                changed, possible_nums[row][col] = eliminate_options(sudoku, possible_nums[row][col], row, col)
                # If there is only one possible number for the cell, add it to the sudoku puzzle
                if len(possible_nums[row][col]) == 1:
                    sudoku[row][col] = possible_nums[row][col][0]
        # Check if the sudoku puzzle has been solved
        if check_if_solved(sudoku):
            not_solved = False

    return sudoku if changed else None


def create_puzzle(difficulty=DEFAULT_DIFFICULTY):
    """
    Create a sudoku puzzle
    Remove numbers from a solved sudoku puzzle one by one until a [parameter 'difficulty'] of failed removals that made the
    puzzle unsolvable.
    @param difficulty: The difficulty of the puzzle, number of failed removals before the puzzle is returned
    return: a tuple containing the puzzle and the solution
    """
    sudoku = create_solved_sudoku()
    # Remove numbers from the solved sudoku puzzle to create a puzzle
    failed_removals = 0
    while True:
        # Choose a random cell to remove a number from
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - 1)
        # If the cell is already empty, skip it
        if sudoku[row][col] == EMPTY_CELL_CHAR:
            continue
        # Remove the number from the cell, and save it in case it needs to be added back
        removed_num = sudoku[row][col]
        sudoku[row][col] = EMPTY_CELL_CHAR
        # Check if the sudoku puzzle can still be solved
        if not solve_sudoku(sudoku):
            failed_removals += 1
            # add the removed number back to the sudoku puzzle
            sudoku[row][col] = removed_num
            # If the number of failed removals is greater than the difficulty, return the puzzle
            if failed_removals > difficulty:
                return sudoku, solve_sudoku(sudoku)


if __name__ == '__main__':
    app.run()
