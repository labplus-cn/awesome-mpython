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
