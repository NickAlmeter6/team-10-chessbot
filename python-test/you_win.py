# you_win.py

import time
from your_turn import your_turn, send_command, split_value, ANGLE_MIN, ANGLE_MAX

# Perform "You win" gesture
def you_win():
    # Step 1: Pointing (from your_turn.py)
    your_turn()

    # Step 2: Fist with thumb extended (win gesture)
    exec_time = 500
    low_time, high_time = split_value(exec_time)

    # Build command
    command = [0x55, 0x55, 20, 0x03, 5, low_time, high_time]

    # Fingers 2-5 bent (ring, middle, index, pinky), thumb extended
    for servo_id in [2, 3, 4, 5]:
        command.extend([servo_id, *split_value(ANGLE_MIN)])  # Bent
    command.extend([1, *split_value(ANGLE_MIN)])  # Thumb extended

    send_command(bytes(command))
    time.sleep(1)

def rotate_wrist_loop():
    exec_time = 1000
    low_time, high_time = split_value(exec_time)

    try:
        while True:
            # Left (ANGLE_MIN)
            command = [0x55, 0x55, 8, 0x03, 1, low_time, high_time, 6, *split_value(ANGLE_MIN)]
            send_command(bytes(command))
            time.sleep(1.0)

            # Right (ANGLE_MAX)
            command = [0x55, 0x55, 8, 0x03, 1, low_time, high_time, 6, *split_value(ANGLE_MAX)]
            send_command(bytes(command))
            time.sleep(1.0)

            # Center
            center_angle = (ANGLE_MIN + ANGLE_MAX) // 2
            command = [0x55, 0x55, 8, 0x03, 1, low_time, high_time, 6, *split_value(center_angle)]
            send_command(bytes(command))
            time.sleep(1.0)
            
    except KeyboardInterrupt: 
        print("Rotation stopped by user.")

# Run the gesture
if __name__ == "__main__":
    you_win()
    rotate_wrist_loop()
    