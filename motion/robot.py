#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# robot.py
# tomoki_sato | 20170630
#

from motion import Interpolation


class Robot(object):
    """ Robot class """
    
    def __init__(self):
        self.joints = [Interpolation(), Interpolation(), Interpolation(), Interpolation()]  # j0, j1, j2, j3


    def __str__(self):
        ret = ''
        for j in self.joints:
            ret += (str(j) + u'\n')
        ret += u'---\n'
        return ret


    def set_pose_list(self, p):
        for i in range(4): # 4 axis
            for v in p[i]:
                self.joints[i].set_waypoint(v)


    def set_step(self, s):
        for i in range(4):
            self.joints[i].set_step(s[i])


    def next(self):
        return [j.next() for j in self.joints]
