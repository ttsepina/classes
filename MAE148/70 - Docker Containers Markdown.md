<!-----

You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 1

Conversion time: 1.562 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β35
* Thu Apr 25 2024 12:18:53 GMT-0700 (PDT)
* Source doc: Copy of 70 - Docker Containers
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 1.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



## Docker Containers


### Version 0.4 15Jan2024

# ***** Not Ready to be user by students  yet *****

# Great quick introduction from Jim from JetsonHacks

# Please watch the short video

[https://jetsonhacks.com/2023/09/04/use-these-jetson-docker-containers-tutorial/](https://jetsonhacks.com/2023/09/04/use-these-jetson-docker-containers-tutorial/)

# From NVIDIA

[https://developer.nvidia.com/embedded/learn/tutorials/jetson-container](https://developer.nvidia.com/embedded/learn/tutorials/jetson-container)

“


## What is a container?

A [container](https://developer.nvidia.com/ai-hpc-containers) is an executable unit of software where an application and its run time dependencies can all be packaged together into one entity. Since everything needed by the application is packaged with the application itself, containers provide a degree of isolation from the host and make it easy to deploy and install the application without having to worry about the host environment and application dependencies.


## What is Docker?

Docker is an open source platform for creating, deploying, and running containers. Docker is included in JetPack, so running containers on Jetson is easy and does not require any installation.


## What is NGC?

NVIDIA NGC is a hub for GPU-optimized deep learning, machine learning, and high-performance computing (HPC) software. NGC hosts containers for the top AI and data science software-- all tuned, tested and optimized by NVIDIA. Containers on NGC provide powerful and easy-to-deploy software proven to deliver fast results, allowing users to build solutions from a tested framework.

Visit NGC portal for more information at [https://www.nvidia.com/en-us/gpu-cloud/](https://www.nvidia.com/en-us/gpu-cloud/).


## Jetson Containers on NGC

Several containers for Jetson are hosted on NVIDIA NGC. Visit the [Jetson cloud-native page](https://developer.nvidia.com/embedded/jetson-cloud-native) on the list of containers for Jetson hosted on NGC.

“

[https://github.com/dusty-nv/jetson-containers](https://github.com/dusty-nv/jetson-containers)



# First, consider installing tmux, it will help you reconnect a SSH session without losing

#  where you were, for example when your computer goes to sleep.

# [https://formulae.brew.sh/formula/tmux](https://formulae.brew.sh/formula/tmux)


    Example configuration has been installed to:


      /opt/homebrew/opt/tmux/share/tmux


    ==> Summary


    🍺  /opt/homebrew/Cellar/tmux/3.3a_3: 9 files, 1.1MB


    ==> Running `brew cleanup tmux`...


    Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.


    Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).


    ==> Caveats


    ==> tmux


    Example configuration has been installed to:


      /opt/homebrew/opt/tmux/share/tmux

[https://jeongwhanchoi.medium.com/install-tmux-on-osx-and-basics-commands-for-beginners-be22520fd95e](https://jeongwhanchoi.medium.com/install-tmux-on-osx-and-basics-commands-for-beginners-be22520fd95e)

# [https://gist.github.com/simme/1297707](https://gist.github.com/simme/1297707)


    To start Tmux just run the following command:


    tmux


    You can create a new session using the command  below:


    tmux new-session -s &lt;your_session_name>


    To view available sessions, enter the following command:


    tmux list-sessions


    Run the command below to detach from your session when you are done:


    tmux detach


    And to reattach to your Tmux session when you are ready to continue working using the following command:


    tmux attach -t &lt;your_session_name>


    Here are some of the usual shortcuts to use Tmux:


    –> Ctrl-b ?: Show all commands


    –> Ctrl+b c: Create a new window


    –> Ctrl-b o: Switch


    –> Ctrl+b arrow key: Switch pane


    –> Ctrl+b “: Split horizontally


    –> Ctrl+b %: Split vertically


    –> Ctrl+b n: Next


    –> Ctrl+b p: Previous

# example

tmux new-session -s jack-agx01

tmux list-sessions

tmux detach

tmux list-sessions

tmux attach -t jack-agx01

exit



# Let’s do some setup for docker at the Jetson

cd projects

sudo apt-get update && sudo apt-get install git python3-pip

git clone --depth=1 https://github.com/dusty-nv/jetson-containers

cd jetson-containers

pip3 install -r requirements.txt

sudo nano /etc/docker/daemon.json

{

    "runtimes": {

        "nvidia": {

            "path": "nvidia-container-runtime",

            "runtimeArgs": []

        }

    },

    "default-runtime": "nvidia"

}

sudo systemctl restart docker

# Let’s confirm we have a swap file as large as our RAM \
free -h


                  total        used        free      shared  buff/cache   available


    Mem:           14Gi       1.2Gi        12Gi        28Mi       1.1Gi        13Gi


    Swap:         7.3Gi          0B       7.3Gi

# For the AGX, we have 16G RAM,  we need 16G of swap. In this case it had 8G RAM

# Using jtop

4MEM

# press + until you get the amount of swap you want, in my case another 8G for Jetson Xavier

# AGX

# Then press S

s



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


free -h

total        used        free      shared  buff/cache   available

Mem:           14Gi       1.2Gi        12Gi        28Mi       1.1Gi        13Gi

Swap:          15Gi          0B        15Gi

sudo usermod -aG docker $USER

“

Then close/restart your terminal (or logout) and you should be able to run docker commands (like docker info) without needing sudo.

“

exit

# SSH into the Jetson again

docker info


     Client:


     Version:    24.0.5


     Context:    default


     Debug Mode: false


    Server:


    …

# Let's have the docker data directory moved to a place easy to find. This is specially useful if

# you have external storage with larger capacity and or a faster media such as another 

# larger SSD drive

# [https://github.com/dusty-nv/jetson-containers/blob/master/docs/setup.md](https://github.com/dusty-nv/jetson-containers/blob/master/docs/setup.md)

cd ~/projects

mkdir docker

sudo cp -r /var/lib/docker ~/projects/docker

sudo nano /etc/docker/daemon.json

{

    "runtimes": {

        "nvidia": {

            "path": "nvidia-container-runtime",

            "runtimeArgs": []

        }

    },

    "default-runtime": "nvidia",

    "data-root": "/home/jetson/projects/docker"

}

sudo systemctl restart docker

# or you can reboot your jetson

# sudo reboot now



# Let’s build out a container image for Jack’s class:

# DonkeyCar and ROS2

#

# We will need the following packages

# OpenCV CUDA

# Tensorflow (including TensorRT)

#  Moises Lopez has done a great job developing scripts to build

# DockerContainer

# We already have a docker image that you can use with DonkeyCar, OpenCV, ROS2 installed

[https://github.com/UCSD-ECEMAE-148/donkeycontainer](https://github.com/UCSD-ECEMAE-148/donkeycontainer)


## # To use the UCSD ECE MAE 148 Docker Image

docker pull ghcr.io/ucsd-ecemae-148/donkeycontainer:devel

# This will take a while. Think about it, we are downloading lots of software.  It takes time to get 

# it from the Internet and  using embedded low power computers. You can see that the CPU

# core(s) are busy by running another terminal to the Jetson and running jtop

# Let’s create a file/script to start the ecemae148 container that has DonkeyCar, ROS, 

#and ROS2 

cd ~/projects

echo docker run \

--name donkey \

-it \

--rm \

--privileged \

--net=host \

-e DISPLAY=$DISPLAY \

-v /dev/bus/usb:/dev/bus/usb \

--device /dev/video0 \

--volume='/dev/input:/dev/input' \

--volume='/home/jetson/.Xauthority:/root/.Xauthority:rw' \

--volume='/tmp/.X11-unix/:/tmp/.X11-unix' \

--volume='/home/jetson/projects/donkeycar:/home/projects/donkeycar' \

--volume='/home/jetson/projects/ucsd_robocar2:/home/projects/ros2_ws/src' \

--volume='/home/jetson/projects/ucsd_robocar1:/home/projects/ros1_ws/src' \

ghcr.io/ucsd-ecemae-148/donkeycontainer:devel >> ucsd-ecemae148-donkey-ros2.sh

# Let’s list the file

more ucsd-ecemae148-donkey-ros2.sh

# Let’s run the container called ucsd-ecemae148-donkey-ros2

sh ./ucsd-ecemae148-donkey-ros2.sh

# Running the container

sh ./ucsd-ecemae148-donkey-ros2.sh

Docker_Container@jack-agx01:/home/projects🦝

source_donkey

(donkey) Docker_Container@jack-agx01:/home/projects/mycar



___________________________________


    # previous version that did not name the container to be ecemae148 


    # and did not have a donkeycar directory


            echo docker run \


            --name donkey \


            -it \


            --rm \


            --privileged \


            --net=host \


            -e DISPLAY=$DISPLAY \


            -v /dev/bus/usb:/dev/bus/usb \


            --device /dev/video0 \


            --volume='/dev/input:/dev/input' \


            --volume='/home/jetson/.Xauthority:/root/.Xauthority:rw' \


            --volume='/tmp/.X11-unix/:/tmp/.X11-unix' \


            --volume='/home/jetson/projects/mycar:/home/projects/mycar' \


            --volume='/home/jetson/projects/ucsd_robocar2:/home/projects/ros2_ws/src' \


            --volume='/home/jetson/projects/ucsd_robocar1:/home/projects/ros1_ws/src' \


        ghcr.io/ucsd-ecemae-148/donkeycontainer:devel >> run.sh


        Git clone  [https://github.com/UCSD-ECEMAE-148/donkeycontainer](https://github.com/UCSD-ECEMAE-148/donkeycontainer)


        sh ./build.sh


```
    This command will save a file name run.sh on the current directory,  a Docker container with the image 'ghcr.io/ucsd-ecemae-148/donkeycontainer:devel' will spin up using the Nvidia Docker runtime. The purpose of the container is to run a project related to a self-driving car.

            Here's a breakdown of the different options used in the 'nvidia-docker run' command:

               - '--name donkey': sets the name of the container to 'donkey'.
               - '-it': starts an interactive terminal within the container.
               - '--rm': removes the container automatically when it exits.
               - '--privileged': gives the container full access to the host system's devices.
               - '--net=host': shares the host system's network stack with the container.
               - '-e DISPLAY=$DISPLAY': sets the 'DISPLAY' environment variable to allow the container to display graphical applications on the host system.
               - '-v /dev/bus/usb:/dev/bus/usb': shares the host system's USB bus with the container.
               - '--device-cgroup-rule='\''c 189:* rmw'\''': sets the device cgroup rule for '/dev/nvhost-ctrl' to allow read, write, and mknod permissions for the container.
               - '--device /dev/video0': shares the host system's first video device with the container.
               - '--volume=''/dev/input:/dev/input'': shares the host system's input devices with the container.
               - '--volume=''/home/jetson/.Xauthority:/root/.Xauthority:rw'': shares the host system's X authentication file with the container.
               - '--volume=''/tmp/.X11-unix/:/tmp/.X11-unix'': shares the host system's X11 socket with the container.
               - '--volume=''/home/jetson/projects/mycar:/home/projects/mycar'': shares the host system's 'mycar' project directory with the container.
               - '--volume=''/home/jetson/projects/ucsd_robocar2:/home/projects/ros2_ws/src'': shares the host system's 'ucsd_robocar2' directory with the container.
               - '--volume=''/home/jetson/projects/ucsd_robocar1:/home/projects/ros1_ws/src'': shares the host system's 'ucsd_robocar1' directory with the container.

            Finally, the 'ghcr.io/ucsd-ecemae-148/donkeycontainer:devel' specifies the image to use for the container, which is pulled from the Github Container Registry (ghcr.io) and tagged with 'devel'.
```



        # sh ./run.sh

___________________________________



# To build the containers using the NVIDIA’s packages

“

See the <code>[packages](https://github.com/dusty-nv/jetson-containers/blob/master/packages)</code> directory for the full list, including pre-built container images and CI/CD status for JetPack/L4T.

Using the included tools, you can easily combine packages together for building your own containers. Want to run ROS2 with PyTorch and Transformers? No problem - just do the [system setup](https://github.com/dusty-nv/jetson-containers/blob/master/docs/setup.md), and build it on your Jetson like this:


```
# $ ./build.sh --name=my_container pytorch transformers ros:humble-desktop
```


There are shortcuts for running containers too - this will pull or build a <code>[l4t-pytorch](https://github.com/dusty-nv/jetson-containers/blob/master/packages/l4t/l4t-pytorch)</code> image that's compatible:


```
#$ ./run.sh $(./autotag l4t-pytorch)
```


“

# Jack’s Todo- check tmux for SSH reconnect

Moisés López to Everyone (Jan 15, 2024, 09:29)

docker run \

       --name donkey \

       -it \

       --rm \

       --privileged \

       --net=host \

       -e DISPLAY=$DISPLAY \

       -v /dev/bus/usb:/dev/bus/usb \

       --device /dev/video0 \

       --volume='/dev/input:/dev/input' \

       --volume='/home/jetson/.Xauthority:/root/.Xauthority:rw' \

       --volume='/tmp/.X11-unix/:/tmp/.X11-unix' \

       --volume='/home/jetson/projects/mycar:/home/projects/mycar' \

       --volume='/home/jetson/projects/ucsd_robocar2:/home/projects/ros2_ws/src' \

       --volume='/home/jetson/projects/ucsd_robocar1:/home/projects/ros1_ws/src' \

       ghcr.io/ucsd-ecemae-148/donkeycontainer:devel

 

Moisés López to Everyone (Jan 15, 2024, 09:35)

donkey createcar --template=path_follow --path .

 

Moisés López to Everyone (Jan 15, 2024, 09:43)

https://docs.linuxserver.io/images/docker-webtop/


## # Docker Commands

# To list all the docker image you have at the Jetson

docker images

# To delete unused docker images

docker system prune -a

# Delete all images

docker system prune -a



# MacOS

[https://docs.docker.com/desktop/install/mac-install/](https://docs.docker.com/desktop/install/mac-install/)

# Homebrew

[https://brew.sh/](https://brew.sh/)

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

eval "$(/opt/homebrew/bin/brew shellenv)"

# Git Client MacOS

https://git-scm.com/downloads

[https://git-scm.com/download/mac](https://git-scm.com/download/mac)

# Install Git

brew install git
