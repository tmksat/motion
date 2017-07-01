#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test_motion.py
# tomoki_sato | 20170630
#

import sys

from motion.motion import Interpolation
def test_interpolation():
    ip = Interpolation()
    print(ip)
    
    test_waypoint = [10, 20, 30, -10, -20, 50]
    for v in test_waypoint:
        ip.set_waypoint(v)
    print(ip)

    test_step = 0.1
    ip.set_step(test_step)
    print(ip)

    while ip.next() is not False:
        print(ip)
    
    print('test_interpolation finished!')




if __name__ == '__main__':
    test_interpolation()
