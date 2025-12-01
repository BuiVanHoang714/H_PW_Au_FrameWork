
#!/usr/bin/env python3
"""
Enhanced Auto Click Python Script
================================
This script automatically clicks at a specified position on your screen.
Features include: Space key position capture, delayed position reading,
and multiple ways to capture mouse coordinates.

Author: Claude
Date: March 31, 2025
"""

import pyautogui
import time
import sys
import threading
import tkinter as tk
from tkinter import ttk, messagebox
import keyboard  # For detecting space key

# Prevent mouse from going out of control by adding a safety feature
# Moving the mouse to the upper-left corner will abort the script
pyautogui.FAILSAFE = True

def get_current_mouse_position_with_delay():
    """
    Function to get the current mouse position after a countdown,
    giving user time to position the cursor.
    
    Returns:
    - tuple: (x, y) coordinates of mouse position
    """
    print("\nGet Current Mouse Position")
    print("=========================")
    print("You will have time to position your mouse.")
    
    # Countdown from 5 seconds
    for i in range(5, 0, -1):
        print(f"Reading position in {i} seconds... Move your mouse to the desired position.")
        time.sleep(1)
    
    print("Capturing position NOW!")
    x, y = pyautogui.position()
    print(f"Position captured: X={x}, Y={y}")
    
    return (x, y)

def mouse_position_tracker():
    """
    Function to continuously track and display mouse position.
    Allows user to capture a specific position with Space key or button.
    
    Returns:
    - tuple: (x, y) coordinates of captured mouse position
    """
    # Create a GUI window to display mouse position
    root = tk.Tk()
    root.title("Mouse Position Tracker")
    root.geometry("400x250")
    root.resizable(False, False)
    
    # Variables to store the captured position
    captured_x = tk.IntVar()
    captured_y = tk.IntVar()
    current_x = tk.IntVar()
    current_y = tk.IntVar()
    is_captured = tk.BooleanVar(value=False)
    
    # Function to update position display
    def update_position():
        if not root.winfo_exists():
            return
            
        x, y = pyautogui.position()
        current_x.set(x)
        current_y.set(y)
        position_label.config(text=f"Current position: ({x}, {y})")
        root.after(100, update_position)
    
    # Function to capture current position
    def capture_position():
        x, y = pyautogui.position()
        captured_x.set(x)
        captured_y.set(y)
        captured_label.config(text=f"Captured position: ({x}, {y})")
        is_captured.set(True)
        status_label.config(text="Status: Position captured!", foreground="green")
        
    # Function called when Space key is pressed
    def on_space_pressed(e=None):
        capture_position()
        
    # Function to confirm selection and close window
    def confirm_selection():
        if is_captured.get():
            root.quit()
            root.destroy()
        else:
            status_label.config(text="Status: Please capture a position first!", foreground="red")
    
    # Create GUI elements
    header_label = ttk.Label(root, text="Mouse Position Tracker", font=("Arial", 12, "bold"))
    header_label.pack(pady=10)
    
    position_label = ttk.Label(root, text="Current position: (0, 0)")
    position_label.pack(pady=5)
    
    instruction_label = ttk.Label(root, text="Move mouse to desired position and press SPACE or click the button below")
    instruction_label.pack(pady=5)
    
    capture_button = ttk.Button(root, text="Capture Current Position", command=capture_position)
    capture_button.pack(pady=5)
    
    captured_label = ttk.Label(root, text="Captured position: (None, None)")
    captured_label.pack(pady=5)
    
    status_label = ttk.Label(root, text="Status: Waiting for position capture...", foreground="blue")
    status_label.pack(pady=5)
    
    confirm_button = ttk.Button(root, text="Confirm Selection", command=confirm_selection)
    confirm_button.pack(pady=10)
    
    # Bind space key for capturing position
    root.bind("<space>", on_space_pressed)
    
    # Register keyboard hook for capturing space key even when window is not focused
    keyboard.on_press_key("space", lambda _: on_space_pressed())
    
    # Start updating position
    update_position()
    
    # Start the main loop
    root.mainloop()
    
    # Unregister keyboard hook
    keyboard.unhook_all()
    
    # Return the captured position
    return (captured_x.get(), captured_y.get())

