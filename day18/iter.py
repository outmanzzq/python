#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 


# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 100000:
#             raise StopIteration()
#         return self.a
#
#
# if __name__ == '__main__':
#     for n in Fib():
#         print(n)


class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


if __name__ == '__main__':
    f = Fib()
    print(f[0:5])
    print(f[:10])
    print(f[:10:2])