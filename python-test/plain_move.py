import serial
import time

# Serial configuration
SERIAL_PORT = 'COM5'
BAUD_RATE = 9600
TIMEOUT = 1

# Servo ID 分配
# 1: Thumb, 2: Ring, 3: Middle, 4: Index, 5: Pinky
FINGER_IDS = [1, 2, 3, 4, 5]

# 角度定义
ANGLE_MIN = 900   # 向外（握拳）
ANGLE_MAX = 2000  # 向内（伸展）

# 拆分数值为两个字节
def split_value(val):
    return val & 0xFF, (val >> 8) & 0xFF

# 发送指令
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

# plain move 动作
def plain_move():
    exec_time = 500
    low_time, high_time = split_value(exec_time)

    # Step 1: fist
    command = [0x55, 0x55, 20, 0x03, 5, low_time, high_time]
    for servo_id in [2,3,4,5]:
        command.extend([servo_id, *split_value(ANGLE_MIN)])
    command.extend([1, *split_value(ANGLE_MAX)])
    send_command(bytes(command))
    time.sleep(0.6)

    # Step 2: strech thumb（1）、middle finger（3）、small finger（5）
    command = [0x55, 0x55, 20, 0x03, 5, low_time, high_time]
    for servo_id in [3,5]:
        command.extend([servo_id, *split_value(ANGLE_MAX)])
    command.extend([1, *split_value(ANGLE_MIN)])
    for servo_id in [2, 4]:
        command.extend([servo_id, *split_value(ANGLE_MIN)])
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


plain_move()
rotate_wrist()
