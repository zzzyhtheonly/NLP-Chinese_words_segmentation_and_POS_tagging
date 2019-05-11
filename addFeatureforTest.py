import sys
import string
import re

f = open(sys.argv[1],"r")

prev = "start"

words = []
pos = []

def is_start(word):
	if prev == "start":
		return True
	return False

def is_end(word):
	return False

def is_alpha(word):
	return word.isalpha()
	
def is_ascii(word):
	return all(ord(c) < 128 for c in word)  
	
def is_digit(word):
	return word.replace(",","").isdigit()

def is_alnum(word):
	return word.isalnum()
	
def is_punct(word):
	#punct = [',','.','!','?','\'','\"','`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','\\','\|','{','}','[',']',';',':','<','>','！','？','：','；','～','…','。','，','……','（','）','《','》']
	punctuation = """！？｡＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟…‧﹏"""
	return word in punctuation
	
def like_num(word):
	pattern = "\d+(\.\d+)?"
	chinese = [
	"一",
	"二",
	"三",
	"四",
	"五",
	"六",
	"七",
	"八",
	"九",
	"十",
	]
	return word.isnumeric() or word.isdecimal() or re.match(pattern,word) != None or word in chinese 

def is_title(word):
	return word.istitle()

def is_lower(word):
	return word.islower()

def is_upper(word):
	return word[0].isupper()

def is_date(word):
	chinese = [
	"一月",
	"二月",
	"三月",
	"四月",
	"五月",
	"六月",
	"七月",
	"八月",
	"九月",
	"十月",
	"十一月",
	"十二月",
	"年",
	"月",
	"日",
	"星期一",
	"星期二",
	"星期三",
	"星期四",
	"星期五",
	"星期六",
	"星期日",
	]
	return word.replace("-","").isdigit()

def is_val(val):
	return val

def_features =  {
	"word" : is_val,
	#"pos" : is_val,
	#"chunk" : is_val,
	#"tag" : is_val,

	#"isstart" : is_start,
	#"isend" : is_end,
	#"isalpha" : is_alpha,
	#"isascii" : is_ascii,
	"isdigit" : is_digit,
	"ispunct" : is_punct,
	#"isalnum" : is_alnum,
	"likenum" : like_num,
	"isdate" : is_date,
	#"isupper" : is_upper,
	#"istitle" : is_title,
	#"islower" : is_lower,
	
	"prevword" : is_val,
	#"prevpos" : is_val,
	#"prevchunk" : is_val,
	#"prevtag" : is_val,
	
	"nextword" : is_val,
	#"nextpos" : is_val,
	#"nextchunk" : is_val,
	#"nexttag" : is_val,
	
	"nnextword" : is_val,
	#"nnextpos" : is_val,
	#"nnextchunk" : is_val,
	#"nnexttag" : is_val,
	
	#"pprevword" : is_val,
	#"pprevpos" : is_val,
	#"pprevchunk" : is_val,
	#"pprevtag" : is_val,
}

enters = []

for line in f.readlines():
	if line == "\n" or line == "\r":
		enters.append(len(words))
		prev = "start"
		continue
	
	s = line.split()
	if len(s) < 2:
		words.append(str(s[0]))
		pos.append('@@')
		continue

	words.append(str(s[0]))
	pos.append(str(s[1]))

	prev = str(s[1])
f.close()
	
# output
prev = "start"
f = open(sys.argv[2],"w")
for i in range(0,len(words)):
	if i == enters[0]:
		f.write("\n")
		enters.pop(0)
		prev = "start"
	
	feature = {}
	for j in def_features.keys():

		if j == "pos":
			feature[j] = def_features[j](pos[i])
		elif j == "prevword":
			if prev == "start" and i < 1:
				feature[j] = def_features[j]("start")
			elif prev == "start" and i >= 1:
				feature[j] = def_features[j](-1)
			else:
				feature[j] = def_features[j](words[i - 1])
		elif j == "prevpos":
			if prev == "start" and i < 1:
				feature[j] = def_features[j]("start")
			elif prev == "start" and i >= 1:
				feature[j] = def_features[j](-1)
			else:
				feature[j] = def_features[j](pos[i - 1])
		elif j == "nextword":
			if i + 1 == len(words):
				feature[j] = def_features[j]("end")
			elif i + 1 == enters[0]:
				feature[j] = def_features[j](-1)
			else:
				feature[j] = def_features[j](words[i + 1])
		elif j == "nextpos":
			if i + 1 == len(words):
				feature[j] = def_features[j]("end")
			elif i + 1 == enters[0]:
				feature[j] = def_features[j](-1)
			else:
				feature[j] = def_features[j](pos[i + 1])
		elif j == "nnextword":
			if i < len(words) - 2 and i + 1 != enters[0] and i + 2 != enters[0]:
				feature[j] = def_features[j](words[i + 2])
			else:
				feature[j] = def_features[j](-1)
		else:
			feature[j] = def_features[j](words[i])

		
	s = ""
	s = s + words[i] + "\t"
	for j in feature.keys():
		if feature[j] != -1:
			s = s + str(j) + "=" + str(feature[j]) + "\t"
			
	s = s + pos[i] + "\n"
	f.write(s)
	prev = pos[i]
f.write("\n")
f.close()
	