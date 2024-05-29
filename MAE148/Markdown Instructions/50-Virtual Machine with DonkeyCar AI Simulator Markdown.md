<!-----

You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 37

Conversion time: 12.976 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β35
* Thu Apr 25 2024 12:17:21 GMT-0700 (PDT)
* Source doc: Copy of 50-Virtual Machine with DonkeyCar AI Simulator
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 37.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>
<a href="#gdcalert7">alert7</a>
<a href="#gdcalert8">alert8</a>
<a href="#gdcalert9">alert9</a>
<a href="#gdcalert10">alert10</a>
<a href="#gdcalert11">alert11</a>
<a href="#gdcalert12">alert12</a>
<a href="#gdcalert13">alert13</a>
<a href="#gdcalert14">alert14</a>
<a href="#gdcalert15">alert15</a>
<a href="#gdcalert16">alert16</a>
<a href="#gdcalert17">alert17</a>
<a href="#gdcalert18">alert18</a>
<a href="#gdcalert19">alert19</a>
<a href="#gdcalert20">alert20</a>
<a href="#gdcalert21">alert21</a>
<a href="#gdcalert22">alert22</a>
<a href="#gdcalert23">alert23</a>
<a href="#gdcalert24">alert24</a>
<a href="#gdcalert25">alert25</a>
<a href="#gdcalert26">alert26</a>
<a href="#gdcalert27">alert27</a>
<a href="#gdcalert28">alert28</a>
<a href="#gdcalert29">alert29</a>
<a href="#gdcalert30">alert30</a>
<a href="#gdcalert31">alert31</a>
<a href="#gdcalert32">alert32</a>
<a href="#gdcalert33">alert33</a>
<a href="#gdcalert34">alert34</a>
<a href="#gdcalert35">alert35</a>
<a href="#gdcalert36">alert36</a>
<a href="#gdcalert37">alert37</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



## 
Virtual Machine with DonkeyCar/DonkeySim AI Simulator


## 04Oct22 - V5

