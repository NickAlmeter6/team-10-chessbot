import serial
import time
import math

# Serial port configuration
SERIAL_PORT = 'COM5'
BAUD_RATE = 9600
TIMEOUT = 1  # Read timeout in seconds

# List of servo IDs (assuming there are 5 servos)
SERVO_IDS = [1, 2, 3, 4, 5]

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

# Function to generate wave motion; each servo moves following a sine curve
def wave_motion():
    # Parameters: 'steps' steps per cycle, 'delay' seconds delay per step
    steps = 20         # Divide one cycle into 20 steps
    delay = 0.15       # Delay per step (approx. 30% faster than 0.2 sec)
    mid = (ANGLE_MIN + ANGLE_MAX) / 2       # Midpoint value, e.g., (900+2000)/2 = 1450
    amplitude = (ANGLE_MAX - ANGLE_MIN) / 2   # Amplitude, e.g., (2000-900)/2 = 550

    # Execution time in milliseconds; here set to 500ms (adjust as needed)
    exec_time = 500
    low_time, high_time = split_value(exec_time)

    i = 0  # Initialize step counter
    while True:
        command = [0x55, 0x55]
        # Data length = (number of servos * 3) + 5 (bytes after the header)
        data_length = len(SERVO_IDS) * 3 + 5
        command.append(data_length)
        command.append(0x03)              # Command value: CMD_MULT_SERVO_MOVE (3)
        command.append(len(SERVO_IDS))     # Number of servos to control
        command.append(low_time)           # Execution time low byte
        command.append(high_time)          # Execution time high byte

        # Calculate the current angle for each servo based on a sine wave
        for j, servo_id in enumerate(SERVO_IDS):
            # Add a phase shift for each servo to enhance the wave effect
            phase = 2 * math.pi * (i / steps) + j * (2 * math.pi / len(SERVO_IDS))
            angle = int(mid + amplitude * math.sin(phase))
            # Split the calculated angle into low and high bytes
            low_angle, high_angle = split_value(angle)
            command.extend([servo_id, low_angle, high_angle])

        # Send the command data
        send_command(bytes(command))
        time.sleep(delay)
        i += 1

# Execute the wave motion in an infinite loop
wave_motion()
