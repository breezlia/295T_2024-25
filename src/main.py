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

motor_r1 = Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)
motor_r2 = Motor(Ports.PORT2, GearSetting.RATIO_6_1, False)
motor_r3 = Motor(Ports.PORT3, GearSetting.RATIO_6_1, False)
right_drive = MotorGroup(motor_r1, motor_r2, motor_r3)

motor_l1 = Motor(Ports.PORT4, GearSetting.RATIO_6_1, False)
motor_l2 = Motor(Ports.PORT5, GearSetting.RATIO_6_1, False)
motor_l3 = Motor(Ports.PORT6, GearSetting.RATIO_6_1, False)
left_drive = MotorGroup(motor_l1, motor_l2, motor_l3)

right_drive.spin(FORWARD, 50, RPM)

right_drive.stop

drivetrain = (left_drive, right_drive)

myVariable = 0

def when_started1():
    global myVariable
    drivetrain.drive_for(FORWARD, 200, MM)
    wait(7, SECONDS)
    drivetrain.drive_for(REVERSE, 200, MM)
// User Control Mode
def ondriver_drivercontrol_0():
    global myVariable
    while True:
        wait(5, MSEC)
// Controls for R1 & R2
def onevent_controller_1buttonR1_pressed_0():
    global myVariable
    digital_out_a.set(True)

def onevent_controller_1buttonR2_pressed_0():
    global myVariable
    digital_out_a.set(False)
def onevent_controller_1buttonL1_pressed_0()
    




// Autonumous Period
def onauton_autonomous_0():
    global myVariable
    pass

// create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    // Stop the autonomous control tasks
    auton_task_0.stop()

def vexcode_driver_function():
    // Start the driver control tasks
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task_0.stop()


// register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )

// system event handlers
controller_1.buttonR1.pressed(onevent_controller_1buttonR1_pressed_0)
controller_1.buttonR2.pressed(onevent_controller_1buttonR2_pressed_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()



        
