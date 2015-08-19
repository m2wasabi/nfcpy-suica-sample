#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import struct
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/nfcpy')

import nfc

service_code = 0x090f
num_blocks = 20

def connected(tag):
  print tag
  if isinstance(tag, nfc.tag.tt3.Type3Tag):
    try:
      for i in range(num_blocks):
        # 1レコードだけ取得
        sc = nfc.tag.tt3.ServiceCode(service_code >> 6 ,service_code & 0x1f)
        bc = nfc.tag.tt3.BlockCode(i,service=0)
        data = tag.read_without_encryption([sc],[bc])
        print "" . join(['%02x ' % s for s in data])
    except Exception as e:
      print "error: %s" % e
  else:
    print "error: tag isn't Type3Tag"

# 接続開始
clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': connected})
