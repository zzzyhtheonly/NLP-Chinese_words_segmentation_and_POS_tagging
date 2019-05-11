# -*- coding:utf8 -*-
import codecs
import sys
import string

list=open(sys.argv[1],"r",encoding="utf-8").read().split("\n")
open(sys.argv[2],"w",encoding="utf-8").writelines(list)