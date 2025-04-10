import serial
import time
import math

# Serial port configuration
SERIAL_PORT = 'COM5'
BAUD_RATE = 9600
TIMEOUT = 1  # Read timeout in seconds

# List of servo IDs (including the new wrist servo ID 6)
SERVO_IDS = [1, 2, 3, 4, 5, 6]  # Fingers + wrist

# Angle range: minimum 900, maximum 2000
ANGLE_MIN = 900
ANGLE_MAX = 2000

# Function to split an integer into low 8 bits and high 8 bits
def split_value(val):
    return val & 0xFF, (val >> 8) & 0xFF

# Function to send data to the serial port
def send_command(data):
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=TIMEOUT) as ser:
            if not ser.is_open:
                raise Exception(f"Unable to open serial port {SERIAL_PORT}")

            print(f"Sending data: {data.hex(' ').upper()}")
            ser.write(data)

            # Wait for device response
            time.sleep(0.1)
            response = ser.read_all()
            if response:
                print(f"Received response: {response.hex(' ').upper()}")
            else:
                print("No response received")
    except serial.SerialException as e:
        print(f"Serial port error: {e}")
    except Exception as e:
        print(f"Error occurred: {e}")


# Function to extend all fingers (servo IDs 1-5)
def extend_fingers():
    exec_time = 500  # Execution time in ms
    low_time, high_time = split_value(exec_time)
    command = [0x55, 0x55, 20, 0x03, 5, low_time, high_time]
    
    for servo_id in [1, 2, 3, 4, 5]:
        low_angle, high_angle = split_value(ANGLE_MAX)  # Extend fingers fully
        command.extend([servo_id, low_angle, high_angle])
    
    send_command(bytes(command))
    time.sleep(0.5)

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

# Function for countdown gesture
def countdown():
    exec_time = 500
    low_time, high_time = split_value(exec_time)
    
    command = [0x55, 0x55, 8, 0x03, 1, low_time, high_time, 5, *split_value(ANGLE_MAX)]
    send_command(bytes(command))
    time.sleep(0.5)
    
    
    # "3" - Bend pinky (1) and thumb (5), others extended
    command = [0x55, 0x55, 20, 0x03, 5, low_time, high_time]
    
    command.extend([5, *split_value(ANGLE_MIN)])  # Bent
    for servo_id in [1, 2, 3, 4]:
        command.extend([servo_id, *split_value(ANGLE_MAX)])  # Extended
    send_command(bytes(command))
    time.sleep(1)
    
    # "2" - Extend index (2) and middle finger (3)
    command = [0x55, 0x55, 20, 0x03, 5, low_time, high_time]
    for servo_id in [1,2, 3]:
        command.extend([servo_id, *split_value(ANGLE_MAX)])  # Extended
    for servo_id in [ 4, 5]:
        command.extend([servo_id, *split_value(ANGLE_MIN)])  # Bent
    send_command(bytes(command))
    time.sleep(1)
    
    # "1" - Extend only index finger (2)
    command = [0x55, 0x55, 20, 0x03, 5, low_time, high_time]
    command.extend([2, *split_value(ANGLE_MAX)])  # Extended
    command.extend([1, *split_value(ANGLE_MAX)])  # Extended
    for servo_id in [3, 4, 5]:
        command.extend([servo_id, *split_value(ANGLE_MIN)])  # Bent
    send_command(bytes(command))
    time.sleep(1)
    
    # Fist - All fingers bent
    command = [0x55, 0x55, 20, 0x03, 5, low_time, high_time]
    for servo_id in [2, 3, 4, 5]:
        command.extend([servo_id, *split_value(ANGLE_MIN)])  # Bent
    command.extend([1, *split_value(ANGLE_MAX)])  # Extended
    send_command(bytes(command))
    time.sleep(1)

# Function for "Your turn" gesture
def your_turn():
    exec_time = 500
    low_time, high_time = split_value(exec_time)
    command = [0x55, 0x55, 20, 0x03, 5, low_time, high_time]

    for servo_id in [3, 4, 5]:
        command.extend([servo_id, *split_value(ANGLE_MIN)])  # Bent
    command.extend([2, *split_value((ANGLE_MIN + ANGLE_MAX) // 2)])  # Slightly bent index finger
    command.extend([1, *split_value(ANGLE_MAX)])

    send_command(bytes(command))
    time.sleep(1)

# Function to extend all fingers (servo IDs 1-5)
def extend_fingers():
    exec_time = 500  # Execution time in ms
    low_time, high_time = split_value(exec_time)
    command = [0x55, 0x55, 20, 0x03, 5, low_time, high_time]
    
    for servo_id in [1, 2, 3, 4, 5]:
        low_angle, high_angle = split_value(ANGLE_MAX)  # Extend fingers fully
        command.extend([servo_id, low_angle, high_angle])
    
    send_command(bytes(command))
    time.sleep(0.5)

# Execute the sequence
rotate_wrist()
extend_fingers()
countdown()
your_turn()
print("Start gesture completed!")