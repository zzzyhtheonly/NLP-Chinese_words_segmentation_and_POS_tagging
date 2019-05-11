import sys

f1 = open(sys.argv[1],"r")
f2 = open(sys.argv[2],"r")

punctuation = """！？：；～…。，……（）《》"""

base = []
word_cnt = 0
sentence_cnt = 0
paragraph_cnt = 0
doc_cnt = 0
for line in f1.readlines():
	if line == "\n":
		paragraph_cnt += 1
		continue
	
	s = line.split()
	if len(s) != 2:
		continue
	if s[0] == "-DOCSTART-":
		doc_cnt += 1
	if s[0] in punctuation:
		sentence_cnt += 1
	base.append(s)
	word_cnt += 1
f1.close()
	
word_correct = 0
sentence_correct = 0
paragraph_correct = 0
doc_correct = 0
sentence_tag = True
paragraph_tag = True
doc_tag = True
i = 0
for line in f2.readlines():
	if line == "\n":
		if paragraph_tag:
			paragraph_correct += 1
		paragraph_tag = True
		continue
	
	s = line.split()
	if len(s) != 2:
		continue
	if s[0] == "-DOCSTART-":
		if doc_tag:
			doc_correct += 1
		doc_tag = True
	if s[0] in punctuation:
		if sentence_tag:
			sentence_correct += 1
		sentence_tag = True
	if s[0] == base[i][0] and s[1] == base[i][1]:
		word_correct += 1
	else:
		sentence_tag = False
		paragraph_tag = False
		doc_tag = False
	i += 1
f2.close()

print("Words correctness: " + str(100*word_correct/word_cnt) + "%")
print("Sentences correctness: " + str(100*sentence_correct/sentence_cnt) + "%")
print("Paragraph correctness: " + str(100*paragraph_correct/paragraph_cnt) + "%")
print("Docs correctness: " + str(100*doc_correct/doc_cnt) + "%")
