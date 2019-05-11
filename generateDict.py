# -*- coding:utf8 -*-

import string
import re
import sys

src_data = open(sys.argv[1],"r").read()
tmp = src_data.split("\n")
dict = set(tmp)

s = ""
for word in dict:
	s += word
	s += "\n"
f = open(sys.argv[2],'w',encoding="utf-8")
f.write(s)
