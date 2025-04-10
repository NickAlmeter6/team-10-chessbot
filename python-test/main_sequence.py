import multiprocessing
import time
import importlib
import sys

# Motions in desired order
motions = [
    "start",
    "your_turn",
    "Thinking",     # Infinite loop
    "plain_move",
    "good_job",
    "big_plunge",
    "you_win",
    "I_win"         # Infinite loop (wrist rotate)
]

# Timeout settings
FIXED_DURATION = 10              # Run each motion for exactly 5 seconds
INFINITE_LOOP_TIMEOUT = 12       # Slightly longer for infinite loops

# Files known to have infinite loops
infinite_loop_files = {"Thinking.py", "I_win.py", "you_win.py"}

def run_module(name):
    try:
        mod = importlib.import_module(name)
        if hasattr(mod, 'main'):
            mod.main()
        else:
            print(f"Module '{name}' has no main() function.")
    except Exception as e:
        print(f"Error running {name}: {e}")

def run_with_timeout(name, timeout):
    process = multiprocessing.Process(target=run_module, args=(name,))
    process.start()
    process.join(timeout)

    if process.is_alive():
        print(f"Timeout reached. Terminating '{name}'...")
        process.terminate()
        process.join()
    else:
        print(f"'{name}' completed.")

def main():
    print("Starting compound motion sequence...\n")

    for motion in motions:
        print(f"\n--- Executing: {motion} ---")
        timeout = INFINITE_LOOP_TIMEOUT if motion in infinite_loop_files else FIXED_DURATION
        run_with_timeout(motion, timeout=timeout)

    print("\nAll motions executed!")

if __name__ == "__main__":
    main()