[The previous version of this document for DonkeyCar 3.x is here](https://docs.google.com/document/d/17EdoqDCiriZ0wldH92uYNHcvwlByuapvx_Z9rY573I0/edit?usp=sharing)

Prepared by

Dr. Jack Silberman

Department of Electrical and Computer Engineering

and 

Dominic Nightingale

Department of Mechanical and Aerospace Engineering

University of California, San Diego

9500 Gilman Dr, La Jolla, CA 92093

	

<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


	

<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")


	

<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")


		

Table of Contents


[TOC]



## 


## Initial Setup


### Download and Install

# You will need  [VMware Player](https://www.vmware.com/products/workstation-player.html) (Windows and Linux),  Fusion Player (MacOS).

# Not working for Mac M1 or M2 yet.

#[ A VMware virtual machine image can be downloaded from here](https://drive.google.com/file/d/1aGVPzoEPYW0GxUnVGjzkiNsqqJFgZ7hb/view?usp=sharing). Download and unzip it

# at your host computer.

# Once unzipped the virtual machine will take about 40G bytes of disc space. If needed, clear some

# space from your computer, example removing videos from

# your computer. Alternatively, use an USB external drive if needed.

# You need a host machine with at least 8G of RAM. The virtual machine is configured by 

# default to use 5G of RAM. If your host machine has 16G RAM or more, please configure your virtual

# machine to use 8G RAM. With the virtual machine not running, change the virtual hardware

# configuration.


### Initial Boot up of VM

# Start the virtual machine using the VMware Player (Windows and Linux),  Fusion Player (MacOS). 


    # If needed to boot,  enable Virtualization on your BIOS/EFI 


    # or modify the virtual machine configuration 


    # On the VMware player machine configuration, disable optimization for virtualization.


    # Example of the virtual machine settings Fusion player on a Mac


    # Processors & Memory / Advanced Options



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")



#### Log into the VMware virtual machine 


    #User: ucsd


    #Password: UcsdStudent

Cutting and Pasting (cut and paste)

# If cutting and pasting from your host computer is not working

# Open a terminal in the VMware machine

sudo apt-get autoremove open-vm-tools

sudo apt-get install open-vm-tools-desktop

sudo reboot now

 


## Connecting Game Controller

# Using a game controller will be desirable. 

# Examples of game controllers

# PS3, PS4, XBox, or Logitech F710. 

# The controller needs to be connected to the

# host computer using USB cable, Bluetooth, or an USB dongle

 

# The VMware Player should ask you where you want to connect the game controller. 

# Hosts or the Linux Virtual machine. 

# Connect to Linux.

# The pop-up window with the options will show as either one of the following:

# If you don’t see this option simply reconnect the controller



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")




# Verify that the virtual machine can see the game controller, identified as **js0**

# Open a terminal in the VMware machine

ls /dev/input 

# After you can see js0 at /dev/input, let’s test the joystick controls

# From a terminal:

sudo apt-get update

sudo apt-get install -y jstest-gtk

jstest /dev/input/js0

# Move/press the game controller buttons

# Test the two joysticks

# Test buttons Sony PS3/PS4 

# Triangle 

# X

# Select/Share

# Start/Options

# Other game controllers, try some

# equivalent buttons


### 


### What if my game controller is not working as I expected?

# Jack, what if my game controller works with the jstest /dev/input/js0 but  is not working with

# the DonkeyCar as I expected. Wrong controls, ec.

# Not to worry much, [there is a way to build a custom file](https://docs.donkeycar.com/parts/controllers/) for your game controller for the 

# controls we use the most.


### Custom controller (if needed/desired)

Note: If you have a controller that is not listed below, or you are having troubles getting your controller to work or you want to map your controller differently, see [Creating a New or Custom Game Controller](https://docs.donkeycar.com/parts/controllers/#creating-a-new-or-custom-game-controller).

To discover or modify the button and axis mappings for your controller, you can use the [Joystick Wizard](https://docs.donkeycar.com/utility/donkey/#joystick-wizard). The Joystick Wizard will write a custom controller named 'my_joystick.py' to your mycar folder. To use the custom controller, set CONTROLLER_TYPE="custom" in your myconfig.py.

# From a terminal:

donkey createjs



* Run the command from your ~/mycar directory
* First make sure the OS can access your device. The utility jstest can be useful here. Installed via: sudo apt install joystick You must pass this utility the path to your controller's device. Typically this is /dev/input/js0 However, if it is not, you must find the correct device path and provide it to the utility. You will need this for the createjs command as well.
* Run the command donkey createjs and it will create a file named my_joystick.py in your ~/mycar folder, next to your manage.py
* Modify myconfig.py to set CONTROLLER_TYPE="custom" to use your my_joystick.py controller


## 


## DonkeyCar AI Framework

Donkey AI Framework Explained

[https://ori.codes/artificial-intelligence/](https://ori.codes/artificial-intelligence/)


### How to Launch the Simulator

# Start the Donkey-Sim   

# Use the “File Explorer” to navigate to  

# ~/projects/DonkeySimLinux/

# Execute (double click over the file) donkey_sim.x86_64

# You should see the Donkey-Sim ready for use 


### Track names

# Depending on the track we will be racing on, you need to train on that track that will be used during the race to be able to race against other people

# donkey-circuit-launch-track-v0

# donkey-warren-track-v0

# donkey-mountain-track-v0


    # ------------------------------------------------------------------


    # [For the race on 15Jan2022](https://www.meetup.com/DIYRobocars/) 


    # We are using the track donkey-mountain-track-v0


    # ------------------------------------------------------------------


### 


### Customize your virtual robot

# From a terminal:

atom myconfig.py

# Change the car_name, racer_name, your country location, and funny fact about you

# Change the color for the robot body to one of the two UCSD’s colors yellow or blue

# Below is an example of a myconfig.py


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


### 


### Get Latency from remote server

# Ping donkey-sim.roboticist.dev take note of the average ping time, ex: 30 ms. 

> ping donkey-sim.roboticist.dev



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.png "image_tooltip")


# In this case since I am in the same network as the donkey-sim.roboticist.dev my ping time 

# is much smaller &lt;0.5 ms. Assuming you are in the USA, you should get between 20~60 ms

# Then write it at the SIM_ARTIFICIAL_LATENCY

SIM_ARTIFICIAL_LATENCY = 30


### Collecting Data

#We will do a “behavioral cloning” AI

#Drive the robot in the local simulator

# If you have not activated the donkey virtual environment,   

conda activate donkey

# (donkey) will show up at the start of the terminal line



<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image7.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image7.png "image_tooltip")


# Change to your donkey car directory

# ex: cd ~/projects/d4_sim

# Now let's drive the robot to collect data automatically

 python manage.py drive


    

<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image8.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image8.png "image_tooltip")


# Open a web browser like Chrome

http://localhost:8887


#### Driving with keyboard and mouse from web browser

# Depending if you have a game controller connected to your virtual machine or not, you can 

# drive your robot with the game controller or mouse/keyboard



<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image9.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image9.png "image_tooltip")



