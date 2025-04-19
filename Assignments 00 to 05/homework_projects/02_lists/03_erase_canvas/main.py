from graphics import Canvas
import time

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser."""
    # Get mouse coordinates to help us know which cells to erase
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()

    # Calculate the boundaries of the eraser
    left_x = mouse_x - ERASER_SIZE // 2  # Center the eraser on the mouse
    top_y = mouse_y - ERASER_SIZE // 2
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    # Find overlapping objects (cells) with the eraser's boundaries
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

    # For each overlapping object, change its color to white (erase it)
    for obj in overlapping_objects:
        if obj != eraser:  # Skip the eraser itself
            canvas.set_color(obj, 'white')

def main():
    # Create the canvas object
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Number of rows and columns in the grid
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    # Draw the grid of cells (rectangles)
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            # Create each cell as a blue rectangle
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

    # Wait for user click to initialize the eraser
    canvas.wait_for_click()
    last_click_x, last_click_y = canvas.get_last_click()  # Get the initial position of the eraser

    # Create the eraser as a pink rectangle
    eraser = canvas.create_rectangle(
        last_click_x, 
        last_click_y, 
        last_click_x + ERASER_SIZE, 
        last_click_y + ERASER_SIZE, 
        'pink'
    )

    # Main loop: move the eraser and erase cells in contact with it
    while True:
        # Get the current mouse position
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()

        # Move the eraser to the mouse position
        canvas.moveto(eraser, mouse_x - ERASER_SIZE // 2, mouse_y - ERASER_SIZE // 2)

        # Erase any overlapping cells with the eraser
        erase_objects(canvas, eraser)

        # Pause to allow the screen to update smoothly
        time.sleep(0.05)

if __name__ == '__main__':
    main()
