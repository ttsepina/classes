<!-- Copy and paste the converted output. -->

<!-----

You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 37

Conversion time: 12.097 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β35
* Thu Apr 25 2024 12:14:05 GMT-0700 (PDT)
* Source doc: Copy of 15 - VESC Setup Instructions
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



## UCSD VESC Setup Instructions

Version 2.0 - 30Dec2022

The instructions below are for different versions for the VESC, pay attention on what you

have. Choosing the incorrect version of a VESC when you update the firmware may damage

the VESC.

We will use a software called VESC Tool to upgrade the firmware in the VESC and

also to measure parameters from the Brushless DC (BLDC) motors sensored or not.

Place the robot on the class provided stand. The wheels of the robot should be clear to spin

Place the robot on the class provided stand. The wheels of the robot should be clear to spin

Place the robot on the class provided stand. The wheels of the robot should be clear to spin

Place the robot on the class provided stand. The wheels of the robot should be clear to spin

**No, this was not a typo repeating the same txt. Place the robot on the class provided stand. The wheels of the robot should be clear to spin. **

You need to power the VESC with the same battery you plan to use on your robot.

You need a longer uUSB cable, or a USB extension cable, to connect the VESC to your host

PC so your host PC. Talk to the instructor if you need a longer uSD cable than the one

provided at the class.

If the VESC is connected to your SBC, disconnect it and connect to the Host PC using a uSD

cable.

Be careful so your host PC or other parts are not in contact with the wheels of the robot; they will spin. 

Let’s all use the same VESC tools and the related firmware version to minimize differences between the robots used in  the class. [Please get the VESC tools from here](https://drive.google.com/drive/folders/1m_gqcIWwaCzV3y3raU1FFiEpCyf3rYPi?usp=sharing).

Unless you are not using the class provided VESC Tools, Ignore if you get a warning to get the latest VESC version.



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


Connect the LiPO battery alarm to the battery 

Connect the provided RC Car battery to the VESC and a uUSB cable between the VESC and your computer.

Click on the VESC tools connect icon



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")


or 



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")


Note: when you connect the VESC to the VESC Tools below, it may warn you that you have a

newer version on the VESC.

For VESC 6.x be free to go ahead and upgrade the firmware to the latest. For VESCs V4.x, e.g., V4.2, do not upgrade the firmware. You will use an older version of the VESC tools that has special firmware for VESC 4.x. 



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")




<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")




<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.png "image_tooltip")




<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image7.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image7.png "image_tooltip")




<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image8.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image8.png "image_tooltip")




<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image9.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image9.png "image_tooltip")


Yes

DO NOT DISCONNECT THE POWER NOR the UCSD CABLE from the VESC during the firmware update.

You will most likely damage the VESC if you do.



<p id="gdcalert10" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image10.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert11">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image10.png "image_tooltip")


As of 30Dec22

The version of firmware we are using is

6.00



<p id="gdcalert11" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image11.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert12">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image11.png "image_tooltip")


VESC Hardware V6.x ex: see this on the VESC Tools when connected 

<p id="gdcalert12" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image12.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert13">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image12.png "image_tooltip")


VESC Edu will see Hw:EDU

Original VESCs 6.x    

Original VESCs Edu

FLIPSKY - FSESC 6.6

FLIPSKY - FSESC 6.7

Let’s play safe and disconnect the power and uUSB cable from the VESC

Remove the power from the VESC by disconnecting the battery

Connect the BLDC motor to the VESC

Connect the motor sensor cables to the VESC

Connect the servo motor used for steering to the VESC

Connect the LiPO battery alarm to the battery

Connect your host computer to the VESC using a USB cable

Connect the battery to the VESC

Start the VESC Tool on your host computer

Using the VESC Tools, connect to the VESC



<p id="gdcalert13" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image13.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert14">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image13.png "image_tooltip")


You can test the Steering Servo here



<p id="gdcalert14" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image14.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert15">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image14.png "image_tooltip")




<p id="gdcalert15" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image15.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert16">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image15.png "image_tooltip")



#### Motor Detection

Once more

Place the robot on the class provided stand. The wheels of the robot should be clear to spin

Place the robot on the class provided stand. The wheels of the robot should be clear to spin

Place the robot on the class provided stand. The wheels of the robot should be clear to spin

Place the robot on the class provided stand. The wheels of the robot should be clear to spin



<p id="gdcalert16" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image16.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert17">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image16.png "image_tooltip")




<p id="gdcalert17" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image17.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert18">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image17.png "image_tooltip")




<p id="gdcalert18" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image18.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert19">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image18.png "image_tooltip")


YES…



<p id="gdcalert19" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image19.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert20">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image19.png "image_tooltip")




<p id="gdcalert20" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image20.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert21">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image20.png "image_tooltip")


# Note: As a good engineer, check the number of poles you have on your motor ex: 4

# Then on the VESC Tools, use that number of poles on your wizard 

# How, see the part number so some search on the web

# Ex: XeRun 3660 G2 sensored motor [https://www.hobbywingdirect.com/products/xerun-3660-g2-sensored-motor](https://www.hobbywingdirect.com/products/xerun-3660-g2-sensored-motor)


    “innovative **4-pole-8-magnet** "staggered pole" rotor (Hobbywing-patented) with low cogging effect and torque pulsation greatly improves control feel around corners.”



<p id="gdcalert21" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image21.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert22">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image21.png "image_tooltip")


How many Cells in your battery?

3, 4, ?, ??

At UCSD we mostly use 3C for ECE MAE 148 and 4C for DSC178 and our racing robots



<p id="gdcalert22" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image22.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert23">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image22.png "image_tooltip")


# What else? Number poles? Do some research.

Your robot should spin the wheels forward then a bit backward.

