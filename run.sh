#!/bin/bash
if [ -f "trainingdata.tar" ]
then
	tar xvf "trainingdata.tar"
fi

if [ -f "testdata.tar" ]
then
	tar xvf "testdata.tar"
fi

echo "Start generating raw data into Input we need..."
./generate_ALL_input.sh

if [ -f "forward.txt" ]
then
	rm -rf "forward.txt"
fi

if [ -f "backward.txt" ]
then
	rm -rf "backward.txt"
fi

echo "Start segmentation..."
python3 forward_segmentation.py dictionary.dic InputRaw.txt
python3 backward_segmentation.py dictionary.dic InputRaw.txt

if [ -f "output.pos" ]
then
	rm -rf "output.pos"
fi

echo "Start training and generating results with POS tags..."
python3 addPOS.py InputTraining.pos InputTest.pos

if [ -f "result.res" ]
then
	rm -rf "result.res"
fi

if [ -f "output.feature" ]
then
	rm -rf "output.feature"
fi

if [ -f "output_test.feature" ]
then
	rm -rf "output_test.feature"
fi

echo "Start generating features output of training data..."
python3 addFeature.py InputTraining.pos output.feature
echo "Start generating features output of test data..."
python3 addFeatureforTest.py InputTest.pos output_test.feature
echo "Start comparing the Baseline with our outputs..."
echo "The correctness of forward segmentation is:" >> "result.res"
python3 SEGscore.py Baseline.seg forward.txt >> "result.res"
echo "The correctness of backward segmentation is:" >> "result.res"
python3 SEGscore.py Baseline.seg backward.txt >> "result.res"
echo "The correctness of pos tagging is:" >> "result.res"
python3 POSscore.py output.pos Baseline.pos >> "result.res"

echo "Now we have done, and the results of segmentations and HMM tagging is:"
echo ""
cat "result.res"
echo ""
echo "You can check all the results at result.res"
