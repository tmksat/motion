#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test_motion.py
# tomoki_sato | 20170630
#

import time

from motion.motion import Interpolation
from motion.robot import Robot


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



def test_robot():
    r = Robot()
    print(r)

    test_pose_list = [  [10,20,30],
                        [-10,20, 4],
                        [0,3,-6],
                        [3,3,3]]
    r.set_pose_list(test_pose_list)
    print(r)

    test_step_list = [0.1, 0.2, 0.3, 1.0]
    r.set_step(test_step_list)
    print(r)

    while r.next() != [False, False, False, False]:
        time.sleep(0.05)    # for debug
        print(r)




if __name__ == '__main__':
    test_interpolation()
    test_robot()
