#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import struct
import sys
import inspect

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/nfcpy')

import nfc

service_code = 0x090f
num_blocks = 20

def connected(tag):
  # tag のメソッド一覧を出す
  print type(tag)
  print inspect.getmembers(tag, inspect.ismethod)

# 接続開始
clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': connected})
