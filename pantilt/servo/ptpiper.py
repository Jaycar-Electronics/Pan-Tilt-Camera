#!/usr/bin/env python3

import time
import os, sys
import pipan

p_servo = pipan.PiPan()


while True:
  fifoLocation = os.environ['PIPAN_FIFO_LOCATION']
  pipein = open(fifoLocation, 'r')
  line = pipein.readline()
  print(line)
  line_array = line.split(' ')
  if line_array[0] == "servo":
    p_servo.do_pan(int(line_array[1]))
    p_servo.do_tilt(int(line_array[2]))
  pipein.close()
