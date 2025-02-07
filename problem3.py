#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_10 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
motor_11 = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
motor_12 = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)
motor_20 = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
motor_19 = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
#   Project:      VEXcode Project
#   Author:       VEX
#   Created:
#   Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_10 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
motor_11 = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
motor_20 = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random


# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
#   Project:      VEXcode Project
#   Author:       VEX
#   Created:
#   Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
def forward (dis):
 motor_1.set_velocity(50, PERCENT)
 motor_10.set_velocity(50, PERCENT)
 motor_11.set_velocity(50, PERCENT)
 motor_20.set_velocity(50, PERCENT)
 motor_1.spin(REVERSE)
 motor_10.spin(FORWARD)
 motor_11.spin(REVERSE)
 motor_20.spin(FORWARD)
 wait(0.3,SECONDS)
 motor_1.set_velocity(50, PERCENT)
 motor_10.set_velocity(50, PERCENT)
 motor_11.set_velocity(50, PERCENT)
 motor_20.set_velocity(50, PERCENT)
 motor_1.spin(REVERSE)
 motor_10.spin(FORWARD)
 motor_11.spin(REVERSE)
 motor_20.spin(FORWARD)
 wait(dis,SECONDS)
 motor_1.stop()
 motor_10.stop()
 motor_11.stop()
 motor_20.stop()
def right (right):
 motor_1.set_velocity(50, PERCENT)
 motor_10.set_velocity(50, PERCENT)
 motor_11.set_velocity(50, PERCENT)
 motor_20.set_velocity(50, PERCENT)
 motor_1.spin_for(FORWARD, right, DEGREES,wait=False)
 motor_10.spin_for(FORWARD, right, DEGREES,wait=False)
 motor_11.spin_for(FORWARD, right, DEGREES,wait=False)
 motor_20.spin_for(FORWARD, right, DEGREES, wait=False)
 
motor_12.set_velocity(100, PERCENT)           
motor_19.spin_for(FORWARD, 50, DEGREES)
wait(1,SECONDS)
motor_12.spin(FORWARD)
wait(1,SECONDS)
forward(0.09)
wait(1,SECONDS)
motor_12.spin(REVERSE)
wait(1,SECONDS)
motor_19.spin_for(FORWARD, 120, DEGREES)
wait(1,SECONDS)
right(145)
wait(3,SECONDS)
forward(0.1 )
wait(1,SECONDS)
motor_19.set_velocity(75, PERCENT)
motor_19.spin_for(REVERSE, 120, DEGREES)
wait(1,SECONDS)
motor_12.spin(FORWARD)
wait(1.5,SECONDS)
motor_1.spin(FORWARD)
motor_10.spin(REVERSE)
motor_11.spin(FORWARD)
motor_20.spin(REVERSE)
wait(0.8,SECONDS)
motor_1.stop()
motor_10.stop()
motor_11.stop()
motor_20.stop()
wait(1,SECONDS)
motor_19.spin_for(FORWARD, 100, DEGREES)
