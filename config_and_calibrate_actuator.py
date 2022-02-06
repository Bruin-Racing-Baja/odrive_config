#ODrive setup script for the actuator motors I think (not cooling)
#Not tested yet. Need to figure out how to get "import odrive" to work on my computer

import odrive
import odrive.enums
import sys

#Command-line argument
axis_num = sys.argv[1]

CURR_LIM = 10 #Amps
VEL_LIM = 20 #Volts
CALIB_CURR = 10 #Amps
ENABLE_BRAKE_RES = True
BRAKE_RES = 0.4699999988079071 # where did that come from?
DC_MAX_NEG_CURR = -0.01  #-10 mA by default
POLE_PAIRS = 7 #the number of magnet poles in the rotor, divided by two
TORQUE_CONSTANT = 8.27/140 #the ratio of torque produced by the motor per Amp of current delivered to the motor. This should be set to 8.27 / (motor KV).
ENCODER_CPR = 42 #the encoder count per revolution [CPR] value

#Tuning constants
VEL_GAIN = 0.07
VEL_INT_GAIN = 3

##############################################################################################

odrv0 = odrive.find_any()
axis0 = odrv0.axis0
axis1 = odrv0.axis1

odrv0.config.enable_brake_resistor = ENABLE_BRAKE_RES
odrv0.config.brake_resistance = BRAKE_RES
odrv0.config.dc_max_negative_current = DC_MAX_NEG_CURR

#Select which axis (0 or 1) to configure
if axis_num == 0:

    #Motor controller settings
    axis0.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL #enum
    axis0.controller.config.vel_limit = VEL_LIM
    axis0.controller.config.vel_gain = VEL_GAIN
    axis0.controller.config.vel_integrator_gain = VEL_INT_GAIN

    #Motor settings
    axis0.motor.config.motor_type = MOTOR_TYPE_HIGH_CURRENT #enum
    axis0.motor.config.current_lim = CURR_LIM
    axis0.motor.config.calibration_current = CALIB_CURR
    axis0.motor.config.pole_pairs = POLE_PAIRS
    axis0.motor.config.torque_constant = TORQUE_CONSTANT

    #Encoder settings
    axis0.encoder.config.mode = ENCODER_MODE_HALL #enum
    axis0.encoder.config.cpr = ENCODER_CPR

else:
    #Motor controller settings
    axis1.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL #enum
    axis1.controller.config.vel_limit = VEL_LIM
    axis1.controller.config.vel_gain = VEL_GAIN
    axis1.controller.config.vel_integrator_gain = VEL_INT_GAIN

    #Motor settings
    axis1.motor.config.motor_type = MOTOR_TYPE_HIGH_CURRENT #enum
    axis1.motor.config.current_lim = CURR_LIM
    axis1.motor.config.calibration_current = CALIB_CURR
    axis1.motor.config.pole_pairs = POLE_PAIRS
    axis1.motor.config.torque_constant = TORQUE_CONSTANT

    #Encoder settings
    axis1.encoder.config.mode = ENCODER_MODE_HALL #enum
    axis1.encoder.config.cpr = ENCODER_CPR

#odrive.utils.dump_errors(odrv0) #might want this just in case

odrv0.save_configuration() #save all .config parameters to persistent memory so the ODrive remembers them between power cycles. This will reboot the board.