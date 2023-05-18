# odrive_config

This repository contains all the configuration data needed to make our odrives to operate smoothly and efficiently.
Follow the steps below to get the odrive operational

## 1 upload our firmware to the Odrive
We have custom firmware on our odrive to add limit switch and some CAN gpio reading functionality. Uploading firmware should only be done once when we have a new odrive or changes need to be made to firmware.

I normally used STM32Cube programmer to do this but documentation for other methods is described here: https://docs.odriverobotics.com/v/0.6.0/dfu.html

## 2 connect to odrive via odrivetool and upload our configuration
The odrive is great because it can be used for many different motors and voltages. In order to get the odrive to work with our system we need to change certain parameters in the odrives configuration. 

You can interface with the odrive using its microusb port and anywhere you can run python. Odrive has its own python interface called odrivetool which you can install sending "pip install --upgrade odrive" in your command terminal.

Configuration data and instructions can be found in the various textfiles in this repository. In the future we may make a python script to do this automatically.

56vEncoder.txt contains the commands for running our 56v odrives with an encoder
24vEncoder.txt contains the commands for running our 24v odrives with an encoder

Odrive_actuator_config_copypaste.txt has our old calibration files from last year which include old motor gains and hall effect configurations

## Common problems
Odrive doesn't show up in odrivetool
    -Is the green power LED on? If not the odrive probably isn't receiving power. Check fuses or multimeter voltage between power and ground.
    -If you're on windows there's a good chance you need to change your USB driver using Zadig: https://zadig.akeo.ie/ and set the odrive driver to libusb-win32 or the other drivers until it works.
Odrive doesn't want to do axis state calibration sequence after calibration
    -dump errors before and after.
    -Check all connections (motor wires, encoders, estops)
    -Make sure to save configuration of the odrive before running axis state calibration
    -if it only does the initial first spin that might mean the hardware limit switches are unplugged 