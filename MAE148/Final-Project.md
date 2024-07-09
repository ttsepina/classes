# Final Project Documentation

## Docker Rquirements (Low Level Later)

* OpenCV > ~ 4.5.0 (trying 4.8.1; 4.9.0 seems to require L4T>36)
* Ros 2 foxy 
    * include gps node, apriltag, etc.

### Dockerfile Intersections
#### ucsd_robocar

The base image - has ros2_foxy as a parent (which has ubuntu:focal as a parent; this one might eat those ones).

Issues include: 
* OpenCV is version 4.2.0
* includes things we didn't use in the course
    * ros1/bridge
    * adafruit twist node
    *

#### Jetson / Dusty Depot


#### ros2 foxy


#### ubuntu 20.04

## Cannot implement OpenCV update to system - will try to move forward with IMU data

## IMU Orientation Determination

In order to get the relative orientation of the car and the cart, need to use IMU to get angular position data. The p1 IMU has the ability to measure the yaw angle relative to East (bearing of the car). Since it uses the same node as the GPS, should be much simpler to implement, especially with ROS2. 

In order to get the car to back up into the cart once they are both facing the correct directions (they would likely need to be placed inline - cannot search for cart), we can use the position of the cart in the frame of the camera to tell the car to back up (the vertical coordinate should be below a given value - similar to line following)


## ROS2 Master Node

The Master node takes in the state of the cart (hitched or not hitched). Once it reads that the cart is hitched (after calling for it to begin rotating), it will move on from that state to check the GPS position and await a goal location. Once a start and goal are assigned, the node will compute the path between them and assign velocity commands to the vesc_twist() node to guide the car to the goal while avoiding obstacles present in the workspace. Once it reaches the goal, the car will actuate the delivery mechanism based on what package is being delivered.   

Use feedback from action to get car to back up.




## Workspace Configuration

We defined a Python class `Workspace()` that takes in a list of the coordinates of the exterior boundary of the navigable space, a dictionary containing lists of coordnates for the corners of obstacles withing that space, a start location, and a goal location.
This class generates a path and the coordinates of each node along it by dividing the navigable space into triangles and connecting their centroids in a visibility graph. From the starting node, nodes are rated by their distance to the goal node, 

