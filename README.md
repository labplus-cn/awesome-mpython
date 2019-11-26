# mPython 精选资源

<img src="https://raw.githubusercontent.com/labplus-cn/awesome-mpython/master/docs/images/mpython_ico_en.png"  width="350" /><img src="https://raw.githubusercontent.com/labplus-cn/awesome-mpython/master/docs/images/micropython.png"  width="350" />

 设立[aswsome-mpython](https://labplus-cn.github.io/awesome-mpython/)网页项目初衷,旨在收集、归纳<kbd>掌控板</kbd>和<kbd>MicroPython</kbd>的一些网络上的资源。提供学习指南，库，软件和资源供<kbd>掌控板</kbd>和<kbd>MicroPython</kbd>爱好者学习！

`mPython`是`MicroPython`基础上的分支，旨在简化低成本微控制器上的实验和教学。它不需要预先安装Python环境或桌面软件，因此比以往更加轻松地上手。使用`mPython`，您可以编写简洁的Python代码来控制硬件，而不必使用复杂的底层语言（例如C或C ++）（Arduino用于编程的语言）。对初学者来说很棒！


## 精选驱动库

### 说明

<img src="https://img.icons8.com/office/40/000000/error.png"></br>

- 由于MicroPython与mPython会存在细微区别,并不一定完全能在mPython上运行。同时我们也会标识出哪些驱动可在mPython上正常运行。
- 对应一些需要二次修改才能使用的驱动或经典的驱动,我们将会收收纳至<kbd>[awesome-mpython/library](https://github.com/labplus-cn/awesome-mpython/tree/master/library)</kbd>。

图标说明:

- <img src="https://img.icons8.com/plasticine/30/000000/guarantee.png">: 经验证可在掌控板上正常使用
- <img src="https://img.icons8.com/cotton/30/000000/add-to-collection--v2.png">: 收纳入awesome-mpython/library


### 传感器


* [ADXL345-with-Pyboard](https://github.com/AbhinayBandaru/ADXL345-with-Pyboard) - ADXL345 16g 3轴加速度计
* [adxl345_micropython](https://github.com/fanday/adxl345_micropython) - ADXL345 16g 3轴加速度计
* [micropython-lis2hh12](https://github.com/tuupola/micropython-lis2hh12) - LIS2HH12 3轴加速度计
* [MMA7660](https://github.com/Bucknalla/MicroPython-3-Axis-Accelerometer/blob/master/MMA7660.py) - MMA7660 1.5g 3轴加速度计

* [CCS811](https://github.com/Ledbelly2142/CCS811) - CCS811 空气质量传感器
* [upython-aq-monitor](https://github.com/ayoy/upython-aq-monitor) - PMS5003 颗粒物浓度传感器
* [micropython-bme280](https://github.com/kevbu/micropython-bme280) - Bosch BME280 气象传感器(温度/湿度/气压)
* [mpy_bme280_esp8266](https://github.com/catdog2/mpy_bme280_esp8266) - Bosch BME280 气象传感器(温度/湿度/气压)
* [wipy_bme280](https://bitbucket.org/oscarBravo/wipy_bme280) - Bosch BME280 气象传感器(温度/湿度/气压)
* [micropython-bmp180](https://github.com/micropython-IMU/micropython-bmp180) - Bosch BMP180 气象传感器(温度/气压/海拔)
* [micropython-ov2640](https://github.com/namato/micropython-ov2640) - MicroPython class for OV2640 camera.
* [micropython-esp8266-hmc5883l](https://github.com/gvalkov/micropython-esp8266-hmc5883l) - 3轴数字指南针
* [pyb_ina219](https://github.com/chrisb2/pyb_ina219) - INA219 电压/电流传感器
* [micropython-gp2y0e03](https://bitbucket.org/thesheep/micropython-gp2y0e03) - Sharp GP2Y0E03 红外测距传感器
* [micropython-vl53l0x](https://bitbucket.org/thesheep/micropython-vl53l0x) - VL53L0X Time-of-Flight 激光测距模块
* [micropython-vl6180](https://bitbucket.org/thesheep/micropython-vl6180) - vl6180近距离感测器(光学测距/环境光线)
* [micropython-hcsr04](https://github.com/rsc1975/micropython-hcsr04) - HC-SR04/05 超声波测距  <img src="https://img.icons8.com/plasticine/30/000000/guarantee.png">  <img src="https://img.icons8.com/cotton/30/000000/add-to-collection--v2.png">
* [ATM90E26_Micropython](https://github.com/whatnick/ATM90E26_Micropython) -ATM90E26 功率测量
* [micropython-MQ](https://github.com/kartun83/micropython-MQ) - MQ系列烟雾传感器
* [MQ135](https://github.com/rubfi/MQ135) - MQ135 烟雾传感器
* [MicroPython-SI1145](https://github.com/neliogodoi/MicroPython-SI1145) - SI1145 光线传感器(紫外光/可见光/红外光)
* [micropython-tsl2561](https://github.com/kfricke/micropython-tsl2561) - TSL2561 数字光强传感器
* [mpy_bh1750fvi_esp8266](https://github.com/catdog2/mpy_bh1750fvi_esp8266) - BH1750FVI 数字光强传感器
* [micropython-bmx055](https://github.com/micropython-IMU/micropython-bmx055) - Driver for Bosch BMX055 IMU sensor.
* [micropython-bno055](https://github.com/deshipu/micropython-bno055) - Bosch Sensortec BNO055 9DOF IMU sensor, I2C interface.
* [micropython-lsm9ds0](https://github.com/micropython-IMU/micropython-lsm9ds0) - LSM9DS0 g-force linear acceleration, gauss magnetic and dps angular rate sensors.
* [micropython-mpu9250](https://github.com/tuupola/micropython-mpu9250) - I2C driver for MPU9250 9-axis motion tracking device.
* [micropython-mpu9x50](https://github.com/micropython-IMU/micropython-mpu9x50) - Driver for the InvenSense MPU9250 inertial measurement unit.
* [MPU6050-ESP8266-MicroPython](https://github.com/adamjezek98/MPU6050-ESP8266-MicroPython) - ESP8266 driver for MPU6050 accelerometer/gyroscope.
* [py-mpu6050](https://github.com/larsks/py-mpu6050) - ESP8266 driver for MPU6050 accelerometer/gyroscope.

* [micropython-chirp](https://github.com/robberwick/micropython-chirp) - Driver for the Chirp Soil Moisture Sensor.
* [micropython-max31855](https://bitbucket.org/thesheep/micropython-max31855) - Thermocouple amplifier, SPI interface.
* [max31856](https://github.com/alinbaltaru/max31856) - Precision thermocouple to digital converter with linearization, SPI interface.
* [bme680-mqtt-micropython](https://github.com/robmarkcole/bme680-mqtt-micropython) - Driver for BME680 gas, pressure, temperature and humidity sensor.
* [LM75-MicroPython](https://github.com/OldhamMade/LM75-MicroPython) - Driver for LM75 digital temperature sensor, I2C interface.
* [micropython-am2320](https://github.com/mcauser/micropython-am2320) - Aosong AM2320 temperature and humidity sensor, I2C interface.
* [micropython-dht12](https://github.com/mcauser/micropython-dht12) - Aosong DHT12 temperature and humidity sensor, I2C interface.
* [micropython-hdc1008](https://github.com/kfricke/micropython-hdc1008) - Driver for the Texas Instruments HDC1008 humidity and temperature sensor.
* [micropython-mcp9808](https://github.com/kfricke/micropython-mcp9808) - Driver for the Microchip MCP9808 temperature sensor.
* [micropython-mpl115a2](https://github.com/khoulihan/micropython-mpl115a2) - Pyboard driver for the MPL115A2 barometric pressure sensor.
* [micropython-sht30](https://github.com/rsc1975/micropython-sht30) - Driver for SHT30 temperature and humidity sensor.
* [micropython-sht31](https://github.com/kfricke/micropython-sht31) - Driver for the SHT31 temperature and humidity sensor.
* [micropython-Si7005](https://github.com/Smrtokvitek/micropython-Si7005) - Driver for Si7005 relative humidity and temperature sensor.
* [micropython-si7021](https://bitbucket.org/thesheep/micropython-si7021) - SI7021 Temperature and humidity sensor, I2C interface.
* [micropython-si7021](https://github.com/chrisbalmer/micropython-si7021) - SI7021 Temperature and humidity sensor, I2C interface.
* [micropython-Si705x](https://github.com/billyrayvalentine/micropython-Si705x) - Silicon Labs Si705x series of temperature sensors, I2C interface.
* [micropython-Si70xx](https://github.com/billyrayvalentine/micropython-Si70xx) - Silicon Labs Si70xx series of relative humidity and temperature sensors, I2C interface.
* [micropython-tmp102](https://github.com/khoulihan/micropython-tmp102) - Driver for TMP102 digital temperature sensor.
* [SHT10_uPython](https://github.com/Omgitskillah/SHT10_uPython) - Driver for SHT10 temperature and humidity sensor.
* [sht25-micropython](https://github.com/Miceuz/sht25-micropython) - Driver for SHT25 temperature and humidity sensor.
* [micropython-mlx90614](https://github.com/mcauser/micropython-mlx90614) - Driver for Melexis MLX90614 IR temperature sensor.
* [micropython-mpr121](https://github.com/mcauser/micropython-mpr121) - Driver for MPR121 capacitive touch keypads and breakout boards.
* [micropython-ttp223](https://github.com/mcauser/micropython-ttp223) - Examples using TTP223 capacitive touch module.
* [XPT2046-touch-pad-driver-for-PyBoard](https://github.com/robert-hh/XPT2046-touch-pad-driver-for-PyBoard) - Driver for XPT2046 touch pad controller used in many TFT modules.
* [micropython-nunchuck](https://github.com/kfricke/micropython-nunchuck) - Driver for Nunchuk game controller, I2C interface.

### 输出类

* [micropython-adafruit-pca9685](https://github.com/adafruit/micropython-adafruit-pca9685) - 16-channel 12-bit PWM/servo driver.
* [micropython-pca9685](https://bitbucket.org/thesheep/micropython-pca9685) - 16-channel 12-bit PWM/servo driver.
* [L298N](https://github.com/GuyCarver/MicroPython/blob/master/lib/L298N.py) - Driver for the L298N dual h-bridge motor controller.
* [micropython-upybbot](https://github.com/jeffmer/micropython-upybbot) - A4988 driver for bipolar stepper motors.
* [JQ6500](https://github.com/rdagger/micropython-jq6500) - JQ6500 UART MP3 模块的驱动
* [KT403A-MP3](https://github.com/jczic/KT403A-MP3) - Driver for KT403A, used by DFPlayer Mini and Grove MP3 v2.0.
* [micropython-buzzer](https://github.com/fruch/micropython-buzzer) - Play nokia compose and mid files on buzzers.
* [micropython-dfplayer](https://github.com/ShrimpingIt/micropython-dfplayer) - Driver for DFPlayer Mini using UART.
* [micropython-longwave](https://github.com/MattMatic/micropython-longwave) - WAV player for MicroPython board.


### 显示类


* LCD

    * [micropython-epaper](https://github.com/peterhinch/micropython-epaper) - Pyboard driver for Embedded Artists 2.7 inch e-paper display.
    * [micropython-ili9341](https://bitbucket.org/thesheep/micropython-ili9341) - SSD1606 active matrix epaper display 128x180.
    * [micropython-waveshare-epaper](https://github.com/mcauser/micropython-waveshare-epaper) - Drivers for various Waveshare e-paper modules.

    * [Grove_RGB_LCD](https://github.com/dda/MicroPython/blob/master/Grove_RGB_LCD.py) - Driver for SeeedStudio's Grove RGB LCD.
    * [lcdi2c](https://github.com/slothyrulez/lcdi2c) - Driver for HD44780 compatible dot matrix LCDs.
    * [micropython-charlcd](https://github.com/rdagger/micropython-charlcd) - Driver for HD44780 compatible LCDs.
    * [micropython-i2c-lcd](https://github.com/Bucknalla/micropython-i2c-lcd) - Driver for I2C 2x16 LCD Screens.
    * [micropython_grove_rgb_lcd_driver](https://github.com/KidVizious/micropython_grove_rgb_lcd_driver) - Driver for SeeedStudio's Grove RGB LCD.
    * [pyboard-LCD-character-display](https://github.com/scitoast/pyboard-LCD-character-display) - PyBoard driver for HDD44780 compatible 1602  LCDs.
    * [python_lcd](https://github.com/dhylands/python_lcd) - Driver for HD44780 compatible dot matrix LCDs.

    * [micropython-lcd-AQM1248A](https://github.com/forester3/micropython-lcd-AQM1248A) - ESP8266 driver for AQM1248A graphic LCD.
    * [micropython-lcd160cr-gui](https://github.com/peterhinch/micropython-lcd160cr-gui) - Simple touch driven event based GUI for the Pyboard and LCD160CR colour display.
    * [micropython-pcd8544](https://github.com/mcauser/micropython-pcd8544) - Driver for Nokia 5110 PCD8544 84x48 LCD modules.
    * [micropython-st7565](https://github.com/nquest/micropython-st7565) - Driver for ST7565 128x64 LCDs.
    * [micropython-st7920](https://github.com/ShrimpingIt/micropython-st7920) - Library for simple graphic primitives on ST7920 128x64 monochrome LCD panel using ESP8266 and SPI.
    * [MicroPython_PCD8544](https://github.com/AnthonyKNorman/MicroPython_PCD8544) - ESP8266 driver for Nokia 5110 PCD8544.
    * [Official LCD160CR](https://github.com/micropython/micropython/tree/master/drivers/display) - Driver for official MicroPython LCD160CR display with resistive touch sensor.


    * [micropython-ili9341](https://bitbucket.org/thesheep/micropython-ili9341) - Collection of drivers for TFT displays, ILI9341, SH1106, SSD1606, ST7735.
    * [micropython-ili934x](https://github.com/tuupola/micropython-ili934x) - SPI driver for ILI934X series based TFT / LCD displays.
    * [MicroPython-ST7735](https://github.com/boochow/MicroPython-ST7735) - ESP32 version of GuyCarvers's ST7735 TFT LCD driver.
    * [micropython-st7735](https://github.com/hosaka/micropython-st7735) - Driver for ST7735 TFT LCDs.
    * [MicroPython_ST7735](https://github.com/AnthonyKNorman/MicroPython_ST7735) - Driver for ST7735 128x128 TFT.
    * [SSD1963-TFT-Library-for-PyBoard](https://github.com/robert-hh/SSD1963-TFT-Library-for-PyBoard) - Driver for SSD1963 864x480 TFT LCDs.
    * [ST7735](https://github.com/GuyCarver/MicroPython/blob/master/lib/ST7735.py) - Driver for ST7735 TFT LCDs.


* led matrix

    * [micropython-ht1632c](https://github.com/vrialland/micropython-ht1632c) - Driver for HT1632C 32x16 bicolor led matrix.
    * [micropython-matrix8x8](https://github.com/JanBednarik/micropython-matrix8x8) - Driver for AdaFruit 8x8 LED Matrix display with HT16K33 backpack.
    * [micropython-max7219](https://github.com/mcauser/micropython-max7219) - Driver for MAX7219 8x8 LED matrix modules.
    * [micropython-wemos-led-matrix-shield](https://github.com/mactijn/micropython-wemos-led-matrix-shield) - Driver for Wemos D1 Mini Matrix LED shield, using TM1640 chip.
    * [micropython-wemos-led-matrix](https://github.com/mattytrentini/micropython-wemos-led-matrix) - Driver for Wemos D1 Mini Matrix LED shield, using TM1640 chip.


* 数码管
    * [LKM1638](https://github.com/arikb/LKM1638) - Driver for JY-LKM1638 displays based on TM1638 controller.
    * [max7219_8digit](https://github.com/pdwerryhouse/max7219_8digit) - Driver for MAX7219 8-digit 7-segment LED modules.
    * [micropython-max7219](https://github.com/JulienBacquart/micropython-max7219) - Driver for MAX7219 8-digit 7-segment LED modules.
    * [micropython-my9221](https://github.com/mcauser/micropython-my9221) - Driver for MY9221 10-segment LED bar graph modules.
    * [micropython-tm1637](https://github.com/mcauser/micropython-tm1637) - Driver for TM1637 quad 7-segment LED modules.
    * [micropython-tm1638](https://github.com/mcauser/micropython-tm1638) - Driver for TM1638 dual quad 7-segment LED modules with switches.
    * [micropython-tm1640](https://github.com/mcauser/micropython-tm1640) - Driver for TM1740 8x8 LED matrix modules.

* 灯带
    * [micropython-morsecode](https://github.com/mampersat/micropython-morsecode) - Blink an LED with morse coded message.
    * [micropython-p9813](https://github.com/mcauser/micropython-p9813) - Driver for P9813 RGB LED used in SeeedStudio's Grove Chainable RGB LED.
    * [micropython-ws2812-7seg](https://github.com/HubertD/micropython-ws2812-7seg) - 7-segment display using WS2812 RGB LEDs.
    * [micropython-ws2812](https://github.com/JanBednarik/micropython-ws2812) - Driver for WS2812 RGB LEDs.
    * [Official APA102](http://docs.micropython.org/en/latest/esp8266/quickref.html#apa102-driver) - ESP8266 APA102/DotStar RGB LED driver.
    * [Official WS2811](http://docs.micropython.org/en/latest/esp8266/quickref.html#neopixel-driver) - ESP8266 WS2811/NeoPixel RGB LED driver.
    * [tlc5940-micropython](https://github.com/oysols/tlc5940-micropython) - Driver for TLC5940 16 channel LED driver.
    * [ledstrip](https://github.com/labplus-cn/awesome-mpython/tree/master/library/ledstrip) -  micropython neopixel module的增强版.

* OLED
    * [Grove_OLED](https://github.com/dda/MicroPython/blob/master/Grove_OLED.py) - Driver for SSD1327 used by SeeedStudio's Grove OLED Display 1.12" v1.0.
    * [micropython-oled](https://bitbucket.org/thesheep/micropython-oled) - Collection of drivers for monochrome OLED displays, PCD8544, SH1106, SSD1306, UC1701X.
    * [micropython-ssd1327](https://github.com/mcauser/micropython-ssd1327) - Driver for SSD1327 128x128 4-bit greyscale OLED displays.
    * [micropython-ssd1351](https://github.com/rdagger/micropython-ssd1351) - Driver for SSD1351 OLED displays.
    * [MicroPython_SSD1306](https://github.com/AnthonyKNorman/MicroPython_SSD1306) - ESP8266 driver for SSD1306 OLED 128x64 displays.
    * [Official SSD1306](https://github.com/micropython/micropython/tree/master/drivers/display) - Driver for SSD1306 128x64 OLED displays.
    * [SH1106](https://github.com/robert-hh/SH1106) - 

### 通讯类


* [PyBoard-HC05-Android](https://github.com/KipCrossing/PyBoard-HC05-Android) - Pyboard HC05 Bluetooth adaptor example application.
* [Official wiznet5k](https://github.com/micropython/micropython/tree/master/drivers/wiznet5k) - Official driver for the WIZnet5x00 series of Ethernet controllers.
* [micropyGPS](https://github.com/inmcm/micropyGPS) - Full featured GPS NMEA sentence parser.
* [micropython-gnssl76l](https://github.com/tuupola/micropython-gnssl76l) - MicroPython I2C driver for Quectel GNSS L76-L (GPS).
</br>
</br>
* 红外
    * [micropython-necir](https://github.com/MattMatic/micropython-necir) - NEC infrared capture for TL1838 IR receiver LEDs.
    * [Micropython-IR](https://github.com/designerPing/Micropython-IR) - Pyboard infrared remote sniff and replay.
    * [IR Remote](https://github.com/labplus-cn/awesome-mpython/tree/master/library/ir_remote) - 红外编解码(NEC)的驱动  <img src="https://img.icons8.com/plasticine/30/000000/guarantee.png">  <img src="https://img.icons8.com/cotton/30/000000/add-to-collection--v2.png">
</br>
</br>

* [Official OneWire](https://github.com/micropython/micropython/tree/master/drivers/onewire) - For devices using the OneWire bus, eg Dallas ds18x20.


* [micropython-radio](https://github.com/peterhinch/micropython-radio) - Protocols for nRF24L01 2.4Ghz radio modules.
* [micropython-rfsocket](https://github.com/wuub/micropython-rfsocket) - Micropython implementation of popular 433MHzn based RFSockets.
* [Official nRF24L01](https://github.com/micropython/micropython/tree/master/drivers/nrf24l01) - Official driver for nRF24L01 2.4Ghz radio modules.

* [micropython-mfrc522](https://github.com/wendlers/micropython-mfrc522) - Driver for NXP MFRC522 RFID reader/writer.
* [micropython-wiegand](https://github.com/pjz/micropython-wiegand) - Wiegand protocol reader.

* [micropython-tinyrtc-i2c](https://github.com/mcauser/micropython-tinyrtc-i2c) - Driver for DS1307 RTC and AT24C32N EEPROM.
* [Micropython_TinyRTC](https://github.com/AnthonyKNorman/Micropython_TinyRTC) - Driver for DS1307 RTC.

* [HueBridge](https://github.com/FRC4564/HueBridge) - Philips Hue Bridge.

### 功能类


* [ads1x15](https://github.com/robert-hh/ads1x15) - Driver for the ADS1015/ADS1115 ADC, I2C interface.
* [micropython-ads1015](https://bitbucket.org/thesheep/micropython-ads1015) - ADS1015 12-Bit and ADS1115 16-bit ADC, 4 channels with programmable gain, I2C interface.
* [Micropython_ADS1115](https://github.com/AnthonyKNorman/Micropython_ADS1115) - ADS1115 16-bit ADC, 4 channels with programmable gain, I2C interface.
* [micropython-mcp4725](https://github.com/wayoda/micropython-mcp4725) - Driver for the MCP4725 I2C DAC.
* [MCP23017-ESP8266-Miniature-Driver](https://github.com/forkachild/MCP23017-ESP8266-Miniature-Driver) - Driver for MCP23017 16-bit I/O Expander.
* [micropython-mcp230xx](https://github.com/ShrimpingIt/micropython-mcp230xx) - Driver for MCP23017 and MCP23008 GPIO expanders.
* [Micropython-AD9833](https://github.com/KipCrossing/Micropython-AD9833) - Pyboard driver for AD9833, spi interface.
* [microbit](https://github.com/labplus-cn/awesome-mpython/tree/master/library/microbit) - 掌控板兼容MicroBit  <img src="https://img.icons8.com/plasticine/30/000000/guarantee.png">  <img src="https://img.icons8.com/cotton/30/000000/add-to-collection--v2.png">
* [ivPID](https://github.com/labplus-cn/awesome-mpython/tree/master/library/ivPID) - PID控制器  <img src="https://img.icons8.com/plasticine/30/000000/guarantee.png">  <img src="https://img.icons8.com/cotton/30/000000/add-to-collection--v2.png">




### 网络类

* [urllib.parse](https://github.com/labplus-cn/awesome-mpython/tree/master/library/urllib) -  URL编码 (MicroPython-lib@urllib.parse精简版)   <img src="https://img.icons8.com/plasticine/30/000000/guarantee.png">  <img src="https://img.icons8.com/cotton/30/000000/add-to-collection--v2.png">
* [bigiot](https://github.com/labplus-cn/awesome-mpython/tree/master/library/bigiot) -  贝壳物联  <img src="https://img.icons8.com/plasticine/30/000000/guarantee.png">  <img src="https://img.icons8.com/cotton/30/000000/add-to-collection--v2.png">
* [yeelight](https://github.com/labplus-cn/awesome-mpython/tree/master/library/yeelight) -  YeeLight  <img src="https://img.icons8.com/plasticine/30/000000/guarantee.png">  <img src="https://img.icons8.com/cotton/30/000000/add-to-collection--v2.png">
* [qqai](https://github.com/labplus-cn/awesome-mpython/tree/master/library/qqai) -  [腾讯AI开放平台](https://ai.qq.com/)  <img src="https://img.icons8.com/plasticine/30/000000/guarantee.png">  <img src="https://img.icons8.com/cotton/30/000000/add-to-collection--v2.png">


------------------------------

## 软件

## 社区

## 贡献

始终欢迎您提供意见和建议！请提出请求以修改Awesome mPython。

- 维护者:[tangliufeng](https://github.com/tangliufeng)
- 共享者:


## 许可证
由[tangliufeng@LabPlus](https://github.com/tangliufeng)编译和维护。