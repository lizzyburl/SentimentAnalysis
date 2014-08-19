import os;
import json;

# This was added to improve the efficiency of the program. Combines two dictionaries into one
def combineDictionaries (bigDict, miniDict):
	for word in miniDict.keys():
		if word in posDict.keys():
			bigDict[word] = posDict[word] + miniDict[word];
		else:
			bigDict[word] = miniDict[word];
	return bigDict;

# Gets rid of entries that should not be in the dictionary to 
# (1) Decrease the size
# (2) Get rid of weird unicode entries that don't like being converted to json and back
def clearBadEntries(dictionary):
	badEntries = ["the", "and", "a", "that", ".", ",", "they", ";", "[", "]", "(", ")", "\n", "\t"];
	for entry in badEntries:
		if entry in dictionary.keys():
			del dictionary[entry];
	for key in dictionary.keys():			
		if not all(ord(c)<128 for c in key):
			del dictionary[key];
			print key;
			continue;
		if dictionary[key] == 1:
			del dictionary[key];
			continue;
	return dictionary;

# Initialize the dictionary for positive reviews
posDict = {}; 
totalWords = 0;

# Get all words from positive reviews
posPath = "C:/Users/Lizzy/Documents/AI2/trainingTokens/tokens/pos/";

# Mini dict gets filled every 30 reviews and is then joined with the big dictionary
miniDict = {};
dictMax = 30;
dictCount = 0;

for filename in os.listdir(posPath): 
	f = open(os.path.join(posPath, filename), 'r');

	# Combining reviews
	if dictCount == dictMax:
		dictCount = 0;
		posDict = combineDictionaries(posDict, miniDict);
		miniDict = {};

	for word in f.read().split():
		totalWords = totalWords + 1;
		if word in miniDict.keys():
			miniDict[word] = miniDict[word] + 1;
		else:
			miniDict[word] = 1;
	f.close();
	print filename;
	dictCount = dictCount + 1;

posDict = combineDictionaries(posDict, miniDict);


negPath = "C:/Users/Lizzy/Documents/AI2/trainingTokens/tokens/neg/";
# Get all words
negDict = {};
miniDict = {};
dictCount = 0;
for filename in os.listdir(negPath): 
	f = open(os.path.join(negPath, filename), 'r');

	if dictCount == dictMax:
		dictCount = 0;
		negDict = combineDictionaries(negDict, miniDict);
		miniDict = {};

	for word in f.read().split():
		totalWords = totalWords + 1;
		if word in miniDict.keys():
			miniDict[word] = miniDict[word] + 1;
		else:
			miniDict[word] = 1;
	f.close();
	print filename;
	dictCount = dictCount + 1;

negDict = combineDictionaries(negDict, miniDict);

# Combine the dictionaries made from positive and negative values
dictionary = combineDictionaries(posDict, negDict);
dictionary = clearBadEntries(dictionary);

print(len(dictionary))

#Dumb dictionary into a json object
with open("dictionary.json", "wb") as fp:
	json.dump(dictionary ,fp, encoding='latin1') ;

