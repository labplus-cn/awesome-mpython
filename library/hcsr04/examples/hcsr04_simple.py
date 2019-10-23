from hcsr04 import HCSR04
from mpython import *

sensor = HCSR04(trigger_pin=Pin.P0, echo_pin=Pin.P1)

distance = sensor.distance_cm()

print('Distance:', distance, 'cm')

while True:
    distance_mm = sensor.distance_mm()
    distance_cm = sensor.distance_cm()
    print('Distance: %0.1fmm , %0.1fcm' % (distance_mm, distance_cm))
    sleep_ms(200)
