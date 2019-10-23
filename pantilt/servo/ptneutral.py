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
# Original source: http://www.mindsensors.com/content/33-pi-pan-readme
# History:
# Date      Author      Comments
# 08/22/13  Deepak      Initial authoring.
# 21/10/19  Dotrar      Change to py3, del unwarranted

import time
import pipan

print(' -- neutral servos pan-tilt -- ')
# create PiPan object
p = pipan.PiPan()
p.neutral_pan()
p.neutral_tilt()
time.sleep (1)
