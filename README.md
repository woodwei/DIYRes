## DIY steps and resource needed

In order to speed up the process for readers to reproduce the measurement results of the paper, various resources are provided here, including circuit board files(eagle format), bill of materials, arduino programs and smartphone software. In addition, you can also find a DIY videos on youtube https://www.youtube.com/watch?v=OaiXhgOjj64&t=348s (But that video is rather old, so some content of it is out of date now). Note that the **smartphone software will upload the measurement results to my server after measurement**. If you don’t want this to happen, you can modify the [code](source_of_moniter_app.rar) and compile/build an app by yourself.



#### Circuit Board Files

1. Shield Board File：[CAMOutputs_of_shield](CAMOutputs_of_shield.rar)

2. Probe Board File：[CAMOutputs_of_probebrd](CAMOutputs_of_probebrd.rar)

   

#### Bill of Materials

arduino due

HC02 bluetooth module 

100nF capacitor (SMT package 0603)

mlx90615ssg-dag *6

ph2.0 signal wire (with header on one side) *6

ph2.0 socket *6


2.54mm header (length 13mm)

2.54mm header (length 8mm)

SPI socket

(M3*11+6) copper pillar *4
*

(M3*4+5) copper pillar *4

M3 plastic nuts (used on copper pillar) *4

M3 nuts (used on side panel) *4



#### Arduino Programs needed

1. Communication module setup program

The program can set the serial communication rate of the hc02 bluetooth communication module and the name of the module. After downloading, you can modify the “tcmexp” on the sixth line to the name you want. It should be noted that after the program is executed, the serial communication rate of the Bluetooth module will be changed. If you want to execute this program again, you also need to modify the fourth line of the program to Serial2.begin(115200);

Please right click-select save as to download: [setuphc02](setuphc02.ino)

2. The main program of the measuring instrument

This program is the main program of the measuring instrument, and its functions include:

- Communicate with multiple infrared probes every 6 seconds to obtain the infrared temperature and body surface temperature at the same time.
- In response to the request of the mobile phone, the measurement result buffered in the device is sent to the mobile phone. If the hardware is arduino due, the data can be cached in the device for more than 90 minutes.

Please right click-select save as to download: [mlx90615](mlx90615.ino)

Library file needed: [LibraryUsed](ArduinolibraryUsed.zip)