def auto_click(x_coord, y_coord, click_count=1, delay=1.0):
    """
    Function to automatically click at a specific point on the screen
    
    Parameters:
    - x_coord (int): X coordinate for mouse position
    - y_coord (int): Y coordinate for mouse position
    - click_count (int): Number of clicks to perform
    - delay (float): Delay between clicks in seconds
    """
    # Display configuration information
    print(f"Auto Click Python Script")
    print(f"======================")
    print(f"Target position: X={x_coord}, Y={y_coord}")
    print(f"Number of clicks: {click_count}")
    print(f"Delay between clicks: {delay} seconds")
    print()
    
    # Get screen resolution to validate coordinates
    screen_width, screen_height = pyautogui.size()
    
    # Validate that the coordinates are within screen boundaries
    if x_coord < 0 or x_coord > screen_width or y_coord < 0 or y_coord > screen_height:
        print(f"Error: Coordinates ({x_coord}, {y_coord}) are outside screen boundaries ({screen_width}x{screen_height}).")
        return False
    
    # Give the user time to prepare
    print("Starting in 3 seconds...")
    print("Move mouse to upper-left corner to abort.")
    time.sleep(3)
    
    # Perform the clicks
    print("Starting click operation...")
    
    for i in range(click_count):
        # Move to the position
        pyautogui.moveTo(x_coord, y_coord, duration=0.2)
        
        # Perform the click
        pyautogui.click()
        
        # Show progress
        print(f"Click {i+1}/{click_count} completed")
        
        # Wait before the next click if needed
        if i < click_count - 1:
            time.sleep(delay)
    
    print("\nClick operation completed successfully!")
    return True

def print_menu():
    """
    Display the main menu of the application
    """
    print("\nAuto Click Tool Menu")
    print("===================")
    print("1. Get current mouse position (with 5-second delay)")
    print("2. Track and capture mouse position (press SPACE to capture)")
    print("3. Start auto-clicking with specified coordinates")
    print("4. Start auto-clicking with captured coordinates")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    return choice

if __name__ == "__main__":
    # Default values
    DEFAULT_X = 500
    DEFAULT_Y = 300
    DEFAULT_CLICKS = 1
    DEFAULT_DELAY = 1.0
    
    # Variables to store captured position
    captured_x = None
    captured_y = None
    
    try:
        # Check if command line arguments were provided
        if len(sys.argv) >= 3:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            
            if len(sys.argv) >= 4:
                clicks = int(sys.argv[3])
            else:
                clicks = DEFAULT_CLICKS
                
            if len(sys.argv) >= 5:
                delay = float(sys.argv[4])
            else:
                delay = DEFAULT_DELAY
            
            # Run the auto click function directly
            auto_click(x, y, clicks, delay)
        else:
            # Interactive menu mode
            while True:
                choice = print_menu()
                
                if choice == '1':
                    print("\nYou have selected to get current mouse position with delay.")
                    print("Please prepare to move your mouse to the desired position.")
                    x, y = get_current_mouse_position_with_delay()
                    captured_x, captured_y = x, y
                    print(f"\nPosition confirmed: X={x}, Y={y}")
                    print("This position has been saved and can be used with option 4.")
                    input("\nPress Enter to return to the menu...")
                
                elif choice == '2':
                    print("Opening mouse position tracker...")
                    print("Move your mouse to the desired position and press SPACE to capture it.")
                    print("You can also use the button in the window.")
                    x, y = mouse_position_tracker()
                    captured_x, captured_y = x, y
                    print(f"Position captured: X={x}, Y={y}")
                    
                elif choice == '3':
                    try:
                        x = int(input("Enter X coordinate: "))
                        y = int(input("Enter Y coordinate: "))
                        clicks = int(input("Enter number of clicks (default=1): ") or "1")
                        delay = float(input("Enter delay between clicks in seconds (default=1.0): ") or "1.0")
                        auto_click(x, y, clicks, delay)
                    except ValueError:
                        print("Error: Please enter valid numbers.")
                
                elif choice == '4':
                    if captured_x is not None and captured_y is not None:
                        print(f"Using captured position: X={captured_x}, Y={captured_y}")
                        clicks = int(input("Enter number of clicks (default=1): ") or "1")
                        delay = float(input("Enter delay between clicks in seconds (default=1.0): ") or "1.0")
                        auto_click(captured_x, captured_y, clicks, delay)
                    else:
                        print("Error: No position has been captured yet. Please use option 1 or 2 first.")
                
                elif choice == '5':
                    print("Exiting the program. Goodbye!")
                    break
                
                else:
                    print("Invalid choice. Please try again.")
        
    except ValueError:
        print("Error: Please provide valid numbers for coordinates, click count, and delay.")
        print("Usage: python auto_click.py [x_coord] [y_coord] [click_count] [delay_in_seconds]")
    except KeyboardInterrupt:
        print("\nOperation aborted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")