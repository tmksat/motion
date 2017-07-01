#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# "motion" package
# tomoki_sato | 20170630
#


class Interpolation:
    """ waypoint間を補完するクラス """
    
    def __init__(self):
        self.name = ""
        self.waypoints = []
        self.now_value = 0.0
        self.parameter = 0.0
    
    def __str__(self):
        return "this is interpolation class."   # test
    
    def set_waypoint(self, wp):
        self.waypoints.append(wp)
    
    def get_waypoint(self):
        return self.waypoints
    
    def next(self):
        # calculate next step

    

    
