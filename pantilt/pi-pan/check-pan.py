#!/usr/bin/env python3
#
# Copyright (c) 2013 OpenElectrons.com
# Pi-Pan isntallation script.
# for more information about Pi-Pan,  please visit:
# http://www.openelectrons.com/Pi-Pan
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
# History:
# Date      Author      Comments
# 08/22/13  Deepak      Initial authoring.
#

import time
import os, sys
import pipan

print("Check that Pan servo is moving (horizontal movement)")

p = pipan.PiPan()

p.neutral_pan()
x = 150

while 1:
    # move head to right
    while x < 170:
        p.do_pan (int(x))
        time.sleep(0.1)
        x += 2

    # move head to left
    while x > 110:
        p.do_pan (int(x))
        time.sleep(0.1)
        x -= 2

