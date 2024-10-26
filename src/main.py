# ---------------------------------------------------------------------------- #
#                                                                              #
#   Module:       main.py                                                      #
#   Author:       saanviboyilla                                                #
#   Created:      10/20/2024, 5:14:58 PM                                       #
#   Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

brain.screen.print("Hello V5")

#right drive
motor_r1 = Motor(Ports.PORT4, GearSetting.RATIO_6_1, True)
motor_r2 = Motor(Ports.PORT5, GearSetting.RATIO_6_1, True)
motor_r3 = Motor(Ports.PORT6, GearSetting.RATIO_6_1, True)
right_drive = MotorGroup(motor_r1, motor_r2, motor_r3)
#left drive
motor_l1 = Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)
motor_l2 = Motor(Ports.PORT2, GearSetting.RATIO_6_1, False)
motor_l3 = Motor(Ports.PORT3, GearSetting.RATIO_6_1, False)
left_drive = MotorGroup(motor_l1, motor_l2, motor_l3)
#intake
motor_intake = Motor(Ports.PORT11,GearSetting.RATIO_6_1, True)
#clamp
digout_clamp = DigitalOut(brain.three_wire_port.a)
#drivetrain
drivetrain = DriveTrain(left_drive, right_drive)
drivetrain.set_drive_velocity(100, PERCENT)
drivetrain.set_turn_velocity(100, PERCENT)
#controller
controller = Controller()

def pre_auntonomus():
# actions to do when program starts
    brain.screen.clear_screen() 
    brain.screen.print ("pre auton code")
    wait(1,SECONDS)
    motor_l1.spin(FORWARD)
    motor_l2.spin(FORWARD)
    motor_l3.spin(FORWARD)
    motor_r1.spin(FORWARD)
    motor_r2.spin(FORWARD)
    motor_r3.spin(FORWARD)
    drivetrain.stop()

def autonomonus():
    brain.screen.clear_screen()
    brain.screen.print("autonomus code")
    # place auntomonus code here

def user_control():
    brain.screen.clear_screen()
    # place driver control code here
    while True:
        drive_control()
        wait(20, MSEC)

def drive_control():
# Forward
    if (controller.axis3.position() > 30): 
        left_velocity = controller.axis3.position()
        right_velocity = controller.axis3.position()
        if (controller.axis1.position() > 30):
        # veer right
            right_velocity = right_velocity - controller.axis1.position()
        elif (controller.axis1.position() < -30):
            # veer left
            left_velocity = left_velocity + controller.axis1.position()
        right_drive.spin(REVERSE, right_velocity, PERCENT)
        left_drive.spin(REVERSE, left_velocity, PERCENT)
# Reverse
    elif (controller.axis3.position() < -30):  
        left_velocity = controller.axis3.position()
        right_velocity = controller.axis3.position()
        if (controller.axis1.position() < -30):
        # veer right
            right_velocity = right_velocity - controller.axis1.position()
        elif (controller.axis1.position() > 30):
            # veer left
            left_velocity = left_velocity + controller.axis1.position()
        right_drive.spin(REVERSE, right_velocity, PERCENT)
        left_drive.spin(REVERSE, left_velocity, PERCENT) 
# Left Turn
    elif (controller.axis1.position() > 30): 
       drivetrain.turn(LEFT, 25, PERCENT)
# Right Turn
    elif (controller.axis1.position() < -30): 
        drivetrain.turn(RIGHT, 25, PERCENT)
    else:
        drivetrain.stop()
#intake
    if(controller.buttonR1.pressing()):
        motor_intake.spin(REVERSE,100,PERCENT)
    elif(controller.buttonR2.pressing()):
        motor_intake.spin(FORWARD,100,PERCENT)
    else:
        motor_intake.stop()
    #clamp
    if(controller.buttonL1.pressing()):
        digout_clamp.set(True)
    elif(controller.buttonL2.pressing()):
        digout_clamp.set(False)





# create competition instance
comp = Competition(user_control, autonomonus)
pre_auntonomus()