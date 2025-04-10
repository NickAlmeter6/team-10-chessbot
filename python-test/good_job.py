import serial
import time
print("qwertyuiop")
# Serial configuration
SERIAL_PORT = 'COM5'
BAUD_RATE = 9600
TIMEOUT = 1  # Read timeout in seconds

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

# Perform "Good job" gesture
def good_job():
    exec_time = 500
    low_time, high_time = split_value(exec_time)

    # Step 1: Fist (all fingers bent)
    command = [0x55, 0x55, 20, 0x03, 5, low_time, high_time]
    for servo_id in [1,2,3,4,5]:
        command.extend([servo_id, *split_value(ANGLE_MIN)]) 
    send_command(bytes(command))
   

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
good_job()
rotate_wrist()