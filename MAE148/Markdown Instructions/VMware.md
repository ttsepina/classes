# VMware Player Installation

Virtual machines (VMs) are essentially computers running on computers &mdash; you can simulate a different operating system than the one native to your computer.

## Prerequisites

* Unzipping software (7Zip, Winrar) 

* Download the VMware Player installer (depending on your machine's OS)

* Download the Ubuntu VM image &mdash; make sure you have enough space on your disk   (~40 GB zipped, ~50 GB unzipped)

* Minimum 8 GB system RAM on host machine (by default the VM uses 5 GB)
  * If your system has at least 16 GB of RAM, enter the VM settings for the image and increase the RAM alloted to 8 GB; the VM must not be running to do so

## VMware setup

* Open VMware Player and select *Open a Virtual Machine*
  * You will be prompted to select an image to be added &mdash; select the image you downloaded with the *.vmx*
 extension

* It should now appear in the list on the left of the VMware Player window &mdash; single-click the image and select *Edit Virtual Machine Settings*

* Here you can edit the memory settings and any other settings required to run the VM

* If you experience an issue with respect to *Intel-VT* or *AMD-V*, disable the virualization engine in the *Processors* tab 

## Initial Boot up of VM

* If necessary, enable virtualization in your BIOS/UEFI

* When you are ready, start the virtual machine

* Login Credentials
  * User: ucsd
  * Password: UcsdStudent 

### Cutting and Pasting

* If cutting and pasting is not working from the host to the VM, open a terminal in the VM and run the following commands:

```
    sudo apt-get autoremove open-vm-tools
    sudo apt-get install open-vm-tools-desktop
    sudo reboot now
```
## Connecting Game Controller

Connecting a game controller is useful in order to control the car used in the simulations you will be running and other projects (these can include Playstation or Xbox controllers, or the Logitech controller likely included in your kit) 

These should be connected using via a USB cable, Bluetooth, or a USB dongle.

When connecting a controller, the VM should ask if the input device will be connected to the host system or the virtual machine &mdash; connect it to the VM.

### Verify Controller connection

The controller will be identified as js0 (or js# if there are multiple "joysticks" connected to the system)

Run the following command in a VM terminal:

    ls /dev/input

If the controller is connected, it should appear as js0 in the terminal output.

To test the joystick controls, run in a terminal:

    sudo apt-get update
    sudo apt-get install -y jstest-gtk
    jstest /dev/input/js0

Then interact with the controller to see the values printed to the terminal change (analog inputs should change smoothly, while digital inputs like button presses change between on and off)

### Custom Controller 

If your controller is not behaving correctly, or you need to generate new controller mappings, you can generate custom controllers. 

See https://docs.donkeycar.com/parts/controllers/ for controller support; custom mapping is linked at the bottom of the page.

To setup a new controller or modify input mappings, you can use the Joystick Wizard (described here: https://docs.donkeycar.com/utility/donkey/#joystick-wizard)

The joystick wizard creates a custom controller named "my_joystick.py" in the *mycar* folder. To enable it, in the *myconfig.py* file, set ```CONTROLLER_TYPE="custom"``` 
    
To run the wizard, from a terminal in the PATH/TO/mycar directory, run 

    donkey createjs

To determine if the system can see the input device, jstest can be used. If it is not installed, run ``` sudo apt install joystick```

## DonkeyCar AI Framework

This software allows you to train an AI model to run simulated or even physical vehicles using computer vision (either virtually or in reality).

### Launching the Simulator

Using the file explorer in the VM, navigate to ```~/projects/DonkeySimLinux/``` and execute the file ```donkey_sim.x86_64```

### Track Names

Depending on the track to be raced on, you need to change the track to train on; those include:

* donkey-circuit-launch-track-v0
* donkey-warren-track-v0
* donkey-mountain-track-v0

### Customizing Virtual Car

From a terminal, run ```atom myconfig.py``` from the ```~/projects/d4_sim/``` directory.

Within the ```myconfig.py``` file, change the:

* car_name
* racer_name
* your country location (under "country")
* a fun fact (under "bio")
* car color (under "body_rgb")

#### Example Config File
```
# 04Jan22
# UCSD mods to make easier for the UCSD students to use the Donkey-Sim
# the following uncommented lines where copied here from the body of myconfig.py below
DONKEY_GYM = True
# DONKEY_SIM_PATH = "remote"
DONKEY_SIM_PATH = "/home/ucsd/projects/DonkeySimLinux/donkey_sim.x86_64"
# DONKEY_GYM_ENV_NAME = "donkey-warren-track-v0"
DONKEY_GYM_ENV_NAME = “donkey-mountain-track-v0”
# UCSD yellow color in RGB = 255, 205, 0
# UCSD blue color in RGB = 0, 106, 150
GYM_CONF = { "body_style" : "car01", "body_rgb" : (255, 205, 0), "car_name" : "UCSD-148-YourName", "font_size" : 30} # body style(donkey|bare|car01) body rgb 0-255
GYM_CONF["racer_name"] = "UCSD-148-YourName"
GYM_CONF["country"] = "USA"
GYM_CONF["bio"] = "Something_about_you, ex: Made in Brazil"
#
# SIM_HOST = "donkey-sim.roboticist.dev"
 SIM_ARTIFICIAL_LATENCY = 0
SIM_HOST = "127.0.0.1"              # when racing on virtual-race-league use host "roboticists.dev"
# SIM_ARTIFICIAL_LATENCY = 30          # Use the value when you ping roboticists.dev. When racing on virtual-race league, use 0 (zero)

# When racing, to give the ai a boost, configure these values.
AI_LAUNCH_DURATION = 3            # the ai will output throttle for this many seconds
AI_LAUNCH_THROTTLE = 1            # the ai will output this throttle value
AI_LAUNCH_KEEP_ENABLED = True      # when False ( default) you will need to hit the AI_LAUNCH_ENABLE_BUTTON for each use. This is safest. When this True, is active on each trip into "local" ai mode.
#
# When using a joystick modify these specially USE_JOYSTICK_AS_DEFAULT = True
# JOYSTICK
# USE_JOYSTICK_AS_DEFAULT = True     #when starting the manage.py, when True, will not require a --js option to use the joystick
JOYSTICK_MAX_THROTTLE = 1.0         #this scalar is multiplied with the -1 to 1 throttle value to limit the maximum throttle. This can help if you drop the controller or just don't need the full speed available.
JOYSTICK_STEERING_SCALE = 0.8       #some people want a steering that is less sensitve. This scalar is multiplied with the steering -1 to 1. It can be negative to reverse dir.
AUTO_RECORD_ON_THROTTLE = True      #if true, we will record whenever throttle is not zero. if false, you must manually toggle recording with some other trigger. Usually circle button on joystick.
JOYSTICK_DEADZONE = 0.2             # when non zero, this is the smallest throttle before recording triggered.
# #Scale the output of the throttle of the ai pilot for all model types.
AI_THROTTLE_MULT = 1.0              # this multiplier will scale every throttle value for all output from NN models
#

```
