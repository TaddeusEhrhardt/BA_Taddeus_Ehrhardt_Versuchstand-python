import time
import os
import random
import string
import gphoto2 as gp
import gphoto2_functions as gpf
from dynamixel_functions import *


class RUN:
    def __init__(self, root):
        # Console Inputs
        self.name = input('Run name: ')
        self.max_angle = float(input('MAX angle: (float) '))
        self.steps = int(input('Steps: (int) '))
        self.root = root
        self.dir = os.path.join(self.root, self.name)
        self.zero_position = 0

        try:
            print("Making folder: " + self.dir)
            os.mkdir(self.dir)
        except:
            print('Failed to create the new directory.')

        print('New Run: ' + self.name)
        print('Image directory: ', self.dir)

    def set_zero_position(self, position):
        self.zero_position = position

    def set_max_angle(self, angle):
        self.max_angle = angle

    def position_from_angle(self, angle):
        position = angle / 360 * 4095 + run.zero_position
        return position

    def set_steps(self, steps):
        self.steps = steps


def generate_random_name(size) -> str:
    filename = ''.join(random.choice(string.ascii_letters) for i in range(size))
    return filename


IMAGE_TARGET = "/home/taddeus/BA_Bilder/"
run = RUN(IMAGE_TARGET)

# Dynamixel Init
init_port()

set_vel_pos_pid(500, 200, 1000, 2000, 0)
set_profile_vel(1000)
# Camera init

# eos_6d = gp.Camera()

# camera_controller = gpf.CustomCamera()
# camera_controller.init_camera(eos_6d)



disable_torque()

# Wait for manual alignment
print('Press enter to commit current position as start.', end='')
input()
# run.set_zero_position(int(input()))
run.set_zero_position(get_dxl_position())
print('Start Position: ', run.zero_position)
enable_torque()
print("Steps: " + str(run.steps))

position = [run.zero_position, run.position_from_angle(run.max_angle)]

for i in range(100):
    print('Position', position[i % 2])
    go_to_position(int(position[i % 2]))
    # camera_controller.capture_and_download_image(eos_6d, os.path.join(run.dir, run.name + '_' + '%07.3f' % current_angle))
    # time.sleep(0.3)
#
disable_torque()
exit(close_port())
