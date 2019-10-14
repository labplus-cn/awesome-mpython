ledstrip module 是 micropython neopixel module的增强版，在neopixel基础功能上封装多种的灯带显示效果。
支持掌控板或micropython的使用。


## 库的安装方法

可通过以下任一方法进行安装。
1. 将项目中的`ledstrip.py`拷到掌控板文件系统上
2. 在掌控板REPL界面中，使用upip安装，步骤如下：
    * 前置条件需要掌控板连接网络
    * 导入upip模块，执行`import upip`
    * 执行`upip.install('mPython-ledstrip'）

```python
>>> import upip
>>> upip.install('mPython-ledstrip')
```
## 简单示例

```python
from ledstrip import *
from machine import Pin

strip=LedStrip(pin=Pin.P15,n=24,brightness=0.5)

print("rainbow")
strip.rainbow()  
print("rainbow_cycle")
strip.rainbow_cycle()  
print("cycle")
strip.cycle((50,50,50))
print("bounce")
strip.bounce((0,0,50))
strip.clear()
print("colorWipe")
strip.colorWipe((0,50,0))
print("theaterChase")
strip.theaterChase((50,0,0))
print("theaterChaseRainbow")
strip.theaterChaseRainbow(wait=5)
print("cylonBounce")
strip.cylonBounce((0,0,50),4,10,50)
print("runningLight")
strip.runningLight((50,50,0),20)

print("meteorRain")
for i in  range(5):
    strip.meteorRain((100,100,100),8,60,True,20)
```


## API 说明

| 函数    | 功能说明  | 参数      |
| :------ | :------  | :------ |
| hsv2rgb(hsv) |将HSV颜色三元组转换为RGB三元组 | ``hsv`` - 三元组 |
| rgb2hsv(rgb) |将RGB颜色三元组转换为HSV三元组 | ``rgb`` - 三元组 |
| wheel(pos) |彩轮，将0~255值转换为RGB三元组 | ``pos`` - 0~255 |
|LedStrip( pin, n=24, brightness=1.0, timing=1) |LedStrip类初始化 | ``pin`` - 引脚； ``n`` - 灯数 </br> ``brightness`` - 亮度设置，范围0~1.0；``timing`` -速率，1为800Khz，0为400kHz  |
| LedStrip.clear() | 熄灭所有灯，不用write()即可生效| /|
| LedStrip.brightness(brightness) | 设置灯带亮度| ``brightness`` - 0~1.0|
| LedStrip.rainbow(wait_us=20) | 彩虹效果| ``wait_us`` - 等待时间，默认20毫秒|
| LedStrip.rainbow_cycle(wait_us=20) | 彩虹环效果:与rainbow略有不同，彩虹在整个过程中均匀分布| ``wait_us`` - 等待时间，默认20毫秒|
| LedStrip.cycle(c, wait=20) |循环效果：有一个像素在所有灯带位置上运行，而其他像素关闭。 | ``c`` - 显示灯RGB颜色，(r,g,b)三元组； ``wait`` - 等待时间，单位毫秒，默认20|
| LedStrip.bounce(c, wait=20) |弹跳效果：弹跳效应和接受(R,G,B)来设置颜色，以及等待时间。等待时间决定了弹跳效果的速度。 | ``c`` - 显示灯RGB颜色，(r,g,b)三元组；``wait`` - 等待时间，单位毫秒，默认20|
| LedStrip.colorWipe(c, wait=20) |逐个填充颜色 | ``c`` - 填充RGB颜色，(r,g,b)三元组；``wait`` - 等待时间，单位毫秒，默认20|
| LedStrip.theaterChase(c, wait=20) |剧院风格的追逐灯效果 | ``c`` - 填充RGB颜色，(r,g,b)三元组；``wait`` - 等待时间，单位毫秒，默认20|
| LedStrip.theaterChaseRainbow(wait=20) |剧院风格的追逐灯效果 | ``wait`` - 等待时间，单位毫秒，默认20|
| LedStrip.cylonBounce(c, eye_size, spee_delay, return_delay) |Cylon效果：模拟Cylon移动“眼睛”的效果：一个红色的“眼睛”从左到右，一次又一次地向后移动 | ``eye_size`` - 运行的LED数量，或：“眼睛”的宽度（外部2，褪色，LED未计数）；``spee_delay`` -影响眼睛移动的速度，较高的值意味着移动缓慢; </br> ``return_delay`` - 设置应该等待反弹的时间|
| LedStrip.runningLight(c,wait) |行走灯效果：多组LED相互追逐。亲切 - 就像你在节日期间用来在商店看到的行车灯一样 |  ``c`` - 显示灯RGB颜色，(r,g,b)三元组； ``wait`` - 等待时间，单位毫秒0 |
| LedStrip.meteorRain(c,size,trail_decay,random_decay,delay) |流星雨效果 |  ``c`` - 显示灯RGB颜色，(r,g,b)三元组；``size`` - 设置流星大小代表流星的LED数量，不计算流星的尾部; </br> ``trail_decay`` - 流星尾部衰减/消失的速度。数字越大，尾部越短和/或消失得越快。理论上，值为64时，每次流星绘制时亮度都会降低25％; ``delay`` - 延时 |

## 执照

所有代码均在MIT许可下发布。