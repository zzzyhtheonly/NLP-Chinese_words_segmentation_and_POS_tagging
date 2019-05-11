import sys

f = open(sys.argv[1],"r")

tag = sys.argv[2]
s = ""

for line in f.readlines():
	if line[0] == '<' or line == '\n' or line[0] == '＜':
		continue
	tmp = line.split()
	
	for word in tmp:
		for c in word:
			if c == '_':
				if tag == 'test':
					break
				else:
					s += ' '
			else:
				s += c
		s += '\n'
	s += '\n'

print(s)

