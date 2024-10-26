# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Saanvi Boyilla                                               #
# 	Created:      8/25/2024, 7:43:49 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

brain.screen.print("Hello V5")

motor_r1 = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)
motor_r2 = Motor(Ports.PORT2, GearSetting.RATIO_6_1, True)
motor_r3 = Motor(Ports.PORT3, GearSetting.RATIO_6_1, True)
right_drive = MotorGroup(motor_r1, motor_r2, motor_r3)

motor_intake = Motor(Ports. PORT7, GearSetting. Ratio_6_1, False))

motor_l1 = Motor(Ports.PORT4, GearSetting.RATIO_6_1, False)
motor_l2 = Motor(Ports.PORT5, GearSetting.RATIO_6_1, False)
motor_l3 = Motor(Ports.PORT6, GearSetting.RATIO_6_1, False)
left_drive = MotorGroup(motor_l1, motor_l2, motor_l3)

drivetrain = (left_drive, right_drive)


def pre_auntonomus():
# actions to do when program starts
brain.screen.clear_screen()
brain.screen.print ("pre auton code")
wait(1,SECONDS)
Motor_l1.spin(FORWARD)
Motor_l2.spin(FORWARD)
Motor_l3.spin(FORWARD)
Motor_r1.spin(FORWARD)
Motor_r2.spin(FORWARD)
Motor_r3.spin(FORWARD)


def autonomonus():
    brain.screen.clear_screen()
    brain.screen.print("autonomus code")
    # place auntomonus code here

def user_control():
    brain.screen.clear_screen()
    # place driver control code here
    while True:
        wait(20, MSEC)
        def drive_control():
    if (controller.axis2.position() > 30):
        drivetrain.drive(FORWARD, controller.axis2.position())
    elif (controller.axis2.position() < -30):
        drivetrain.drive(REVERSE,-controller.axis2.position())
    else:
        drivetrain.stop()


# create competition instance
comp = Competition(user_control, autonomus)
pre_autonomus()
