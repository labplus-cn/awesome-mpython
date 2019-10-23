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