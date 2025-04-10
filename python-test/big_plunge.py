import serial
import time

# Serial configuration
SERIAL_PORT = 'COM5'
BAUD_RATE = 9600
TIMEOUT = 1

# Servo IDs
FINGER_IDS = [1, 2, 3, 4, 5]  # 1: thumb, 2: index, 3: middle, 4: ring, 5: pinky

# Angle range
ANGLE_MIN = 900   # Fully bent
ANGLE_MAX = 2000  # Fully extended

# Split integer into two bytes
def split_value(val):
    return val & 0xFF, (val >> 8) & 0xFF

# Send data to servo
def send_command(data):
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=TIMEOUT) as ser:
            print(f"Sending: {data.hex(' ').upper()}")
            ser.write(data)
            time.sleep(0.1)
            response = ser.read_all()
            if response:
                print(f"Response: {response.hex(' ').upper()}")
            else:
                print("No response")
    except Exception as e:
        print(f"Serial error: {e}")

# Perform "Big Plunge" gesture
def big_plunge():
    exec_time = 500
    low_time, high_time = split_value(exec_time)

    # Step 1: Fist - all fingers bent
    command = [0x55, 0x55, 20, 0x03, 5, low_time, high_time]
    for servo_id in [2,3,4,5]:
        command.extend([servo_id, *split_value(ANGLE_MIN)])
    command.extend([1, *split_value(ANGLE_MAX)])
    send_command(bytes(command))
    time.sleep(0.8)

    # Step 2: Extend pinky (servo ID 5)
    command = [0x55, 0x55, 8, 0x03, 1, low_time, high_time, 5, *split_value(ANGLE_MAX)]
    send_command(bytes(command))
    time.sleep(1)


def rotate_wrist():
    exec_time = 1000  # Increase execution time for better response
    low_time, high_time = split_value(exec_time)

    # Move wrist to one extreme first
    command = [0x55, 0x55, 8, 0x03, 1, low_time, high_time, 6, *split_value(ANGLE_MIN)]
    send_command(bytes(command))
    time.sleep(1.0)

    # Then move to the opposite extreme
    command = [0x55, 0x55, 8, 0x03, 1, low_time, high_time, 6, *split_value(ANGLE_MAX)]
    send_command(bytes(command))
    time.sleep(1.0)

# Run gesture
big_plunge()
rotate_wrist()
