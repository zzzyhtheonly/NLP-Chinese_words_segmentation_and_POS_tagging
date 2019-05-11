# -*- coding:utf8 -*-
import codecs
import string
import re
import sys 
  
# segmentation of forward and backward
def seg(dict,maxLen,sentence,foreward=True):
	words = []  
	cycle = len(sentence)/100
	i = 0
	j = 0
	while(len(sentence) > 0):
		n = len(sentence)
		
		if i > cycle:
			i = 0
			j += 1
			print("Processing %d%% "%j)
		
		if foreward:
			word = sentence[0:maxLen]
		else:
			word = sentence[n - maxLen:n]

		found = False; 
  
		while((not found) and (len(word)>0)):
			if(word in dict):
				words.append(word + '\n')
				i += len(word)
				if foreward:
					sentence = sentence[len(word):n]
				else:
					sentence = sentence[0:n-len(word)]
				found = True;
			else:   
				if(len(word) == 1):  
					words.append(word + '\n')
					i += 1					
					if foreward:
						sentence = sentence[1:n]
					else:
						sentence = sentence[0:n - 1]
					found = True; 
				else:
					if foreward:
						word = word[0:len(word) - 1]
					else:
						word = word[1:len(word)]
	return words  
  
# load dictionary
f = open(sys.argv[1],'r',encoding="utf-8").read()  
maxLen = 1  
dict = f.split("\n")
for i in dict:
	if len(i) > maxLen:  
		maxLen = len(i)  

# load raw data
strIn = open(sys.argv[2],encoding="utf-8").read()
	
print("Start Forward segmentation...")
f_result = seg(dict,maxLen,strIn,True)
open('forward.txt','w',encoding="utf-8").writelines(f_result)
print("Done!")
print("Start Backward segmentation...")
b_result = seg(dict,maxLen,strIn,False)
open('backward.txt','w',encoding="utf-8").writelines(b_result[::-1])
print("Done!")