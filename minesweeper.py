import tkinter as tk
import random
from tkinter import messagebox

# Grid size and number of bombs
grid_size = 8
num_bombs = 10

# Function to create a cell using dictionaries
def create_cell(row, col):
    # A cell is represented as a dictionary with the following properties:
    # 'row': Row index of the cell
    # 'col': Column index of the cell
    # 'mine': Flag indicating if the cell contains a bomb
    # 'adjacent_mines': Number of adjacent cells containing bombs
    # 'revealed': Flag indicating if the cell has been revealed
    return {'row': row, 'col': col, 'mine': False, 'adjacent_mines': 0, 'revealed': False}

# Function to place bombs randomly on the grid
def place_bombs(grid):
    for a in range(num_bombs):
        while True:
            try:
                # Generate random coordinates
                x = random.randint(0, grid_size - 1)
# Function to place bombs randomly on the grid
def place_bombs(grid):
    for a in range(num_bombs):
        while True:
            try:
                # Generate random coordinates
                x = random.randint(0, grid_size - 1)
                y = random.randint(0, grid_size - 1)
                # Check if the cell is empty (not containing a bomb)
                if not grid[x][y]['mine']:
                    # Place a bomb in the cell
                    grid[x][y]['mine'] = True
                    break
            except IndexError:
                continue

# Function to count the number of bombs around a given cell
def count_bombs_around(grid, i, j):
    count = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            try:
                # Check the neighboring cells within the grid boundaries
                if 0 <= i + x < grid_size and 0 <= j + y < grid_size:
                    # Check if the neighboring cell contains a bomb
                    if grid[i + x][j + y]['mine']:
                        count += 1
            except IndexError:
                continue
    return count

# Function to create the reveal command for a button
def create_reveal_command(buttons, grid, a, b):
    def reveal_command():
        try:
            if grid[a][b]['mine']:
                buttons[a][b].config(text="B")  # Set the button text to "B" to indicate a bomb
                show_game_over_message()
            elif grid[a][b]['adjacent_mines'] == 0:
                value = count_bombs_around(grid, a, b)
                buttons[a][b].config(text=str(value))
        except IndexError:
            return
    return reveal_command

# Function to show the game over message
def show_game_over_message():
    messagebox.showinfo("Game Over", "You revealed a bomb! Game Over.")

# Function to create the buttons for the game grid
def create_buttons(window, grid):
    buttons = []
    for a in range(grid_size):
        row_buttons = []
        for b in range(grid_size):
            button = tk.Button(window, width=3, height=1)
            button.grid(row=a, column=b)
            button.config(command=create_reveal_command(buttons, grid, a, b))
            row_buttons.append(button)
        buttons.append(row_buttons)
    return buttons

# Function to start the game
def start_game():
    # Create the game grid
    grid = [[create_cell(row, col) for col in range(grid_size)] for row in range(grid_size)]

    # Place bombs on the grid
    place_bombs(grid)

    # Create the game window
    window = tk.Tk()
    window.title("Minesweeper")

    # Create the buttons for the grid
    buttons = create_buttons(window, grid)

    # Start the game loop
    window.mainloop()

# Start the game
start_game()
