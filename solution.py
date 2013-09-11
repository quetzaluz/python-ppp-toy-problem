f = open('mowords.txt', 'r')
max_word_length = 28
test_string = "etaelehoyrnrsweeneiornvtsdelreiolrertsrhotruongpmghwsihlxtdeelaneeetldosheeralithtndareluttelderrocltaeiwrtodeoeyladfswpsremeucraddfvrntaiansudynaeytnaidthioicheegblyoeielsvvneoliiwudveieuaoaodptetpurrdeieecnohasapiwdoehltflsbohlamthioeosistssbstwe"

def getTextChunk(string, start_index=0, end_index=2):
	# May want to refactor this to be a subroutine within a function that can be recursively called.
	substring = string[start_index:end_index]
	return substring

def anagramsForChunk(string, index=0, ret=[]):
	# Recursive function for getting all anagrams for a testing chunk
	def placeLetters(string, index1, index2):
		# Subroutine for trying different letter placements.
		if index1 != index2:
			temp = string[index1]
			string[index1] = string[index2]
			string[index2] = temp
		return ''.join(string)
	def checkDuplicates(array):
		seen = set()
		result = []
		for word in array:
			if word not in seen: 
				seen.add(word)
				result.append(word)
		return result
	if isinstance(string, str):
		string_letters = list(string)
	else:
		string_letters = string
	if index >= len(string_letters):
		return ret
	for i in range(index, len(string_letters)): # = index; i < len(string); i++:
		ret.append(placeLetters(string_letters, index, i))
	anagramsForChunk(string_letters, index+1, ret)
	return checkDuplicates(ret)

def findDictionaryMatch(word):
	# Iterate through dictionary and see if input word matches a dictionary word.
	found = False
	for line in f:
		if word == line.strip('\r\n'):
			found = line.strip('\r\n')
	f.seek(0);
	return found;

def parseScrambledText(test_string):
	# Primary function that unscrambles testing string, calls helper functions.
	start_index = 0
	end_index = 2
	last_index = len(test_string) - 1
	while end_index <= last_index:
		word_found = False
		word_found_length = 0
		while end_index <= min((start_index + max_word_length), last_index):
			chunk = getTextChunk(test_string, start_index, end_index)
			anagrams = anagramsForChunk(chunk, 0 , [])
			for word in anagrams:
				dictionary_match = findDictionaryMatch(word)
				if dictionary_match:
					print "Matched: " + dictionary_match
					word_found = dictionary_match
					word_found_end_index = end_index
					break
			end_index += 1
		if word_found is False:
			new_string = test_string[:start_index] + '-' + test_string[start_index+1:]
			test_string = new_string
			start_index += 1
			end_index = start_index + 1
		else:
			print "Word " + word_found + " found, incrementing..."
			new_string = test_string[:start_index] + word_found.capitalize() + test_string[word_found_end_index:]
			test_string = new_string
			start_index = word_found_end_index
			end_index = start_index + 1
	print test_string

parseScrambledText(test_string)
