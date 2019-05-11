#!/bin/bash
echo "Deal training data..."
if [ -f "InputTraining.pos" ]
then
	rm -rf "InputTraining.pos"
fi

for file in `ls trainingdata`
do
	echo "Processing "$file
	echo "-DOCSTART- -X-" >> "InputTraining.pos"
	echo "" >> "InputTraining.pos"
	python3 "generateInputforOne.py" "trainingdata/"$file "train" >> "InputTraining.pos"
done

echo "Deal test data..."
if [ -f "InputTest.pos" ]
then
	rm -rf "InputTest.pos"
fi

if [ -f "Baseline.pos" ]
then
	rm -rf "Baseline.pos"
fi

if [ -f "Baseline.seg" ]
then
	rm -rf "Baseline.seg"
fi

i=0;
for file in `ls testdata`
do
	echo "Processing "$file
	echo "-DOCSTART-" >> "InputTest.pos"
	echo "-DOCSTART- -X-" >> "Baseline.pos"
	echo "" >> "InputTest.pos"
	echo "" >> "Baseline.pos"
	python3 "generateInputforOne.py" "testdata/"$file "test" >> "InputTest.pos"
	python3 "generateInputforOne.py" "testdata/"$file "train" >> "Baseline.pos"
	if [ "$i" -lt 100 ]
	then
		python3 "generateInputforOne.py" "testdata/"$file "test" >> "Baseline.seg"
	fi
	((i++))
done

if [ -f "dictionary.dic" ]
then
	rm -rf "dictionary.dic"
fi

echo "Generating dictionary for segmentation..."
python3 generateDict.py InputTest.pos dictionary.dic

if [ -f "InputRaw.txt" ]
then
	rm -rf "InputRaw.txt"
fi

python3 generateRaw.py Baseline.seg InputRaw.txt

echo "All input files have been generated!"
