#!/usr/bin/env python3
#
# Copyright (c) 2015 mindsensors.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

panServo = 0
tiltServo = 1

## PiPan: this class provides functions for PiPan servo controller
#  for read and write operations.
class PiPan:
    
    ServoBlaster = 0
    y = 0

    ## Initialize the class by opening servoblaster
    #  @param self The object pointer.
    def __init__(self):
        global ServoBlaster
        try:
            ServoBlaster = open('/dev/servoblaster', 'w')
        except (IOError):
            print("*** ERROR ***")
            print("Unable to open the device, check that servod is running")
            print("To start servod, run: sudo /etc/init.d/servoblaster.sh start")
            exit()

    ## Writes a pwm value one of the servo controller pins
    def pwm(self, pin, angle):
        #print "servo[" + str(pin) + "][" + str(angle) + "]"
        ServoBlaster.write(str(pin)+'=' + str(int(angle)) + '\n')
        ServoBlaster.flush()

    ## Brings the pan servo to neutral position
    def neutral_pan(self):
        self.pwm (panServo, 150)

    ## Brings the tilt servo to neutral position
    def neutral_tilt(self):
        self.pwm (tiltServo, 150)

    ## Writes pan movement value between 50 and 250
    def do_pan(self, x):
        if ( x > 250 ):
            x = 250
        if ( x < 50 ):
            x = 50
        self.pwm (panServo, x)

    # Writes the tilt movement value between 80 and 220
    def do_tilt(self, y):
        # limit tilt between 80 and 220
        if ( y > 220 ):
            y = 220
        if ( y < 80 ):
            y = 80
        self.pwm (tiltServo, y)


