
## Setup the can:  
Setup PCI Connection to prbt
current IP adress: 169.254.60.100
In order to check it you are connected:
$ ping 169.254.60.100

Setup USB Ethernet connection to the RPi Router, which is the IP configured for the RET socket server   
current IP Address: 10.4.11.132.    
In order to check it you are connected:   
$ ping 10.4.11.132

Create connection via  CAN:
$ sudo ip link set can0 up type can bitrate 1000000 

after every reset of the Robot you should turn it off:
$ sudo ip link set can0 down
and up again.

Note: For the current Pilz Setup, The Computer has to be connected before it robot starts otherwise the connection will fail. If you connect the Robot to the PC after the Robot ist already starten then you need to reset the robot and start the can again!

## Launch Moveit + Rviz + Button Masher Application (BMA):
Ensure the RET Socket server is already running, since the BMA tries to connect to it first. Then launch:

$ source devel/setup.bash
$ roslaunch pilz_manipulation ret_pilz_ROS.launch
