<img width="400" src="/images/mpython.png"/> <img width="400" src="/images/yeelight.png"/>

## 概述

`yeelight` 是掌控板或micropython驱动库，用于控制局域网内的YeeLight智能灯泡/小米智能灯具设备。

## 库的安装方法

可通过以下任一方法进行安装。
1. 将项目中的`yeelight.py` 
2. 在掌控板REPL界面中，使用upip安装，步骤如下：
    * 前置条件需要掌控板连接网络
    * 导入upip模块，执行`import upip`
    * 执行`upip.install('mPython-yeelight'）

```python
>>> import upip
>>> upip.install('mPython-yeelight')
```

## 使用

准备工作：

* YeeLight智能灯泡在使用前，须要先配置好连接好wifi，并将 `局域网控制` 功能打开。
* 掌控板确保已与智能灯泡在同个局域网内，并网络通畅。

yeelight Library Documentation：https://mpython-lib.readthedocs.io    </br>

YeeLight第三方控制协议：https://www.yeelight.com/download/Yeelight_Inter-Operation_Spec.pdf

## 简单示例

```python
from mpython import *
from yeelight import *

my_wifi = wifi()                    # 连接到与YeeLight相同的局域网内
my_wifi.connectWiFi("","")          


discover_bulbs()        # 发现局域网内YeeLight的设备信息

bulb=Bulb("192.168.0.7")    # 构建Bulb类用于控制，传入IP参数

bulb.turn_on()              # 开灯
sleep(2)
bulb.turn_off()             # 关灯
sleep(2)
bulb.toggle()               # 翻转
sleep(2)
bulb.set_rgb(255,0,0)       # 设置RGB值
bulb.set_brightness(50)     # 调节亮度
sleep(2)
bulb.set_hsv(180,100)       # 设置HSV值
sleep(2)
```

## 执照

所有代码均在MIT许可下发布。