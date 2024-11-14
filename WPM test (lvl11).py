# WPM test. This one was a struggle. Between not knowing what curses is and how to use it and backspace giving me way too much pain, this took longer than a project of this difficulty should have.
# I watched the beginning of Tech with Tim's section on this as he displays how curses works before building the test, which I did myself.

import curses, time, os
from curses import wrapper


def WPM(start, chars):
    return round((chars / 5) * (60 / (time.time() - start))) if (time.time() - start) > 0 else 0


def main(stdscr):
    
    # Initialize the text to type and typed text variables
    original = "This is a sentence that you need to type out as quickly as possible."
    typed_text = []
    cursor_pos = 0  # Position of the cursor in the typed text

    # Initialize color pairs
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Default text
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Correctly typed text
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)    # Incorrectly typed text

    stdscr.clear()

    while True:

        if len(typed_text) <= 1:
            start = time.time()

        # Redraw the original text each loop to ensure it stays visible
        stdscr.addstr(0, 0, original, curses.color_pair(1))

        # Display the typed text with colors for correctness
        for i, char in enumerate(typed_text):
            if i < len(original) and char == original[i]:
                stdscr.addstr(0, i, char, curses.color_pair(2))  # Correct character
            elif i < len(original):
                stdscr.addstr(0, i, char, curses.color_pair(3))  # Incorrect character
            else:
                stdscr.addstr(0, i, char, curses.color_pair(3))  # Extra characters (if any)


        # Set cursor position
        stdscr.move(1, cursor_pos)

        correct = 0
        for i in range(0, len(typed_text)-1):
            if typed_text[i] == original[i]:
                correct += 1

        wpm = WPM(start, correct)

        # WPM section
        stdscr.addstr(1, 0, f"WPM: {wpm}", curses.color_pair(1))

        # Refresh screen
        stdscr.refresh()

        # Get user key input
        key = stdscr.getch()
        if key in (curses.KEY_BACKSPACE, 127, 8):  # Handle backspace
            if cursor_pos > 0:
                cursor_pos -= 1
                typed_text.pop(cursor_pos)
        elif key == curses.KEY_LEFT:  # Move cursor left
            if cursor_pos > 0:
                cursor_pos -= 1
        elif key == curses.KEY_RIGHT:  # Move cursor right
            if cursor_pos < len(typed_text):
                cursor_pos += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:  # Enter key
            break
        elif 32 <= key <= 126 and len(typed_text) < len(original):  # Printable characters within limit
            typed_text.insert(cursor_pos, chr(key))
            cursor_pos += 1

        # Check if typed text matches the original and is complete
        if "".join(typed_text) == original:
            os.system('cls')
            stdscr.addstr(2, 0, f"Congratulations! You've completed the sentence with a WPM of {wpm}!", curses.color_pair(2))
            stdscr.refresh()
            stdscr.getch()
            break

wrapper(main)