#### 


#### Driving with a physical joystick

# If you connected a game controller and want to use it directly without http://localhost:8887

# Edit myconfig.py

atom myconfig.py


    # JOYSTICK


    USE_JOYSTICK_AS_DEFAULT = **True**     #when starting the manage.py, when True, wi$


    JOYSTICK_MAX_THROTTLE = 1.0         #this scalar is multiplied with the -1 to 1$


    JOYSTICK_STEERING_SCALE = 0.7       #some people want a steering that is less s$


    AUTO_RECORD_ON_THROTTLE = True      #if true, we will record whenever throttle $


    CONTROLLER_TYPE='**F710**'               #(ps3|ps4|xbox|nimbus|wiiu|F710|rc3|MM1|cu$


    JOYSTICK_DEADZONE = 0.0             # when non zero, this is the smallest throttle before recording triggered.

# There are some advantages - You can use buttons on the controllers 



* Delete 100 data points (@20HZ = 5s) - PS3/PS4 “Triangle”, Logitech F710 “Y”
* Emergency Stop - PS3/PS4 “X”, Logitech F710 “A”
* Change operation modes - PS3/PS4 “Select/Options”, Logitech F710 “Back”

# Practice for a while, don’t worry about not driving well initially, 

# we will show you how to delete all the data you collected so far 

# so you can start with a clean set in a while.

# Hint, to delete the last 100 data points (5s of driving) 

# press the green triangle on PS3* 

# read the keys your game controller uses when you start the          # donkey framework

# We will train the AI model in increments of approximately 20 laps, count your laps as feasible.

**# To stop the DonkeyCar framework with Ctrl-C   (like other Python Code you used so far) **


#### Deleting data that you don't want to use for training

# Deleting the entire data directory to start fresh. It is basically Linux …

The data is in the data directory. Where are they? Guess.



<p id="gdcalert10" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image10.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert11">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image10.png "image_tooltip")


# Now lets clean-up the whole data directory and start fresh



<p id="gdcalert11" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image11.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert12">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image11.png "image_tooltip")


 

 rm -rf data

# Then we need to create the data directory again

mkdir data


### Training and Testing

# Train the model using all the data giving it a name ex: 20aug20_sim_160x120_1.h5

python train.py --model=models/20aug20_sim_160x120_20.h5 --type=linear --tubs=data/

# Let's test your model

python manage.py drive --model=/models/19sep20_sim_160x120_20.h5 --type=linear

# Then press “select” twice on the game controller (PS3) to start the AI model to drive. Or other #controllers, read how to change “mode” when you start the Donkey AI framework. Post on Basecamp. # We will figure it out.

# Does the AI model work? If not, add another 20 claps and train. 

# If your model is not working around the corners, there is a chance that the corners are not being 

# recorded. If your myconfig.py has AUTO_RECORD_ON_THROTTLE = True then manage.py will be

# keeping track of your throttle, and will only record when it is non zero. This means that if you let go of

# the throttle while going around the corners, that it will stop recording. This means that the system

# will not learn how to go around the corners. If this is happening, there are two solutions. One is to

# make sure to keep at least a little bit of throttle when going around the corners (if the car is driving

# too fast for you, try and lower the JOYSTICK_MAX_THROTTLE value) . The other solution is to change

# AUTO_RECORD_ON_THROTTLE = True to AUTO_RECORD_ON_THROTTLE = False, and to figure out

# which button toggles the recording state for your controller. 

#It is a good idea to keep your terminal viewable while you are driving as it will allow you to see if you are recording data or not

# You can rename the model as you go. ex: 19sep20_sim_160x120_40.h5 

python train.py --model=models/19sep20_sim_160x120_40.h5 --type=linear

# Let's test your model with all the data

python manage.py drive --model=./models/19sep20_sim_160x120_40.h5 --type=linear

# Train on a specific Tub and transfer to a previous model

