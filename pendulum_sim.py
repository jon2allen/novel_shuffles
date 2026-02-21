import curses
import time
import random

def pendulum_shuffle_gen(arr):
    """
    Generator that yields the array state, boundaries, and active index 
    after every step to allow for animation.
    """
    left = 0
    right = len(arr) - 1
    turn = 0
    
    while left < right:
        # Pick from the shrinking unshuffled window
        j = random.randint(left, right)
        
        if turn % 2 == 0:
            arr[left], arr[j] = arr[j], arr[left]
            yield arr, left, right, left, "LEFT"
            left += 1
        else:
            arr[right], arr[j] = arr[j], arr[right]
            yield arr, left, right, right, "RIGHT"
            right -= 1
            
        turn += 1
        
    yield arr, left, right, left, "DONE"

def draw_state(stdscr, arr, left, right, active_idx, status):
    max_y, max_x = stdscr.getmaxyx()
    stdscr.erase()
    
    # Text overlay
    stdscr.addstr(0, 2, f" Pendulum Shuffle Visualizer ", curses.color_pair(4) | curses.A_BOLD)
    stdscr.addstr(1, 2, f" Status: {status} | Left: {left} | Right: {right} ", curses.color_pair(1))

    # Draw the array as a bar graph
    for x in range(len(arr)):
        if x >= max_x:  # Prevent drawing off-screen
            break
            
        val = arr[x]
        
        # Determine color based on whether the element is locked in
        if x < left:
            color = curses.color_pair(2) # Left boundary (Cyan)
        elif x > right:
            color = curses.color_pair(3) # Right boundary (Magenta)
        else:
            color = curses.color_pair(1) # Unshuffled window (White)
            
        # Draw the column
        for y in range(val):
            draw_y = max_y - 1 - y
            if draw_y > 2: # Keep top rows clear for text and pendulum marker
                # Draw block character
                stdscr.addch(draw_y, x, '█', color)
                
    # Draw the "Pendulum Bob" swinging indicator
    if status != "DONE" and active_idx < max_x:
        # Calculate top of the current bar
        top_of_bar = max_y - 1 - arr[active_idx]
        if top_of_bar > 2:
            stdscr.addch(top_of_bar - 1, active_idx, '▼', curses.color_pair(4) | curses.A_BOLD)

    stdscr.refresh()

def main(stdscr):
    # Setup curses environment
    curses.curs_set(0) # Hide cursor
    stdscr.nodelay(1)  # Non-blocking input
    
    # Initialize colors
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)   # Unshuffled
    curses.init_pair(2, curses.COLOR_CYAN, -1)    # Left shuffled
    curses.init_pair(3, curses.COLOR_MAGENTA, -1) # Right shuffled
    curses.init_pair(4, curses.COLOR_YELLOW, -1)  # Pendulum indicator/Text
    
    max_y, max_x = stdscr.getmaxyx()
    
    # Create an initially sorted array scaled to the terminal height
    # Using max_x so it fills the screen width
    array_size = max_x - 1 
    max_val = max_y - 5 # Leave room at the top
    
    # Generate array with values mapping to terminal height
    arr = [int((i / array_size) * max_val) + 1 for i in range(array_size)]
    
    # Draw initial state
    draw_state(stdscr, arr, 0, len(arr)-1, 0, "INIT")
    time.sleep(9)

    # Run the generator
    for state_arr, left, right, active_idx, status in pendulum_shuffle_gen(arr):
        draw_state(stdscr, state_arr, left, right, active_idx, status)
        
        # Adjust speed based on array size for watchability
        time.sleep(0.02) 
        
        # Allow user to quit early
        if stdscr.getch() == ord('q'):
            break

    # Final hold
    stdscr.addstr(2, 2, " Finished! Press any key to exit. ", curses.color_pair(4) | curses.A_REVERSE)
    stdscr.nodelay(0)
    stdscr.getch()

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
