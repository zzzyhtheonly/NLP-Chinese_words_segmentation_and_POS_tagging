# -*- coding:utf8 -*-
import codecs
import sys
import string

baseline = open(sys.argv[1],"r",encoding="utf-8").read().split("\n")
list = open(sys.argv[2],"r",encoding="utf-8").read().split("\n")

correct = 0
lidx = 0
bidx = 0
idx = 0
for w in list:
	while(lidx > bidx and idx < len(baseline)):
		bidx += len(baseline[idx])
		idx += 1

	if idx == len(baseline):
		continue
	if lidx < bidx:
		lidx += len(w)
		continue
	if w == baseline[idx]:
		correct += 1
	lidx += len(w)
	
print("Correct words：%d"%correct)
print("All generating words：%d"%len(list))
print("All baseline words：%d"%len(baseline))
	
P = correct*1.0/len(list)
R = correct*1.0/len(baseline)
F = 2*P*R/(P+R)
	
print("Precision = %.3f"%P)
print("Recall = %.3f"%R)
print("F measure = %.3f"%F)
	
