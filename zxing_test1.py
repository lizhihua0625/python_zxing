#! /usr/bin/python
# coding=utf-8

import sys
#pip install qrcode pillow image zxing
import zxing

reader = zxing.BarCodeReader()
barcode = reader.decode("wx.jpg")
print(barcode.data)
#print('\n'.join(['%s:%s' % item for item in barcode.__dict__.items()]))