#!/usr/bin/env python
import odrive
import odrive.enums
import time
import numpy as np

odrv0 = odrive.find_any()
axis1 = odrv0.axis1

def config():
    # config
    axis1.motor.config.current_lim = 10
    axis1.motor.config.calibration_current = 10
    odrv0.config.enable_brake_resistor = True
    odrv0.config.brake_resistance = 0.5
    odrv0.config.dc_max_negative_current = -0.01
    axis1.motor.config.pole_pairs = 12  # poles / 2
    axis1.motor.config.torque_constant = 8.27 / 330  # 8.27 / KV
    axis1.motor.config.motor_type = odrive.enums.MOTOR_TYPE_HIGH_CURRENT
    axis1.controller.config.vel_gain = 0.01
    axis1.controller.config.vel_integrator_gain = 0.05
    axis1.controller.config.control_mode = odrive.enums.CONTROL_MODE_VELOCITY_CONTROL
    axis1.controller.config.vel_limit = 400/(2*np.pi*12)
    axis1.motor.config.current_lim = 2 * odrv0.axis0.config.sensorless_ramp.current
    axis1.sensorless_estimator.config.pm_flux_linkage = 5.51328895422 / (12 * 330)
    axis1.config.enable_sensorless_mode = True
    axis1.config.startup_encoder_index_search = False
    axis1.encoder.config.use_index = False

    odrv0.save_configuration()

def calibrate():
    # calibration
    axis1.requested_state = odrive.enums.AXIS_STATE_MOTOR_CALIBRATION
    axis1.motor.config.pre_calibrated = True
    odrv0.save_configuration()

def velocity():
    # start closed loop
    axis1.requested_state = odrive.enums.AXIS_STATE_CLOSED_LOOP_CONTROL

    # set velocity
    axis1.controller.input_vel = 0
    print(axis1.controller.input_vel)

    time.sleep(1)

    # disable velocity control
    axis1.requested_state = odrive.enums.AXIS_STATE_IDLE

def stop():
    axis1.requested_state = odrive.enums.AXIS_STATE_IDLE

def errors():
    odrive.utils.dump_errors(odrv0)

config()
calibrate()
#stop()