python train.py --tub ~/projects/d3_sim/data/tub_name  --transfer=models/previous_model.h5  --model=models/new_model.h5

ex:

python train.py --tub ~/projects/d3_sim/data/tub_name  --transfer=models/  19sep20_sim_160x120_20.h5 --model=models/19sep20_sim_160x120_40.h5 --type=linear




### Upgrading to the latest Donkey-Sim and Donkey-Gym (if needed)

# When you know there was a new release of the Donkey-Sim, you don’t need to get a 

# new virtual machine. Just upgrade what is needed.

#

# Delete your previous donkey-sim directory and DonkeySimLinux.zip



<p id="gdcalert12" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image12.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert13">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image12.png "image_tooltip")




<p id="gdcalert13" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image13.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert14">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image13.png "image_tooltip")


# From the virtual machine open a web browser

# Download the binary version that you are looking for from here

[https://github.com/tawnkramer/gym-donkeycar/releases](https://github.com/tawnkramer/gym-donkeycar/releases)

# ex:



<p id="gdcalert14" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image14.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert15">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image14.png "image_tooltip")


# Remember that on our virtual machine we run Linux …



<p id="gdcalert15" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image15.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert16">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image15.png "image_tooltip")




* Extract the Zipped file  into your projects directory



<p id="gdcalert16" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image16.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert17">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image16.png "image_tooltip")




* Make the donkey-sim executable - in a terminal navigate to where you extracted the executable. I hope you learned that already from our intro to Linux 
    * chmod +x donkey_sim 
* Or use the Files/Properties/Allow executing file as program
* Then run the Donkey-Sim as you already know how to do



<p id="gdcalert17" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image17.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert18">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image17.png "image_tooltip")




<p id="gdcalert18" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image18.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert19">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image18.png "image_tooltip")


# DonkeyCar dev vs. main branch

# 

# https://docs.donkeycar.com/guide/host_pc/setup_ubuntu/

# Delete the previous donkeycar  install if you have it

cd ~/projects

rm -rf donkeycar

rm -rf d4_sim

git clone https://github.com/autorope/donkeycar

cd donkeycar

git checkout main

conda update -n base -c defaults conda

conda env remove -n donkey

conda env create -f install/envs/ubuntu.yml

# Conda installs sometimes get too slow. Then lets try mamba


    conda install mamba -n base -c conda-forge


    mamba env create -f install/envs/ubuntu.yml

conda activate donkey

pip install -e .[pc]

donkey createcar --path ~/projects/d4_sim

# Now let's upgrade the donkeygym

# Why do we need to do that? Because this is the interface between the simulator donkey-sim

#  and your code donkeycar

# [https://github.com/tawnkramer/gym-donkeycar](https://github.com/tawnkramer/gym-donkeycar)

# Open a terminal

conda activate donkey

cd ~/projects/donkeycar

pip install git+https://github.com/tawnkramer/gym-donkeycar --upgrade



<p id="gdcalert19" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image19.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert20">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image19.png "image_tooltip")


# Lets test the Donkey-Sim

# Double click over the donkey_sim.x86_64 



<p id="gdcalert20" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image20.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert21">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image20.png "image_tooltip")




<p id="gdcalert21" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image21.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert22">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image21.png "image_tooltip")


<p id="gdcalert22" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image22.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert23">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image22.png "image_tooltip")



### 


### Common Issues


#### Slow FPS Locally

Running the Donkey-Sim on your host computer vs. Virtual Machine

By Haoru Xue

Oct 27

Define low FPS: if you are not getting 20 FPS on your local simulator, then there is a large chance that your trained model will not do well on the remote machine. Because a stock donkeycar runs at 20Hz. If the simulator is not able to update the environment at higher or equal to the same frequency, you will have trouble controlling the car. And even if your model might seem to work on your local machine, it will break once running on the remote server which is refreshing more frequently.

There is a great fix to this as I just helped a student from 10-15 FPS to 30-40 FPS.

The typical bottleneck is the fact that you are essentially running a 3D game, that runs on Ubuntu, that runs on Windows/Mac. Virtualization could significantly drag your simulator performance down.

**The solution is to run the simulator on your Windows/Mac, while running everything else on Ubuntu.**

How to: 



1. Close anything that could be eating up your system resources such as browsers. If you need the documentation, open it on your phone/tablet.
2. Download [simulator binaries](https://github.com/tawnkramer/gym-donkeycar/releases/tag/20.9.14) for your base system **in your base system**. Download DonkeySimWin for Windows, and DonkeySimMac for Mac.
3. Mac Only: If you cannot open the simulator, it is most likely due to insufficient permission.open a terminal, cd into the simulator package, and do "chmod +x donkey_sim"
4. Windows Only: If prompted blocked by Windows Defender, click on "More Info", and "Run Anyway".
5. Look up your Windows/Mac IP address: type "ipconfig" in a cmd/PowerShell/terminal window, and copy down IPV4 address, usually in the form of 192.168.X.XXX.
6.  **Important**: On Ubuntu VM, go to myconfig.py, change "sim_path" to "remote", and "sim_host" to "192.168.X.XXX", the IPV4 address of your Windows/Mac machine. This will treat the simulator just as a remote server.
7. Launch the car. you should see the car running on the simulator, directly on your base system. Notice the FPS improvement.

Note: this also means that whenever you are launching the car, **you need to manually launch the simulator first**. Donkey won't launch it for you since it cannot launch a program outside the VM.




## UCSD GPU Cluster Instructions

**# Hold on using the GPU cluster until you are told the GPU cluster is ready for you to use**

**# Please do not use the GPU cluster until you demonstrate training on your local machine first.**

**# It is part of your deliverables for the class.**

# If needed, to look up your username (https://sdacs.ucsd.edu/~icc/index.php)

# [Instructions from our IT folks](https://docs.google.com/document/u/1/d/e/2PACX-1vTe9sehl7izNJJNypsDNABD4wg-F-AClAi0cYV3pIIRGpCknD7SEWQPEGqy_5DBRmFQtkulLkHkLxEm/pub)

# For faster training, we will access the gpu-clusters provided by the school

# Within your VMmachine you will have 2 terminals,

# 1. Local session: Terminal on your host. If you train here, you will be doing local training using 

# VMmachine 

# 2. Remote session: You will ssh onto the account provided by the school to train using gpu

# 	you can train models, and store data within 2 containers available inside the ssh session

# First, open your local session in one terminal and ssh onto gpu-cluster on another terminal

# In order to access the gpu-cluster, you must ssh onto your assigned account. Ex:

ssh  &lt;user_name>@dsmlp-login.ucsd.edu

# You will be asked your password (case-sensitive)

# For security reasons, no characters will be shown when typing in your password

# The highlighted will be replaced with you username, and the extension might also be different 



<p id="gdcalert23" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image23.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert24">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image23.png "image_tooltip")


# Launching a container inside your ssh session

# Within your account you have access to a container with only a CPU and another container 

# with the GPU that the school provides

# The GPU clusters are limited, so you want to make sure you are only using it for training, and # the CPU for transferring data and everything else that does not require more computer power.

# This are the options available (do not type anything under your session yet)

# Launching container for transferring data (2 CPU, 4G RAM)

	launch-scipy-ml.sh -i ucsdets/donkeycar-notebook:latest

# Or launching container for training (8 CPU, 1 GPU, 16G RAM)

	launch-scipy-ml.sh -g 1 -i ucsdets/donkeycar-notebook:latest

# When creating the gpu container this will show in your terminal:



<p id="gdcalert24" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image24.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert25">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image24.png "image_tooltip")


	

# Make sure to only have one container open at the time

# Each time you launch a container it creates a ‘pod’, in order to successfully exit the pod do:

	exit 

# To confirm you have exited the launched container and it was automatically deleted do

	kubectl get pods 

# This should return _‘no resources found’_

# If you do have pods you have to delete them with

	Kubectl delete pod &lt;pod_name>

# For example, killing the gpu container launched above

<p id="gdcalert25" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image25.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert26">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image25.png "image_tooltip")


# Now, in the remote session, prepare donkeyCar:

# The donkey environment is automatically invoked for you, so no more conda activate donkey

On entering try 

           #conda activate donkey

If this doesn’t work because donkey not found then

           # conda init

Relogin

	# conda activate donkey

After you have confirmed that you are in the virtual environment


    #mkdir ~/projects


    #cd ~/projects


    #donkey createcar --path d4_sim


    #cd d4_sim

# First transfer, transfer your ‘my_config.py’, for example:

rsync -avr -e ssh myconfig.py &lt;user_name>@dsmlp-login.ucsd.edu:projects/d4_sim/

# if you modify the my_config.py on your local session you must transfer it again 

# Transfering the data collected in local session to the remote session for the gpu training

# In local session do:

rsync -avr -e ssh data/&lt;tub_name> &lt;user_name>@dsmlp-login.ucsd.edu:projects/d4_sim/data/

# Transferring specific tubs. For example, sending all the tubs with name ‘tub_#_21-07-13’

# In local session:



<p id="gdcalert26" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image26.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert27">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image26.png "image_tooltip")


# These tubs will now show in your remote session (ssh)



<p id="gdcalert27" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image27.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert28">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image27.png "image_tooltip")


# Training the model on remote session

# Once you get your data and my_config.py file transfered, this step is the same as how you 

# would do it in your local setup. 

# In remote session

# You can use multiple tubs, separated by comma (NO SPACE)

python manage.py train --tub data/tub1,data/tub2 --model models/pilot.h5

# OR

# manage.py train & train.py should have the same effect

python train.py --tub data/tub1 --model models/p_1.h5

# OR

# transfer training: alter the previous model behavior with new data

python train.py --tub data/tub1 --model models/p_2.h5 --transfer models/p_1.h5

**Note: **If `imgaug` is not available and Donkeysim generates and error, run

	pip install imgaug

# Transfering model back to local session

# Similar as before using the rsync command, but the source and destinations are flipped

# as we are transferring from remote > local

# In local session (one line command)

rsync -avr -e ssh &lt;user_name>@dsmlp-login.ucsd.edu:projects/d4_sim/models/&lt;model_file> models/

# Then you can test your car in the local session as before \





## Using a Remote Server for the Simulator

# External server name donkey-sim.roboticist.dev

Please remember to remove the latency from your myconfig.py when using an external server

Where does the latency number come from? I hoped you followed the instructions during the class and used the ping result number from &lt;ping donkey-sim.roboticist.dev> before you trained your model.

Here are some hints where to change things on your myconfig.py

# #When racing, to give the ai a boost during start, configure these values.

AI_LAUNCH_DURATION = 3

AI_LAUNCH_THROTTLE = 1.0

#

# If you want to slow down your robot a bit, modify this and test

AI_THROTTLE_MULT = 87

#

#

DONKEY_GYM = True

DONKEY_SIM_PATH = "remote"

#

SIM_HOST = "donkey-sim.roboticist.dev"

SIM_ARTIFICIAL_LATENCY = 0

#

# AI_LAUNCH_KEEP_ENABLED = True

Hey Professor, if I am not running the simulator on my local machine, how do I see my robot on the track?

Good question. Try this to see what happens:

[https://www.twitch.tv/roboticists](https://www.twitch.tv/roboticists)     (for the 15Jan22 ECE MAE 148 prep and race)

or 

[https://www.twitch.tv/roboticists2](https://www.twitch.tv/roboticists2)

Your robot should show at the Twitch stream after a few  seconds once  you start it. Remember, everything you see on the twitch stream is in the past a few seconds, it is not near real-time.

Consider following Roboticists so you get notified when the server is up for you to train.

Remember, these are cutting edge tools, they may break periodically and “cut” us...

Have fun.

- Jack


## 


## ROS2

# Robot Operating System (ROS) 2

**# The virtual machine with Ubuntu 20.04 already has ROS2 installed.**


### Steps to install on another machine if desired (DO NOT DO ON VM)

Just in case you want to install it in another Ubuntu 20.04 machine

# Always follow the last version from the official support site

# ROS2 releases

# https://docs.ros.org/en/foxy/Releases.html



<p id="gdcalert28" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image28.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert29">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image28.png "image_tooltip")


# https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html

# Let’s install the latest long term supported Foxy Fitzroy

# https://docs.ros.org/en/foxy/Tutorials/Configuring-ROS2-Environment.html

# Follow the instructions to set the latest repository

sudo apt-get update

sudo apt-get upgrade

# Lets install the desktop version to have most of the packages available for us 

# Desktop Install -  ROS, RViz, demos, and tutorials

sudo apt install ros-foxy-desktop

# Why do we need to source (run) setup.bash? Enable to Ubuntu to find the ROS2 install 


    “


    This is accomplished by sourcing setup files every time you open a new shell, or by adding the source command to your shell startup script once. Without sourcing the setup files, you won’t be able to access ROS 2 commands, or find or use ROS 2 packages. In other words, you won’t be able to use ROS 2.


    “

# If you don’t want to source setup.bash everytime you open a terminal 

echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc

 #


    ”


    To undo this (to change to another distro) in Linux and macOS, locate your system’s shell startup script and remove the appended source command.


    “

#

# Otherwise you will need to enter this every time you open a terminal before using ROS2

# source /opt/ros/foxy/setup.bash

sudo apt update

sudo apt install -y python3-pip

pip3 install -U argcomplete

# Installing colcon - https://colcon.readthedocs.io/en/released/user/installation.html

# Debian package:

# /usr/share/colcon_cd/function

# /usr/share/colcon_argcomplete/hook

sudo apt install python3-colcon-common-extensions

echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc

echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc

# Let's create a directory for development and source files. In ROS we called in a work space (ws).

# We will have our source files in the directory src

# We will get some sample files from ros_tutorials

# 

mkdir -p ~/projects/ros2/dev_ws/src

cd ~/projects/ros2/dev_ws/src

git clone https://github.com/ros/ros_tutorials.git -b foxy-devel



<p id="gdcalert29" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image29.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert30">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image29.png "image_tooltip")


# Go to the root of the workspace (ws), then let's resolve dependencies

cd /home/ucsd/projects/ros2/dev_ws

rosdep install -i --from-path src --rosdistro foxy -y

# Now lets build the software that is in your workspace source ws/src

colcon build



<p id="gdcalert30" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image30.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert31">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image30.png "image_tooltip")


# Open a new terminal

**# It is important to do this from a new terminal..**

# If not done at your ~/.bashrc

source /opt/ros/foxy/setup.bash 

# In the root of your workspace, source your overlay. Overlays is where you have your developments /

#  in addition to the ROS2 install.

. install/local_setup.bash

# Installing Gazebo

#http://gazebosim.org/tutorials?tut=ros2_installing&cat=connect_ros

sudo apt install ros-foxy-gazebo-ros-pkgs

source /opt/ros/foxy/setup.bash


### Testing ROS2

# Open another terminal

ros2 run demo_nodes_cpp talker

# Ctrl-C to stop



<p id="gdcalert31" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image31.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert32">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image31.png "image_tooltip")


# Open another terminal

source /opt/ros/foxy/setup.bash

ros2 run demo_nodes_py listener

# Ctrl-C to stop



<p id="gdcalert32" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image32.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert33">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image32.png "image_tooltip")




# Lets try something more fun

ros2 run turtlesim turtlesim_node



<p id="gdcalert33" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image33.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert34">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image33.png "image_tooltip")


# Ctrt-L to stop

atom ~/projects/ros2/dev_ws/src/ros_tutorials/turtlesim/src/turtle_frame.cpp

# Change line #52 to setWindowTitle("MyTurtleSim");



<p id="gdcalert34" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image34.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert35">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image34.png "image_tooltip")


# From the first terminal where we build the source, lets build again since we changed one of the

# source files.

# ucsd@ucsd-ubuntu-vm:~/projects/ros2/dev_ws$ colcon build

colcon build

# Back to the 2nd terminal

ros2 run turtlesim turtlesim_node

# Note the chance on the title of the window


### Rviz (ROS Visualization)

# https://docs.ros.org/en/foxy/Tutorials/dummy-robot-demo.html

# Let’s go to our workspace

cd ~/projects/ros2/dev_ws

# Let’s source our workspace

. install/local_setup.bash

ros2 launch dummy_robot_bringup dummy_robot_bringup.launch.py



<p id="gdcalert35" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image35.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert36">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image35.png "image_tooltip")


# Open another terminal

cd ~/projects/ros2/dev_ws

. install/local_setup.bash

rviz2



<p id="gdcalert36" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image36.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert37">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image36.png "image_tooltip")



### Launch Gazebo

#http://gazebosim.org/tutorials?tut=ros2_installing&cat=connect_ros

source /opt/ros/foxy/setup.bash

gazebo



<p id="gdcalert37" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image37.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert38">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image37.png "image_tooltip")


# Cool, we have a virtual machine with Ubuntu 20.4, Donkey-Sim, DonkeyCar 4.x, ROS2, OpenCV, Jupyter Notebook, and some nice development tools.
