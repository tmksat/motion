#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# "motion" package
# tomoki_sato | 20170630
#


class Interpolation(object):
    """ waypoint間を補完するクラス """


    def __init__(self):
        self.name = ""
        self.waypoints = []
        self.now_value = 0.0
        self.now_target = 0.0
        self.param_step = 0.0
        self.step = 0.0
        self.count = 0


    def __str__(self):
        return u'[Ip][waypoints, value, target, step]=%s' % [str(s) for s in self.waypoints, self.now_value, self.now_target, self.step]


    def _calculate(self):
        if abs(self.now_target - self.now_value) < abs(self.step):
            self.now_value = self.now_target
            try:
                self.now_target = self.waypoints.pop(0)
            except:
                print(u'[Ip]Cannot pop next value from waypoints list')
                return False
        elif self.now_target > self.now_value:
            self.now_value += self.step
        elif self.now_target < self.now_value:
            self.now_value -= self.step
        else:
            pass


    def set_waypoint(self, wp):
        self.waypoints.append(wp)


    def get_waypoint(self):
        return self.waypoints


    def get_value(self):
        return self.now_value


    def get_target(self):
        return self.now_target


    def set_step(self, st):
        self.step = st


    def next(self):
        """ calculate next step """
        if self.count == 0:
            try:
                self.now_target = self.waypoints.pop(0)
            except:
                pass
        else:
            pass
        
        if self._calculate() is False:
            self.count += 1
            return False
        else:
            self.count += 1
            return self.now_value

        
