<!-----

You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 7

Conversion time: 3.11 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β35
* Thu Apr 25 2024 11:43:48 GMT-0700 (PDT)
* Source doc: Copy of 30-UCSD Robocar Jetson Nano Configuration
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 7.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>
<a href="#gdcalert7">alert7</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



## **UCSD Robocar Jetson Nano Configuration**

Version V5.1 - 18Sep2022

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


	

		


## 


## Table of Contents


[TOC]



## Introduction

The Nvidia Jetson Nano in this document is also referred as JTN

References

[https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

[https://developer.nvidia.com/embedded/downloads](https://developer.nvidia.com/embedded/downloads)

[http://docs.donkeycar.com](http://docs.donkeycar.com)

 

In general for this course if you are using a computer with a Linux distribution like Ubuntu you will have an easier time installing the necessary Artificial Intelligence Framework. Linux uses a file format that is not easily read in an Apple MacOS or MS Windows computer.  If you need to modify files in the uSD card formatted for Linux, e.g., a disk partition that uses Ext4 format, you should ask a colleague first if they have a Linux PC, then Tutors or TA for help.

Every Team is expected to try installing the necessary software based on these instructions using the uSD image, not the recovery image.  And every member of the team needs to participate during the lab embedded linux hands-on exercise. The same SBC (JTN) can be used at the class by several users without the need to connect a monitor and a keyboard to it. It is part of your learning in the course to get familiar with Embedded Linux, Head-Less Single Board Computers (SBC) like the JTN, terminal running in a PC, SSH, and remotely installing software in a SBC.

If you run out of time, based on instructor’s set deliverables, or your uSD card gets corrupted, you can use the recovery uSD card image that has all the software pre-installed. On the there is a link to a recovery uSD card image.


## 


## Flashing Micro SD Card for the Jetson 

From your PC let's prepare (flash) the micro SD card (uSD card). Make sure your computer can access the Internet. If you are using one of our WiFi Access Points in one of the labs, or at one of the tracks, the first device that connects to the WiFi Access point and try to access the Internet, will need to accept the UCSD Wireless Visitor Agreement, just like when you are connecting to UCSD’s Visitor WiFi. In fact you are basically connecting to the Internet via the UCSD’s Visitor WiFi. 


### Software Installation

Etcher can use Zipped files, you don’t need to Unzip the image file if you are using Etcher. Ignore if your Windows or Mac computer tells you it can not ready the uSD card. The uSD card will be used on the JTN running Linux. It uses a file format that Windows and Mac don’t know about unless you use specialized software to do that. You don’t need it. If you are using Linux or MacOS command lines to write the disk image to a uSD card, you may need to extract the file first.

**Download the UCSD’s Jetson Nano Developer Kit SD Card Image [from here](https://drive.google.com/file/d/1Ikdat_BaP3IqEYoYfjfMQJGgmAC-UGNK/view?usp=sharing)**

Install Etcher to be able to write the disk image to a uSD Card [here](https://www.balena.io/etcher/)

Using the image we are providing as a starting point has some advantages with some pre-configuration. For example, it won't require a monitor and a keyboard connected to the JTN to get you started.


### Writing an Image to Micro SD Card

Connect  a microSD (uSD) adapter to your PC.



1. Insert the provided uSD card (64 gigabytes) into the uSD adapter.
2. Install and run Etcher.
3. Start Etcher, choose the Zipped file with the Disk Image you downloaded, pay attention when choosing the drive with the uSD card on it (e.g., 64 gigabytes).
4. Write the image to uSD card.
5. Eject the uSD card from your PC first using the procedure for your PC Operating System (e.g., eject drive) 
6. Then insert the uSD card into the JTN uSD card slot. Note this is a push-in-to-lock and push-in-to-unlock the uSD card. Please do not pull the uSD card out of the slot before unlocking it, 

    otherwise you may damage your JTN and or uSD card.



## 


## Powering on the Jetson

The preferable way to power the JTN is with the provided 5V 4A power supply; it has a barrel connector that plugs into the JTN. You need to place a jumper connector at J48, there is a text label close to it that says

ADD JUMPER TO DISABLE USB PWR. 

For the initial configuration you don’t have to use the 5V 4A power supply. If you are not using the provided power supply for the initial configuration, you need to remove the jumper located above the JNT power connectors to allow it to be powered by the uUSB cable. Please save the jumper. You can leave it in place connected to one of the pins of J48.

Power on the JTN by connecting the power supply to a power outlet and the barrel jack into the barrel port on the Jetson. 

**Note: Give the Jetson a minute or two to boot and load its software and the fan may not work until you install the software later in these instructions.**


## 


## Wired Communication with Jetson

We will use the command line to access the Jetson Nano (JTN) using a secure shell (SSH). Don’t worry, if you are not familiar with terminals and using command lines, you will master it in this class. Mastering these will be a good skill to have and another mention in your resume.

The Linux OS running on the JTN enables two protocols of communication: **Serial Communication** and **SSH. **Both use a local network interface with TCP/IP over the USB cable. By using a micro USB cable between the JTN and the PC, you can communicate with the JTN. On the PC, you need to use software to enable serial communication or SSH. e.g., Serial Communication - screen on Linux or MacOS. CoolTerm is another option that runs on Linux, MacOS, and MS Windows. SSH is natively supported on Linux and MacOS. MS Windows 10 or later supports SSH too.

**Note: Your JTN should have a WiFi / Bluetooth network interface and antennas already installed on it. If not, please contact the Tutors or TAs.**


### SSH Communication (via USB Connection)

Connect a uUSB cable between the JTN and your PC.


```
ssh jetson@192.168.55.1
or
ssh jetson@ucsdrobocar-xxx-yy.local
```


The default UserID is jetson and password is jetsonucsd (all lower case)

Username: jetson

Password: jetsonucsd


### Serial Communication 

If needed install a software called screen on your host or virtual Linux computer and/or update it


```
sudo apt-get install screen
sudo apt-get update screen
```


Or you can install coolterm, or use any terminal emulator software you have. On my computer the JTN plugged in using the uUSB cable shows up as /dev/ttyACM1. Log-in info when doing a serial connection is the same as the SSH connection

The command line in a terminal to connect to it in Linux is


```
screen /dev/ttyACM1
```



## 


## Wireless Communication with Jetson

After connecting to the JTN via USB connection, let's configure the JTN to connect to a WiFi Access Point. Using SSH via USB connection or using the serial communication software log into the JTN.

Let’s make sure the network service is running


```
sudo systemctl start networking.service
```



### Accessing WiFi Networks

List the available WiFi networks


```
sudo nmcli device wifi list
```


If the WiFi Access point that you want to connect is not initially listed try rescan to refresh the list. If after several tries the network still does not show, try rebooting.


```
sudo nmcli device wifi rescan
```


(If needed) `sudo reboot now`


### Connecting to a WiFi network

We have bridged WiFi access points. Try to stay in the 5GHz network.

Here is the command to connect he JTN to an access point


```
sudo nmcli device wifi connect <ssid_name> password <password>
```


Here are the WiFi access points we use

   ssid="UCSDRoboCar5GHz"

   password="UCSDrobocars2018"

   ssid="UCSDRoboCar"

   password="UCSDrobocars2018"

   ssid="SD-DIYRoboCar5GHz" 

   password="SDrobocars2017"

   ssid="SD-DIYRoboCar"

   password="SDrobocars2017"



examples:

5GHz


```
sudo nmcli device wifi connect UCSDRoboCar5GHz password UCSDrobocars2018
```


2.4GHz


```
sudo nmcli device wifi connect UCSDRoboCar password UCSDrobocars2018

sudo nmcli device wifi connect UCSDRoboCar password UCSDrobocars2018
```




<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")



### Get IP Address of Jetson

After connecting the JTN to a WiFi Access Point, let's find out the IP address the JTN is getting

from the network so we can connect to it remotely. 

To get IP address of the JTN


```
ifconfig
```




<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")


**Note: To connect to a new Access Point you may have to repeat these steps using a uUSB cable connected between your PC and the JTN **

**Note: You can add your phone as an Access Point so you always have a backup connection to your JTN. If you have your phone with you, you can connect to the JTN and then add another WiFi using SSH.**

In the example above this JTN’s IP address is 192.168.222.167. Now that we have the JTN connected to WiFi and have its IP address, we can now do wireless communication with the JTN with SSH via WiFi connection. 


### SSH Communication (via WiFi Connection)

Connect your PC to the JTN using WiFi (using example IP address from above) then enter the password


```
ssh jetson@192.168.222.167
```


Username: jetson

Password: jetsonucsd


### Update WiFi Power Settings

Lets turn-off the power saving for the WiFi device

If your SSH connection is slow, lagging, make sure you have the power saving on the WiFi disabled


```
sudo iw dev wlan0 set power_save off
```


Lets install a small text editor called nano


```
sudo apt-get update
sudo apt-get install nano
```


 

Lets make the change on the WiFi power saving settings persistent. We need to edit a file. 


```
sudo nano /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
```


change 

wifi.powersave = 3

to

wifi.powersave =** 2**


## 


## System Settings

Now lets change the name of the JTN (host name) and password of the JTN. We will configure the name of the JTN based on your Class xxx and Team yy. Hostname ucsdrobocar-xxx-yy where xxx-yy is your class and team number, ex: 148-05, 190-01,190-TA1, 190-TA2

Example: ucsdrobocar-148-05 for Team 5

See current computer information


```
hostnamectl
```




<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")



### Changing Host name

Replace xxx-yy with class number and team number


```
sudo hostnamectl set-hostname ucsdrobocar-xxx-yy
```


There is one more place to change the hostname


```
sudo nano /etc/hosts
```




<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.png "image_tooltip")


change jetson or any other name it may have for your JTN name

ex: 127.0.1.1       ucsdrobocar-xxx-yy

Press Ctr-X (^X) to save the file


### Changing Password

Lets change the JTN user jetson password


```
passwd
```


Lets reboot the JTN to make sure all settings were saved

sudo reboot now


### Setting Date and Time

Hint. In the case the clock on the JTN is not updating automatically by getting information 

from the Internet, you need to set the date and time manually or updates and software installs may fail

Again, if updates are failing, please check and adjust the date/time before asking for help.

Check that the date and time is correct at the JTN and install ntp to auto-update date and time


```
date
```


Manually Setting Date and Time


```
sudo date -s '2019-07-03 09:30:00'
```


Let's set the time zone. Ex: US/Pacific,  Los Angeles


```
sudo dpkg-reconfigure tzdata
```


If the date and time are not updating automatically after the JTN is connected to the Internet

These should force a clock synchronization


```
sudo apt-get update
sudo apt-get install ntp
sudo /etc/init.d/ntp stop
```


`sudo ntpd -q -g \
sudo /etc/init.d/ntp start` \


Reboot to check if the date / times are updating correctly 


```
sudo reboot now
```


if the time is not updating, you can force a time update with


```
sudo ntpd -q -g
```



### 


### GUI Settings

If you are running your SBC only using a remote terminal and no graphical user interface, you can disable it to save you some hardware resources. Optional settings when you don’t need the Graphical User Interface on the JTN. Once you have configured your JTN to connect to a WiFi Access Point, there is no need to have the GUI enabled until you need some kind of remote desktop access. Let’s disable it. You can always revert if needed. These steps will save on CPU cycles and save lots of megabytes of RAM.

**Note: when using Intel RealSense cameras, LIDAR, and other ROS sensors, you may need to leave the GUI (X Server running) for troubleshooting. **

To disable GUI (X Server) on boot


```
sudo systemctl enable multi-user.target
sudo systemctl set-default multi-user.target
```


Let's say you want to use a computer monitor attached to the JTN

To re-enable GUI issue the command:


```
sudo systemctl set-default graphical.target
```


or

To start a GUI  session on a system without a current GUI just execute:


```
sudo systemctl start gdm3.service
```


To stop the GUI


```
sudo systemctl stop gdm3.service
```


Lets reboot to make sure the GUI (X Server) is not loading


```
sudo reboot now
```



### Cleaning up

Lets remove some packages that we don't use

Ubuntu crash reporting


```
sudo apt purge whoopsie
sudo apt purge apport
```



    to enable it


```
    sudo apt install apport
    sudo systemctl start apport
```



    set to 1 in /etc/default/apport


```
    sudo nano /etc/default/apport
```


Ubuntu modem management


```
sudo apt purge modemmanager
```


Ubuntu Unattended Upgrades


```
sudo apt purge unattended-upgrades
```


Lets update the software already installed in the JTN


```
sudo apt-get update
sudo apt-get upgrade
```


It may take a while depending on how many of the installed software needs to be updated/upgraded

**Do not upgrade to Ubuntu 20.04**

If some packages are no longer in use, the following packages were automatically installed and are no longer required:


```
sudo apt autoremove
```


If you see warning of packages being kept back on the upgrade


```
sudo apt-get --with-new-pkgs upgrade
```


Reboot the JTN


```
sudo reboot now
```



        Skip creating a swap file. Keeping this note here for reference.


        The new OS already has a swap file created by default 


        Lets add a swap so larger software can be compiled and installed


        [https://www.jetsonhacks.com/2019/04/14/jetson-nano-use-more-memory/](https://www.jetsonhacks.com/2019/04/14/jetson-nano-use-more-memory/)


```
        cd ~/projects
        git clone https://github.com/jetsonhacksnano/installSwapfile
        cd installSwapfile
        ./installSwapfile.sh
        sudo reboot now
```



## Fan 


### Physical Installation

If it has not been done already, install the fan on the JTN using the provided M3x16 screws, note the fan orientation. The fan sticker is facing up. The fan power connector is keyed, pay attention when connecting it. Look for a connector at the JTN labeled Fan close to the Ethernet connector.


### Activating Fan

At this point you should have your JTN powered with the provided power supply 5V 4A. We will need this to power the fan.


#### Install Software

While in an SSH session on the JTN, enter the following commands


```
mkdir projects
cd projects
git clone https://github.com/Pyrestone/jetson-fan-ctl.git
sudo apt-get update
sudo apt install python3-dev
cd ~/projects/jetson-fan-ctl
./install.sh
```



#### As Needed Customize Fan Settings

open /etc/automagic-fan/config.json with your favorite editor (I'm using nano):


```
sudo nano /etc/automagic-fan/config.json
```


Check status of the fan and if the JTN is running at high power (10W / high clock) 


```
sudo service automagic-fan status
```


Type CTRL-C if you are stuck on the fan/power status

At this point you should see the fan at the JTN spinning.

Lets try a reboot and see if the fan starts automatically after the JTN boots


```
sudo reboot now
```



## NVCC

Let's make sure nvcc is working - CUDA

[https://devtalk.nvidia.com/default/topic/1048926/jetson-nano/unable-to-install-cuda-on-jetson-nano-help-/](https://devtalk.nvidia.com/default/topic/1048926/jetson-nano/unable-to-install-cuda-on-jetson-nano-help-/)


```
nvcc -V
```


you should see something like this

nvcc: NVIDIA (R) Cuda compiler driver

Copyright (c) 2005-2019 NVIDIA Corporation

Built on Mon_Mar_11_22:13:24_CDT_2019

Cuda compilation tools, release 10.0, V10.0.326

If not, then type these lines and try the command again or modify the .bashrc file to include these lines below


```
sudo nano ~/.bashrc
```


Then add these lines to the end of the file

export PATH=${PATH}:/usr/local/cuda/bin

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/cuda/lib64

Then source the .bashrc file and try the nvcc command again


```
source ~/.bashrc
nvcc -V
```


Expected output similar to:

nvcc: NVIDIA (R) Cuda compiler driver

Copyright (c) 2005-2021 NVIDIA Corporation

Built on Sun_Feb_28_22:34:44_PST_2021

Cuda compilation tools, release 10.2, V10.2.300

Build cuda_10.2_r440.TC440_70.29663091_0


## 


## Backup of the uSD Card

Once you have finished the configuration of your SBC, why not make a backup of the uSD card to save you time during a recovery process? You will only need to write the backup image back to the uSD card. Backup the uSD card following these steps in a Linux machine


### Using a Linux Machine

Eject the uSD card from your SBC, plug it into a linux PC using a uSD adapter


```
sudo fdisk -l
```


Expected output:

Disk /dev/sda: 59.6 GiB, 64021856256 bytes, 125042688 sectors

Units: sectors of 1 * 512 = 512 bytes

Sector size (logical/physical): 512 bytes / 512 bytes

I/O size (minimum/optimal): 512 bytes / 512 bytes

Disklabel type: gpt

Disk identifier: D048AD43-24FD-4DED-B06E-7BB8ED98158C

Device     Start       End   Sectors  Size Type

/dev/sda1  24576 125042654 125018079 59.6G Linux filesystem

/dev/sda2   2048      2303       256  128K Linux filesystem

/dev/sda3   4096      4991       896  448K Linux filesystem

/dev/sda4   6144      7295      1152  576K Linux filesystem

/dev/sda5   8192      8319       128   64K Linux filesystem

/dev/sda6  10240     10623       384  192K Linux filesystem

/dev/sda7  12288     13439      1152  576K Linux filesystem

/dev/sda8  14336     14463       128   64K Linux filesystem

/dev/sda9  16384     17663      1280  640K Linux filesystem

/dev/sda10 18432     19327       896  448K Linux filesystem

/dev/sda11 20480     20735       256  128K Linux filesystem

/dev/sda12 22528     22687       160   80K Linux filesystem

In my case, the 64G uSD was mounted on /dev/sda

example on the command line for making an image of the uSD card mounted on Linux machines as /dev/sda


```
sudo dd bs=4M if=/dev/sda of=ucsd_robocar_image_25sep19.img status=progress
```


Lets compress the image using Zip


```
zip ucsd_robocar_image_25sep19.zip ucsd_robocar_image_25sep19.img
```



### 


### Using a Mac Machine

Eject the uSD card from your SBC, plug it into a linux PC using a uSD adapter


```
diskutil list
```


Expected output:

/dev/disk6 (external, physical):


<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: Definition &darr;&darr; outside of definition list. Missing preceding term(s)? </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


   :                       TYPE NAME                    SIZE       IDENTIFIER

   0:      GUID_partition_scheme                        *128.0 GB   disk6

   1:           Linux Filesystem                         127.6 GB   disk6s1

   2:           Linux Filesystem                         67.1 MB    disk6s2

   3:           Linux Filesystem                         67.1 MB    disk6s3

   4:           Linux Filesystem                         458.8 KB   disk6s4

   5:           Linux Filesystem                         458.8 KB   disk6s5

   6:           Linux Filesystem                         66.1 MB    disk6s6

   7:           Linux Filesystem                         524.3 KB   disk6s7

   8:           Linux Filesystem                         262.1 KB   disk6s8

   9:           Linux Filesystem                         262.1 KB   disk6s9

  10:           Linux Filesystem                         104.9 MB   disk6s10

  11:           Linux Filesystem                         134.2 MB   disk6s11

example on the command line for making an image of the uSD card mounted on /dev/disk6


```
sudo dd if=/dev/disk6 of=ucsdrobocar-xxx-yy-v1.0.img
```



### Using a Windows Machine

Once you open Win32 Disk Imager, use the blue folder icon to choose the location and the name of the backup you want to take, and then choose the drive letter for your SD card. Click on the Read button. The card will then be backed up to your PC. [Example of uSD backup on Windows](https://thepihut.com/blogs/raspberry-pi-tutorials/17789160-backing-up-and-restoring-your-raspberry-pis-sd-card#:~:text=Using%20Windows&text=Once%20you%20open%20Win32%20Disk,backed%20up%20to%20your%20PC.)

**END of Jetson Nano (JTN) configuration**


## Optional Configurations


### Enable SSH Connection Without Typing the Password

Generate the Private and Public Keys

Exchange Security Keys

At the PC


```
cd ~
sudo apt-get install rsync
ssh-keygen -t rsa
```


ubuntu


```
cat .ssh/id_rsa.pub
```


mac


```
cat ~/.ssh/id_rsa.pub
```


Copy the output of the command into the buffer (Ctrl-C or Command-C on a Mac)

At the single board computer (SBC) running Linux


```
cd ~
mkdir .ssh
```


> mkdir: cannot create directory ‘.ssh’: File exists


```
chmod 700 .ssh
sudo chown jetson:jetson .ssh
nano .ssh/authorized_keys
```



### Firewall

Install a firewall management app.


```
sudo apt-get install gufw
```


Then using the GUI look for the Firewall App.

For advanced experimental users

Jetson Nano with Ubuntu 20.04 - [https://github.com/Qengineering/Jetson-Nano-Ubuntu-20-image](https://github.com/Qengineering/Jetson-Nano-Ubuntu-20-image)
