# -*- coding:utf8 -*-
import codecs
import string
import re
import sys 
  
print("Start Backward segmentation...")
# load dictionary
f = open(sys.argv[1],'r',encoding="utf-8").read()  
maxLen = 1  
dict = f.split("\n")
for i in dict:
	if len(i) > maxLen:  
		maxLen = len(i)  

# load raw data
strIn = open(sys.argv[2],encoding="utf-8").read()

words = []  
cycle = len(strIn)/100
i = 0
j = 1
while(len(strIn) > 0):
	n = len(strIn)	
	if i > cycle:
		print("Processing %d%% "%j)
		i = 0
		j += 1
		
	word = strIn[n - maxLen:n]
	while True:
		if(word in dict):
			words.append(word + '\n')
			i += len(word)
			strIn = strIn[0:n-len(word)]
			break
		else:   
			if(len(word) == 1):  
				words.append(word + '\n')
				i += 1					
				strIn = strIn[0:n - 1]
				break
			else:
				word = word[1:len(word)]
	
open('backward.txt','w',encoding="utf-8").writelines(words[::-1])
print("Done!")