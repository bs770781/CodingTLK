import time
import threading

# Converts seconds into HH:MM:SS.ms format
def format_time(seconds):
    millis = int((seconds - int(seconds)) * 100)
    mins, secs = divmod(int(seconds), 60)
    hrs, mins = divmod(mins, 60)
    return f"{hrs:02d}:{mins:02d}:{secs:02d}.{millis:02d}"

def stopwatch():
    # Display initial instructions
    print("Simple Terminal Stopwatch")
    print("Commands:")
    print("  [s] Start")    # Start the stopwatch from zero
    print("  [p] Pause")    # Pause the stopwatch and keep elapsed time
    print("  [r] Resume")   # Resume the stopwatch from paused time
    print("  [q] Quit")     # Quit and display the final elapsed time

    # Initialize stopwatch states
    running = False         # Indicates whether the stopwatch is currently running
    start_time = 0          # Time when the stopwatch was last started
    elapsed_time = 0.0      # Total elapsed time (excluding current session when running)
    stop_display = False    # Controls display thread termination

    # This function runs in a separate thread and updates the time display
    def display_time():
        while not stop_display:
            if running:
                # Compute elapsed time while running
                current_time = elapsed_time + (time.time() - start_time)
                print(f"\rElapsed Time: {format_time(current_time)}", end="")
            time.sleep(0.1)

    # Start the display thread
    display_thread = threading.Thread(target=display_time)
    display_thread.daemon = True
    display_thread.start()

    # Main loop for user input
    while True:
        command = input("\nEnter command (s/p/r/q): ").strip().lower()

        if command == 's':
            # Start command: resets and starts the stopwatch
            if not running:
                elapsed_time = 0.0              # Reset elapsed time
                start_time = time.time()        # Record start time
                running = True
                print("Stopwatch started.")
            else:
                print("Stopwatch is already running.")

        elif command == 'p':
            # Pause command: pauses the stopwatch
            if running:
                elapsed_time += time.time() - start_time  # Add current session to elapsed time
                running = False
                print(f"\nPaused at {format_time(elapsed_time)}.")
            else:
                print("Stopwatch is not running.")

        elif command == 'r':
            # Resume command: resumes the stopwatch from pause
            if not running and elapsed_time > 0:
                start_time = time.time()        # Record new start time
                running = True
                print("Resumed.")
            elif running:
                print("Stopwatch is already running.")
            else:
                print("Stopwatch has not been started yet. Use 's' to start.")

        elif command == 'q':
            # Quit command: stops everything and shows the final time
            if running:
                elapsed_time += time.time() - start_time  # Update final time
                running = False
            stop_display = True                # Signal display thread to stop
            time.sleep(0.2)                    # Allow thread to cleanly exit
            print(f"\nFinal Time: {format_time(elapsed_time)}.")
            break

        else:
            # Handle invalid input
            print("Invalid command. Use s (start), p (pause), r (resume), q (quit).")

# Run the stopwatch if this file is executed directly
if __name__ == "__main__":
    stopwatch()
