#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 

from PIL import Image, ImageFilter


im = Image.open('cat.jpeg')
#
# w, h = im.size
# print('Original image size: %sx%s' % (w, h))
#
# im.thumbnail((w//2, h//2))
# print('Resize image to: %sx%s' % (w//2, h//2))
#
# im.save('thumbnail.jpg', 'jpeg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')