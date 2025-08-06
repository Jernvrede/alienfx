#
# controller_R4.py
#
# Copyright (C) 2013-2014 Ashwin Menon <ashwin.menon@gmail.com>
# Copyright (C) 2015-2021 Track Master Steve <trackmastersteve@gmail.com>
#
# Alienfx is free software.
#
# You may redistribute it and/or modify it under the terms of the
# GNU General Public License, as published by the Free Software
# Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# Alienfx is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with alienfx.    If not, write to:
# 	The Free Software Foundation, Inc.,
# 	51 Franklin Street, Fifth Floor
# 	Boston, MA  02110-1301, USA.
#

""" Specialization of the AlienFxController class for the R4 controller.

This module provides the following classes:
AlienFXControllerR4 : Aurora R4 Desktop
"""

import alienfx.core.controller as alienfx_controller

class AlienFXControllerdesktopr4(alienfx_controller.AlienFXController):
    
    """ Specialization of the AlienFxController class for the R4 controller.
    """
    
    # Speed capabilities. The higher the number, the slower the speed of 
    # blink/morph actions. The min speed is selected by trial and error as 
    # the lowest value that will not result in strange blink/morph behaviour.
    DEFAULT_SPEED = 200
    MIN_SPEED = 50
    
    # Zone codes
    LEFT_PANEL = 0x0080
    RIGHT_PANEL = 0x0100
    FRONT_BOTTOM = 0x0008
    FRONT_LEFT = 0x0020
    FRONT_RIGHT = 0x0040
    ALIEN_HEAD = 0x0001
    TOP_LEFT = 0x0002
    TOP_RIGHT = 0x0004

    # Reset codes
    RESET_ALL_LIGHTS_OFF = 3
    RESET_ALL_LIGHTS_ON = 4
    
    # State codes
    BOOT = 1
    AC_SLEEP = 2
    
    def __init__(self):
        alienfx_controller.AlienFXController.__init__(self)
        self.name = "Alienware R4 Desktop"
        
        # USB VID and PID
        self.vendor_id = 0x187c
        self.product_id = 0x0513
        
        # map the zone names to their codes
        self.zone_map = {
            self.ZONE_LEFT_PANEL: self.LEFT_PANEL,
            self.ZONE_RIGHT_PANEL: self.RIGHT_PANEL,
            self.ZONE_FRONT_RIGHT: self.FRONT_RIGHT,
            self.ZONE_FRONT_LEFT: self.FRONT_LEFT,
            self.ZONE_ALIEN_HEAD: self.ALIEN_HEAD,
            self.ZONE_FRONT_BOTTOM: self.FRONT_BOTTOM,
            self.ZONE_TOP_LEFT: self.TOP_LEFT,
            self.ZONE_TOP_RIGHT: self.TOP_RIGHT,
        }
        
        # map the reset names to their codes
        self.reset_types = {
            self.RESET_ALL_LIGHTS_OFF: "all-lights-off",
            self.RESET_ALL_LIGHTS_ON: "all-lights-on"
        }
        
        # map the state names to their codes
        self.state_map = {
            self.STATE_BOOT: self.BOOT,
            self.STATE_AC_SLEEP: self.AC_SLEEP,
        }

alienfx_controller.AlienFXController.supported_controllers.append(
    AlienFXControllerdesktopr4())
