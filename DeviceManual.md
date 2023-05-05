### Manual of the measurement device

1. First install the moniter software (link at the bottom of this page) on a mobile phone, then open the file manager in the mobile phone, and create a folder called tcmexp under /sdcard or /storage/emulated/0/. If your mobile phone cannot see /sdcard or /storage/emulated/0/, it is because its security policy is stricter. At this time, you can try to create a tcmexp directory at the root of the mobile phone storage, which should also work. 

2. Turn on the bluetooth of the mobile phone, run the mobile phone software installed in step 1, search for nearby devices, you can find the recorder, connect to the device, enter 1234 when prompted to enter the password. 

3. Wait for a while, the software will prompt that it is connected, and the name of the device will be displayed in the upper left corner, and a curve will appear and scroll to the left continuously. 

4.  Attach multiple probes with white silicone rings and paste them on different fingers. The colors are arranged as follows: the radial side of the thumb-gray, the radial side of the index finger-yellow, the ulnar side of the middle finger-green, the ulnar side of the ring finger- pink, the radial side of the little finger - purple, and the ulnar side of the little finger - black. Be careful not to stick the tape too tightly, otherwise it will hinder the flow of Qi and blood. Then put on gloves (or wrap your hands with clothes, etc.) and start the measurement (be careful not to put your arms and hands under the quilt or be heated by other heat sources such as electric heaters).

5. After the measurement is over, a new file can be seen in the folder created in step 1. This file can be opened and analyzed using the tmrreader software, or the python program drawpng.py. 

   

#### Precautions: 

1. The voltage on four metal contacts on the probe is very low(lower than the electric needle voltage). If it is used with the rubber ring on the fingers, it will not touch the human body. However, if it is used on other parts of the human body, it needs to be insulated (wrapped with a layer of tape), otherwise sensitive people may be allergic. 

2. Be cautious to static electricity in winter, please wear cotton clothes. Before using the device, touch a grounded metal (such as a faucet) to discharge static electricity. 

3.  Since there are many probes and the wires are soft, please try to avoid placing liquid near the device to prevent the probe from being accidentally soaked in the liquid. If it is accidentally soaked, please take it out immediately and turn off the power, and try to use it after leaving it for more than two days. 

4. The measuring instrument needs to be powered by a 9-12V transformer instead of USB (may cause inaccurate measurement data) 

#### Common problem: 

1. The mobile phone software exits as soon as it is started. At this time, it is necessary to check whether there is a tcmexp folder. 

2. The mobile phone cannot find the device or cannot connect. At this time, it should be verified whether the device  is powered on. 

3. The device  can be connected but there is no curve. At this time, you should check whether the yellow light flashes every 6 seconds. If not, try to power on again. 

4. During the measurement, it is found that the mobile phone software disappears. At this time, the mobile phone software can be restarted, and the data during the interruption will not be lost. However, the data will be distributed in multiple files at this time, and subsequent files need to be appended to see the whole curves. 

5. The mobile phone vibrates and reports that the time is reversed. The reason is that the device is powered off and then powered on again. At this time, the mobile phone software needs to be restarted. 

If you have any other questions, please contact me.

------------------------

Note that the **moniter software will upload the measurement results to my server after measurement**. If you don’t want this to happen, you can modify the [code](source_of_moniter_app.rar) and compile/build an App by yourself.

[moniter app](Moniter_auto_upload_to_server.apk) 

[replay app](tmrreader.apk)

[python program to show tmr file](drawpng.py)