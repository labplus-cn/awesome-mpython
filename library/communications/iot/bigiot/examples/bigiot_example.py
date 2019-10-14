from mpython import *
from bigiot import Device       

mywifi = wifi()                 # 连接wifi
mywifi.connectWiFi('', '')



ID = ""                             # 设备ID
API_KEY = ""                        # 设备APIKEY

def say_cb(msg):                    # 回调函数
    print(msg)

device = Device(ID, API_KEY)        # 构建bigiot 设备

device.say_callback(say_cb)         # 设置say通讯的回调函数

device.check_in()                   # 登录

device.say(user_id=0000,msg="hello I am mpython!")   # 向web,app端发送消息
