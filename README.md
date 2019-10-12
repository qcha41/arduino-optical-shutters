# Arduino optical shutters for free space optical experiments

This is an Arduino project dedicated to automate three home made optical shutters (light caches mounted on a DC motor) used in free space optical experiments. The Arduino board is controlled by a python driver script running on a computer, through a serial (USB) connection.

![](shutters.gif)

This repository contains both the arduino microprogram, and the python driver.

Elements:
- 1x [Arduino Uno Rev 3](https://store.arduino.cc/arduino-uno-rev3) 
![alt text](https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/500x375/f8876a31b63532bbba4e781c30024a0a/a/0/a000066_iso_3.jpg)
- 3x [Parallax Standard Servo](https://www.parallax.com/product/900-00005)
![alt text](https://www.parallax.com/sites/default/files/styles/mid-sized-product/public/900-00005.png)
- Wires

Scheme:

![alt text](scheme.png)
