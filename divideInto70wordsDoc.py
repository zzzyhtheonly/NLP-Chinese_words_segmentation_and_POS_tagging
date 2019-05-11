import sys

# unused, only use this in personal segmentation test



def is_alphabet(char):
	if (char >= '\u0041' and char <= '\u005a') or (char >= '\u0061' and char <= '\u007a'):
		return True
	else:
		return False


with open(sys.argv[1],'rb') as f:
      buffer = f.read().decode('utf-8')
f.close()

i = 0
j = 1
words = ""
for c in buffer:
	
	if i < 70 or is_alphabet(c):
		words += c
		i += 1
	else:
		f = open("./input/" + str(j),"w", encoding = 'utf8')
		j += 1
		f.write(words)
		f.close()
		words = c
		i = 0

	