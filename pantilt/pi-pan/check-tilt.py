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

print("Check that Tilt servo is moving (vertical movement)")

p = pipan.PiPan()

p.neutral_tilt()
x = 150

while 1:
    # move head down
    while x < 180:
        p.do_tilt (int(x))
        time.sleep(0.1)
        x += 2

    # move head up
    while x > 90:
        p.do_tilt (int(x))
        time.sleep(0.1)
        x -= 2

