
from neopixel import *
from machine import Pin
from time import sleep_us, sleep_ms
import math
from random import randint

def hsv2rgb(hsv):
    h = float(hsv[0])
    s = float(hsv[1])
    v = float(hsv[2])
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0:
        r, g, b = v, t, p
    elif hi == 1:
        r, g, b = q, v, p
    elif hi == 2:
        r, g, b = p, v, t
    elif hi == 3:
        r, g, b = p, q, v
    elif hi == 4:
        r, g, b = t, p, v
    elif hi == 5:
        r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b


def rgb2hsv(rgb):
    r, g, b = rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return round(h,2), round(s,2), round(v,2)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b)


class LedStrip(NeoPixel):

    def __init__(self, pin, n=24, brightness=0.5, timing=1):
        self._brightness = brightness
        useable_pin = [Pin.P5, Pin.P6, Pin.P8, Pin.P9, Pin.P11,
                       Pin.P13, Pin.P14, Pin.P15, Pin.P16, Pin.P19, Pin.P20]
        if pin not in useable_pin:
            raise TypeError('neopixel not supported in IO%d' % pin)
        super().__init__(Pin(pin), n=n, bpp=3, timing=timing)

    def clear(self):
        # 熄灭所有RGB
        for i in range(self.n):
            self[i] = (0, 0, 0)
            self.write()

    def write(self):
        if self._brightness > 0.99:
            neopixel_write(self.pin, self.buf, self.timing)
        else:
            neopixel_write(self.pin, bytearray([int(i * self._brightness) for i in self.buf]), self.timing)

    def brightness(self, brightness):
        self._brightness = min(max(brightness, 0.0), 1.0)

    def rainbow(self, wait_us=20):
        # 彩虹效果
        for j in range(255):

            for i in range(self.n):
                self[i] = wheel((i+j) & 255)
            self.write()
            sleep_us(wait_us)

    def rainbow_cycle(self, wait_us=20):
        # 与rainbow略有不同，这使得彩虹在整个过程中均匀分布
        for j in range(255):
            for i in range(self.n):
                pixel_index = (i * 256 // self.n) + j
                self[i] = wheel(pixel_index & 255)
            self.write()
            sleep_us(wait_us)

    def cycle(self, c, wait=20):
        # 循环效果,有一个像素在所有灯带位置上运行，而其他像素关闭。
        for i in range(4 * self.n):
            for j in range(self.n):
                self[j] = (0, 0, 0)
            self[i % self.n] = c
            self.write()
            sleep_ms(wait)

    def bounce(self, c, wait=20):
        # 弹跳效果,等待时间决定了弹跳效果的速度
        for i in range(4 * self.n):
            for j in range(self.n):
                self[j] = c
            if (i // self.n) % 2 == 0:
                self[i % self.n] = (0, 0, 0)
            else:
                self[self.n - 1 - (i % self.n)] = (0, 0, 0)
            self.write()
            sleep_ms(wait)

    def colorWipe(self, c, wait=10):
        # 逐个填充颜色
        # Fill the dots one after the other with a color
        for i in range(self.n):
            self[i] = c
            sleep_ms(wait)
            self.write()
            sleep_ms(wait)

    def theaterChase(self, c, wait=50):
        # 剧院风格的追逐灯
        for j in range(10):
            for q in range(3):
                for i in range(0, self.n, 3):
                    self[i+q] = c
                self.write()
                sleep_ms(wait)
                for i in range(0, self.n, 3):
                    self[i+q] = (0, 0, 0)

    def theaterChaseRainbow(self, wait=50):
        # 剧院风格的追逐灯带rainbow效果
        for j in range(256):
            for q in range(3):
                for i in range(0, self.n, 3):

                    self[i+q] = wheel((i+j) % 255)
                self.write()
                sleep_ms(wait)
                for i in range(0, self.n, 3):
                    self[i+q] = (0, 0, 0)

    def cylonBounce(self, c, eye_size, spee_delay, return_delay):
        """ 
        我想我们并不是所有人都知道Cylon是什么，但我和那些很酷的机器人一起长大，我肯定想拥有一个。我熟悉骑士骑士（尽管那个时代差不多）？它很亲切 - 类似。这种类型的“扫描仪”通常被称为拉尔森扫描仪，
        以Glen Larson的名字命名，Glen Larson是负责制作原始太空堡垒卡拉狄加和骑士骑士电视节目的人。无论如何，这里有一个模拟Cylon移动“眼睛”的效果：一个红色的“眼睛”从左到右，一次又一次地向后移动。
        亲切 - 一个充满弹性的球哈哈。
        :param eye_size-确定运行的LED数量，或：“眼睛”的宽度（外部2，褪色，LED未计数）
        :param spee_delay-影响眼睛移动的速度，较高的值意味着移动缓慢。
        :param return_delay-设置应该等待反弹的时间
        """
        for i in range(self.n-eye_size - 2):
            self.fill((0, 0, 0))
            self[i] = (int(c[0]/10), int(c[1]/10), int(c[2]/10))
            for j in range(1, eye_size+1):
                self[i+j] = c
            self[i+eye_size+1] = (int(c[0]/10), int(c[1]/10), int(c[2]/10))
            self.write()
            sleep_ms(spee_delay)

        sleep_ms(return_delay)

        for i in range(self.n-eye_size - 2, 0, -1):
            self.fill((0, 0, 0))
            self[i] = (int(c[0]/10), int(c[1]/10), int(c[2]/10))
            for j in range(1, eye_size+1):
                self[i+j] = c
            self[i+eye_size+1] = (int(c[0]/10), int(c[1]/10), int(c[2]/10))
            self.write()
            sleep_ms(spee_delay)

        sleep_ms(return_delay)

    def runningLight(self, c, wait):
        """
        这种效应使得多组LED相互追逐。亲切 - 就像你在节日期间用来在商店看到的行车灯一样。
        :param wait表示循环中放入了多少延迟，数字越大，它就越慢。
        """
        position = 0
        for j in range(self.n * 2):
            position += 1
            for i in range(self.n):
                self[i] = (int(((math.sin(i+position) * 127 + 128)/255)*c[0]),
                           int(((math.sin(i+position) * 127 + 128)/255)*c[1]),
                           int(((math.sin(i+position) * 127 + 128)/255)*c[2]))
            self.write()
            sleep_ms(wait)

    def meteorRain(self,c,size,trail_decay,random_decay,delay):
        """
        流星雨效果
        :param size  - 设置流星大小代表流星的LED数量，不计算流星的尾部
        :param  trail_decay - 流星尾部衰减/消失的速度。数字越大，尾部越短和/或消失得越快。理论上，值为64时，每次流星绘制时亮度都会降低25％
        :param  random_decay - 随机衰变-通过使衰变有点随机来模仿碎片中的某些差异。如果此值设置为“true”，则会向轨道添加一些随机性。如果将值设置为“false”，则尾部将非常平滑
        :param  delay - 延时

        """

        self.fill((0,0,0))
        def fadeToBlack(ledNo, fadeValue):
        
            r = self.buf[ledNo*3+0]
            g = self.buf[ledNo*3+1]
            b = self.buf[ledNo*3+2]
     
            r = (0 if (r<=10) else r-int(r*fadeValue/256 ))
            g = (0 if (g<=10) else g-int(g*fadeValue/256 ))
            b = (0 if (b<=10) else b-int(b*fadeValue/256 ))

            self[ledNo]=(r,g,b)

        for i in range(self.n*2):

            for j in range(self.n):
                if (not random_decay) or (randint(0,10) > 5) :
                    fadeToBlack(j, trail_decay )      

            for j in range(size):
                if ( i-j <self.n) and (i-j>=0) :

                    self[i-j]=c
            
            self.write()
            sleep_ms(delay)
  