import sys

f1 = open(sys.argv[1],"r")
f2 = open(sys.argv[2],"r")

arc = {}
emit = {}

arc_cnt = 0
emit_cnt = 0
prev = "start"
arc["start"] = {}
arc["."] = {}
for line in f1.readlines():
	if line == "\n" or line == "\r":
		if "end" not in arc[prev].keys():
			arc[prev]["end"] = 0
		arc[prev]["end"] += 1
		prev = "start"
		continue
		
	str = line.split()
	if len(str) != 2:
		continue

	if str[1] not in emit.keys():
		emit[str[1]] = {}
	if str[1] not in arc[prev].keys():
		arc[prev][str[1]] = 0
	if str[0] not in emit[str[1]].keys():
		emit[str[1]][str[0]] = 0
	arc[prev][str[1]] += 1
	emit[str[1]][str[0]] += 1
	prev = str[1]
	if prev not in arc.keys():
		arc[prev] = {}


for i in arc.keys():
	for j in arc[i].keys():
		arc_cnt += arc[i][j]
	for j in arc[i].keys():
		arc[i][j] = arc[i][j] / arc_cnt
	arc_cnt = 0

for i in emit.keys():
	for j in emit[i].keys():
		emit_cnt += emit[i][j]
	for j in emit[i].keys():
		emit[i][j] = emit[i][j] / emit_cnt
	emit_cnt = 0

f1.close()

output_file = open("output.pos", "w")
prev = "start"
prevprob = 1.0
s = ""
for line in f2.readlines():
	if line == "\n" or line == "\t":
		s += "\n"
		prev = "start"
		prevprob = 1.0
		continue
	if line == "":
		break
	tmp = line.replace("\n","")
	res = "UNKNOWN"
	prob = prevprob
	resprob = 0
	for i in arc[prev].keys():
		if i != "end" and tmp in emit[i].keys():
			prob = prevprob * arc[prev][i] * emit[i][tmp]
			if resprob < prob:
				resprob = prob
				res = i
	if res == "UNKNOWN":
		for i in emit.keys():
			if i != "end" and tmp in emit[i].keys():
				prob = prevprob * emit[i][tmp]
				if resprob < prob:
					resprob = prob
					res = i
	if res == "UNKNOWN":
		for i in arc[prev].keys():
			if i == "end":
				continue
			prob = prevprob * arc[prev][i]
			if resprob < prob:
				resprob = prob
				res = i

	s = s + tmp + " " + res + "\n"
	prevprob = resprob
	if res != "UNKNOWN":
		prev = res

f2.close()
output_file.write(s)
