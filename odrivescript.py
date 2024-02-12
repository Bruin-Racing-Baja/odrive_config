import odrive
import time
from odrive.utils import dump_errors
import odrive.pyfibre.fibre.libfibre

def initial_configuration_24():
    odrv0.axis1.config.can.node_id = 1
    odrv0.can.config.baud_rate = 250000
    odrv0.axis1.motor.config.current_lim = 30
    odrv0.axis1.controller.config.vel_limit = 40
    odrv0.axis1.motor.config.calibration_current = 10
    odrv0.config.enable_brake_resistor = True
    odrv0.config.brake_resistance = 0.4699999988079071
    odrv0.config.dc_max_negative_current = -0.01
    odrv0.axis1.motor.config.pole_pairs = 7
    odrv0.axis1.motor.config.torque_constant = 8.27 / 140
    odrv0.axis1.motor.config.motor_type = 0
    odrv0.axis1.encoder.config.cpr = 8192
    odrv0.axis1.encoder.config.mode = 0
    odrv0.axis1.encoder.config.use_index = True
    odrv0.axis1.config.startup_encoder_index_search = False
    odrv0.axis1.controller.config.control_mode = 2
    odrv0.axis1.controller.config.vel_gain = 0.125
    odrv0.axis1.controller.config.vel_integrator_gain = .625

def initial_configuration_56():
    odrv0.axis1.config.can.node_id = 1
    odrv0.can.config.baud_rate = 250000
    odrv0.axis1.motor.config.current_lim = 24
    odrv0.axis1.controller.config.vel_limit = 80
    odrv0.axis1.motor.config.calibration_current = 10
    odrv0.config.enable_brake_resistor = True
    odrv0.config.brake_resistance = 0.4699999988079071
    odrv0.config.dc_max_negative_current = -0.01
    odrv0.axis1.motor.config.pole_pairs = 7
    odrv0.axis1.motor.config.torque_constant = 8.27 / 140
    odrv0.axis1.motor.config.motor_type = 0
    odrv0.axis1.encoder.config.cpr = 8192
    odrv0.axis1.encoder.config.mode = 0
    odrv0.axis1.encoder.config.use_index = True
    odrv0.axis1.config.startup_encoder_index_search = False
    odrv0.axis1.controller.config.control_mode = 2
    odrv0.axis1.controller.config.vel_gain = 0.125
    odrv0.axis1.controller.config.vel_integrator_gain = .625

print("hello")
odrv0 = odrive.find_any()

print (odrv0.vbus_voltage)

print("Starting motor calibration...")
x = input("Type 24 for 24vEncoder or 56 for 56vEncoder: ")
if x == "24":
    initial_configuration_24()
elif x == "56":
    initial_configuration_56()


try:
    print("we are here")
    odrv0.save_configuration()
except:
    print("now we are in the except")
    pass

odrv0 = odrive.find_any()

print("Running full axis state calibration")
odrv0.axis1.requested_state = 3

time.sleep(8)

odrv0.axis1.motor.config.pre_calibrated = True
odrv0.axis1.encoder.config.pre_calibrated = True

dump_errors(odrv0)

print("motor precalibrated: ", odrv0.axis1.motor.config.pre_calibrated)
print("encoder precalilbrated: ", odrv0.axis1.encoder.config.pre_calibrated)

print("Saving configuration...")
#odrv0.save_configuration()
print("Finding index")
odrv0.axis1.requested_state = 6

time.sleep(5)

odrv0.axis1.requested_state = 8
odrv0.axis1.controller.input_vel = 0

time.sleep(5)

while True:
    x = input("give me a velocity. or type q to quit. ")
    if x == "q":
        print("ok bye bye")
        odrv0.axis1.controller.input_vel = 0
        break

    odrv0.axis1.controller.input_vel = x
