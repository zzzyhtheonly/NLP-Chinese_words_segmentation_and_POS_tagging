# -*- coding:utf8 -*-
import codecs
import string
import re
import sys 

print("Start Forward segmentation...")
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
		
	word = strIn[0:maxLen]
	while True:
		if(word in dict):
			words.append(word + '\n')
			i += len(word)
			strIn = strIn[len(word):n]
			break
		else:   
			if(len(word) == 1):  
				words.append(word + '\n')
				i += 1					
				strIn = strIn[1:n]
				break 
			else:
				word = word[0:len(word) - 1] 

open('forward.txt','w',encoding="utf-8").writelines(words)
print("Done!")