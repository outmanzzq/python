#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self.height * self.width


if __name__ == '__main__':
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution = ', s.resolution)

    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')

