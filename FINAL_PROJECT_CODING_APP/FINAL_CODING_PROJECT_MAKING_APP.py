import time

def stopwatch():
    print("Simple Terminal Stopwatch")
    print("Commands:")
    print("  [s] Start")
    print("  [p] Pause")
    print("  [r] Resume")
    print("  [q] Quit")

    running = False
    start_time = 0
    elapsed_time = 0.0

    while True:
        command = input("Enter command (s/p/r/q): ").strip().lower()

        if command == 's':
            if not running:
                elapsed_time = 0.0  # Reset elapsed time on start
                start_time = time.time()
                running = True**
                print("Stopwatch started.")
            else:
                print("Stopwatch is already running.")

        elif command == 'p':
            if running:
                elapsed_time += time.time() - start_time
                running = False
                print(f"Paused at {format_time(elapsed_time)}.")
            else:
                print("Stopwatch is not running.")

        elif command == 'r':
            if not running and elapsed_time > 0:
                start_time = time.time()
                running = True
                print("Resumed.")
            elif running:
                print("Stopwatch is already running.")
            else:
                print("Stopwatch has not been started yet. Use 's' to start.")

        elif command == 'q':
            if running:
                elapsed_time += time.time() - start_time
                running = False
            print(f"Final Time: {format_time(elapsed_time)}.")
            break

        else:
            print("Invalid command. Use s (start), p (pause), r (resume), q (quit).")

def format_time(seconds):
    millis = int((seconds - int(seconds)) * 100)
    mins, secs = divmod(int(seconds), 60)
    hrs, mins = divmod(mins, 60)
    return f"{hrs:02d}:{mins:02d}:{secs:02d}.{millis:02d}"

if __name__ == "__main__":
    stopwatch()