If it moved backwards than forward, you need to reverser (REV) on the option below)

&lt;Battery_TYPE_LIION…>

**<span style="text-decoration:underline;">PLEASE CHECK WHAT KIND OF BATTERY YOU HAVE, GENERALLY:</span>**

3 CELL - 3AH BATTERIES

4 CELL - 4AH BATTERIES

Battery Cells Series

**&lt;3>**

Battery Capacity

**&lt;3.000 Ah>**



<p id="gdcalert23" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image23.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert24">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image23.png "image_tooltip")


&lt;Next>

&lt;Direct Drive>

Wheel Diameter 

&lt;100.00 mm>

&lt;Run Detection>

**Last chance, is your robot over the stand and all the wheels clear to spring?**

**Are you sure?**

If yes, proceed, if not then make the wheels clear of any contact.



<p id="gdcalert24" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image24.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert25">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image24.png "image_tooltip")


Write the Motor configuration



<p id="gdcalert25" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image25.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert26">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image25.png "image_tooltip")


Write the App configuration



<p id="gdcalert26" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image26.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert27">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image26.png "image_tooltip")



#### Sensor Detection

Let’s check what the wizard did for us so we make sure the sensors are being detected on our motors



<p id="gdcalert27" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image27.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert28">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image27.png "image_tooltip")




<p id="gdcalert28" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image28.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert29">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image28.png "image_tooltip")




<p id="gdcalert29" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image29.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert30">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image29.png "image_tooltip")




<p id="gdcalert30" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image30.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert31">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image30.png "image_tooltip")




<p id="gdcalert31" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image31.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert32">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image31.png "image_tooltip")




<p id="gdcalert32" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image32.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert33">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image32.png "image_tooltip")


Example



<p id="gdcalert33" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image33.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert34">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image33.png "image_tooltip")




<p id="gdcalert34" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image34.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert35">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image34.png "image_tooltip")



#### Enable Servo Control For Steering

Now lets enable to use the VESC PWM (SERVO) cable as output to control a servo motor for steering of our robot



<p id="gdcalert35" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image35.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert36">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image35.png "image_tooltip")




<p id="gdcalert36" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image36.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert37">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image36.png "image_tooltip")


Write the App Configuration


#### 

<p id="gdcalert37" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image37.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert38">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image37.png "image_tooltip")



#### As of Fall 2022 we are migrating to the original VESC 6 edu version

So follow VESC6 above.

This is for the previous VESCs older than HW6.x


#### VESC Hardware V4.12 **(again if you have V6, follow the instructions above)**

**If you are using a VESC6 compatible device, skip this. VESC6 instructions are above**

**FLIPSKY - MINI FSESC4.2 **

 ===========================================

Note: With the new VESCs 6.x and VESC 6 edu you can skip this. They support the new version of firmware already

We will use a special firmware that allows the VESC to use its PWM connection, normally

used as input to the VESC as an output to power and control the servo motor we use for

steering our scale autonomous cars. Unfortunately, the latest versions of VESC Tools are not

providing the firmware that has the servo out - vesc_servoout.bin.

[Here is where you can get the VESC Tools we will use](https://drive.google.com/drive/folders/1eJoHYFSpNcAuC_M24GmvPr4kfRsdm-JV?usp=sharing). We will use VESC 2.03, which has by

 default firmware version 4.2.

============================================

Pre built VESC Tools

[https://github.com/rpasichnyk/vesc_tool/releases](https://github.com/rpasichnyk/vesc_tool/releases)

[https://github.com/rpasichnyk/vesc_tool/releases/tag/v2.03](https://github.com/rpasichnyk/vesc_tool/releases/tag/v2.03)

 [&lt; US$60](https://usa.banggood.com/Flipsky-Mini-FSESC4_20-50A-ESC-Based-Upon-VESC-With-Aluminum-Anodized-Heat-Sink-for-Rc-Car-p-1349277.html?gmcCountry=US&currency=USD&createTmp=1&utm_source=googleshopping&utm_medium=cpc_bgcs&utm_content=frank&utm_campaign=pla-usg-all-pc&gclid=Cj0KCQjwhZr1BRCLARIsALjRVQPrRBs7amfJo5-W6YBpE0tvqMeuQsGOokNCAJ-hOQ4p_G_cjhfIMs8aAldxEALw_wcB&cur_warehouse=CN) VESC (Flipsky Mini). It looks well built. Surprisingly good for the cost. We will see the

 long term use. You can get the same unit[ more expensive](https://flipsky.net/products/mini-fsesc4-20-50a-base-on-vesc-widely-used-in-eskateboard-escooter-ebike) from the manufacturer, go figure.

[https://f1tenth.readthedocs.io/en/latest/getting_started/driving/drive_manual.html](https://f1tenth.readthedocs.io/en/latest/getting_started/driving/drive_manual.html)

I am using the less expensive VESC compatible. I can get them for less than US60 from

China vs. hundred of dollars of the VESC 6.

Need to use a firmware version for hardware V4.12  

[https://github.com/RacecarJ/vesc-firmware](https://github.com/RacecarJ/vesc-firmware)  

[https://github.com/RacecarJ/vesc-firmware/tree/master/firm](https://github.com/RacecarJ/vesc-firmware/tree/master/firmware)

At this point I am using the latest VESC Tool V2.03 that supplies the latest firmware V4.2 that

has the firmware VESC_servoout.bin. As of 28Apr20, the latest VESC Tool is 2.05.  It has

firmware 5.1. I don’t see vesc_servoout.bin there.

I had a copy of VESC Tool V2.03. I uploaded firmware V4.2 VESC_servoout.bin to the FESC

4.2 (HW 4.12). The BLDC sensored motor was detected without problems.

Then follow the detection of the motor as in the VESC 6.x
