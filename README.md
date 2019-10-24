# Arduino optical shutters for free space optical experiments

This is an Arduino project dedicated to automate three home made optical shutters (light caches mounted on a DC motor) used in free space optical experiments. The Arduino board is controlled by a python driver script running on a computer, through a serial (USB) connection.

![](shutters.gif)

This repository contains both the microprogram to flash on the Arduino, and the python driver based on the Python library pyvisa.

## Elements:
- 1x [Arduino Uno Rev 3](https://store.arduino.cc/arduino-uno-rev3) 
![alt text](https://store-cdn.arduino.cc/uni/catalog/product/cache/1/image/500x375/f8876a31b63532bbba4e781c30024a0a/a/0/a000066_iso_3.jpg)
- 3x [Parallax Standard Servo](https://www.parallax.com/product/900-00005)
![alt text](https://www.parallax.com/sites/default/files/styles/mid-sized-product/public/900-00005.png)
- Wires

## Wiring diagram:

![alt text](scheme.png)

![alt text](photo.jpg = 250x)


## Python driver:

You first need to set in the driver the attribute `POS` that contains the reference angles of each servo for their ON and OFF states. Test different angles with the functions `setAngleShutter<NUM>`.

Once this is done, you can use the functions `setShutter<NUM>` to enable or disable a shutter.

``` python
arduino = Driver('ASRL::2::INSTR')
arduino.shutter1.set_state(True)        # Enable shutter 1
arduino.shutter2.set_state(False)       # Disable shutter 2
arduino.shutter3.invert()               # Invert state of shutter 3
arduino.set_global_config('1x0')        # Enable shutter 1, don't move shutter 2, disable shutter 3
arduino.safe_state()                    # Enable every shutters
```
