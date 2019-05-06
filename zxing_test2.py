#! /usr/bin/python
# coding=utf-8

import sys
import zxing

reader = zxing.BarCodeReader("/home/lizhihua/zxing")

barcode = reader.decode("wx.jpg")
print(barcode.data)
#print('\n'.join(['%s:%s' % item for item in barcode.__dict__.items()]))
# (barcode1, barcode2) = reader.decode(["/tmp/1.png", "/tmp/2.png"])
# code_list = reader.decode("/tmp/barcodes", True)