
# The MIT License (MIT)

# Copyright (c) 2019, Tangliufeng for labplus Industries

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# NEC infrared receiving and sending library of the mPython or MicropPython, please note that sending and receiving function cannot be used at the same time.
# Both have an effect,only choose one.
#
'''
# IR Receive example:
from ir_remote import  IRDecode
from machine import Pin

def remote_callback(address,command):        
    print(address,command)

remote = IRDecode( Pin.P1)
remote.set_callback(remote_callback)
# enable print debug
# remote.set_debug(True)
'''

'''
# IR send example:
from ir_remote import  IRTransmit
from machine import Pin

ir = IRTransmit(Pin.P0)

ir.send(0,01)  # format (address, command). or ir.send(b'\x00',b'\x01')

'''



def remote_callback(address,command):        
    print(address,command)
from machine import Pin, PWM
import time
import _thread
import gc

class IRDecodeException(Exception):
    """Generic decode exception"""
    pass


class _Const:
    NEC_HDR_MARK = 9000
    NEC_HDR_SPACE = 4500
    NEC_BIT_MARK = 560

class IRDecode:
  

    def __init__(self, pin):

        self.pulse_buffer = []
        self._prev_time = 0
        self.callback = None
        self.debug = False
        self.waittime = 150             # time in milliseconds
        self.recv = Pin(pin, Pin.IN, Pin.PULL_UP)
        self.recv.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING,
                      handler=self._pulse_width_record)
        _thread.start_new_thread(self._ir_recv_thread, ())

    def _pulse_width_record(self, pin):
        """record the width of th IR remote signal."""
        self._time = time.ticks_us()
        if self._prev_time == 0:
            self._prev_time = self._time
            return
        self.pulse_buffer.append(self._time - self._prev_time)
        self._prev_time = self._time

    def _lead_cheak(self):
        """function to cheak the lead code """
        offset = 0.3
        return int(_Const.NEC_HDR_MARK * (1-offset)) < self.pulse_buffer[0] < int(_Const.NEC_HDR_MARK*(1+offset))  \
            and int(_Const.NEC_HDR_SPACE*(1-offset)) < self.pulse_buffer[1] < int(_Const.NEC_HDR_SPACE*(1+offset))

    def decode_pulse_nec(self):
        """decode IR signal of NEC"""
        recv_bytes = bytearray(0)
        index = 0
        if self._lead_cheak():
            for i in range(4):
                byte = 0
                for j in range(8):
                    index = 16 * i + 2 * j + 2
                    _Const.NEC_BIT_MARK = min(
                        _Const.NEC_BIT_MARK, self.pulse_buffer[index])
                    if (self.pulse_buffer[index] +
                            self.pulse_buffer[index + 1]) > _Const.NEC_BIT_MARK * 4:
                        byte |= 1 << j

                recv_bytes.append(byte)
            return bytes(recv_bytes)

    def _print_debug(self,decode):
        """"""
        print('---------Received pulse width buffer---------')
        print('Lead Code: (%d %d)' %
              (self.pulse_buffer[0], self.pulse_buffer[1]))
        index = 0
        for i in range(4):
            print('Byte %d:' % i, end='')
            for j in range(8):
                index = 16 * i + 2 * j + 2
                print('(%d %d)' % (self.pulse_buffer[index], self.pulse_buffer[index + 1]),
                      end=', ')
            print('')
        print('Buffer:{} ,length:{}' .format(
            decode, len(self.pulse_buffer)))
        print('--------------------------------------------')

    def _ir_recv_thread(self):
        while True:
            if (time.ticks_us()-self._prev_time) > self.waittime * 1000 and self.pulse_buffer != []:
                if self._lead_cheak():
                    if len(self.pulse_buffer) >= 66:
                        decode = self.decode_pulse_nec()
                        if self.debug:
                            self._print_debug(decode)
                        self.pulse_buffer = []
                        self._prev_time = 0

                        if self.callback != None:
                            self.callback(decode[:1],decode[2:3])      # Address ,Command
                    else:
                        print("Warning: Buffer length too short!")
                        self.pulse_buffer = []
                        self._prev_time = 0

                else:
                    print("Warning: Buffer lead code error!")
                    self.pulse_buffer = []
                    self._prev_time = 0

                gc.collect()

    def set_callback(self, callback=None):
        """function to allow the user to set
        or change the callback function. farmat,callback(address ,command) """
        self.callback = callback

    def remove_callback(self):
        """remove_callback, function to allow the user to remove
        the callback function used at any time"""
        self.callback = None

    def set_debug(self, debug=True):
        """set_debug, function to turn verbose mode
        on or off. Used to print out pulse width list
        """
        self.debug = debug

class IRTransmit:
    """IR NEC  signal transmits"""
    def __init__(self,pin):
        self.ir_transmit = PWM(Pin(pin), duty=0, freq=38000)
        
    def _mark(self,us):
        self.ir_transmit.duty(512)
        time.sleep_us(us)

    def _space(self,us):
        self.ir_transmit.duty(0)
        time.sleep_us(us)

    def _bit(self, bit):
        # print(bit)
        self._mark(_Const.NEC_BIT_MARK)
        if bit:
            self._space(_Const.NEC_BIT_MARK*3)
        else:
            self._space(_Const.NEC_BIT_MARK)

    def _generate_bits(self,addr,cmd):
        if type(addr) == bytes : 
            addr = int.from_bytes(addr,'little')&0xff
        if type(cmd) == bytes : 
            cmd = int.from_bytes(cmd,'little')&0xff
        self._payload =[]
        for i in range(4):
            self._payload.append([])
        for i in range(8):
            if (addr>>i)&0x01:
                self._payload[0].append(1)
                self._payload[1].append(0)
            else:
                self._payload[0].append(0)
                self._payload[1].append(1)
        for i in range(8):
            if (cmd>>i)&0x01:
                self._payload[2].append(1)
                self._payload[3].append(0)
            else:
                self._payload[2].append(0)
                self._payload[3].append(1)

    def send(self,address,command):
        """send NEC data"""
        self._generate_bits(address,command)
        print(self._payload)
        self._mark(_Const.NEC_HDR_MARK)
        self._space(_Const.NEC_HDR_SPACE)
        for i in range(4):
            for j in range(8):
                self._bit(self._payload[i][j])
        self._mark(560)
        self._space(40000)
        


