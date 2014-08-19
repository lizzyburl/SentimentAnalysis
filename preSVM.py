import json;
import os;

# creates an output file ready for use by libSVM
# outputFileName: the output file name
# posPath: The path for the folder containing positive movie reviews
# negPath: The path for the folder containing negative movie reviews
def prepareOutput(outputFileName, posPath, negPath):
	with open("dictionary.json", "rb") as fp:
	    dictionaryScore = json.load( fp, encoding="latin1")


	indexMap = {};
	counter = 1;

	# The index cannot be a word; it must be a number, so we map each word to a unique number
	for word in dictionaryScore.keys():
		indexMap[word] = counter;
		counter = counter + 1;

	output = open(outputFileName , 'wb');


	for filename in os.listdir(posPath): 
		f = open(os.path.join(posPath, filename), 'r');
		reviewMap = {};

		for word in f.read().split():
			# Only care about words that are in the giant dictionary of words.
			if not word in dictionaryScore.keys():
				continue;
			if word in reviewMap.keys():
				reviewMap[word] = reviewMap[word] + 1;
			else:
				reviewMap[word] = 1;

		# Format the output as it asked
		output.write('+1 ');
		for word in reviewMap.keys():
			value = reviewMap[word] * dictionaryScore[word];
			output.write(str(indexMap[word]) + ":" + str(reviewMap[word]*dictionaryScore[word]) + " ");
		output.write("\n");
		print filename;
		f.close();


	for filename in os.listdir(negPath): 
		f = open(os.path.join(negPath, filename), 'r');
		reviewMap = {};

		for word in f.read().split():
			if not word in dictionaryScore.keys():
				continue;
			if word in reviewMap.keys():
				reviewMap[word] = reviewMap[word] + 1;
			else:
				reviewMap[word] = 1;
		output.write('-1 ');
		for word in reviewMap.keys():
			value = reviewMap[word] * dictionaryScore[word];
			output.write(str(indexMap[word]) + ":" + str(reviewMap[word]*dictionaryScore[word]) + " ");
		output.write("\n");
		f.close();
		print filename;

	output.close();

# Prepares the training output to go to a file called "trainingOutput" and the test output to go to a file called "testingOutput"
prepareOutput("trainingOutput", "C:/Users/Lizzy/Documents/AI2/trainingTokens/tokens/pos/", "C:/Users/Lizzy/Documents/AI2/trainingTokens/tokens/neg/");
print "Moving on to testing output";
prepareOutput("testingOutput", "C:/Users/Lizzy/Documents/AI2/testTokens/pos/", "C:/Users/Lizzy/Documents/AI2/testTokens/neg/");