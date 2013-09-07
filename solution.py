f = open('mowords.txt', 'r')
max_word_length = 28
test_string = "etaelehoyrnrsweeneiornvtsdelreiolrertsrhotruongpmghwsihlxtdeelaneeetldosheeralithtndareluttelderrocltaeiwrtodeoeyladfswpsremeucraddfvrntaiansudynaeytnaidthioicheegblyoeielsvvneoliiwudveieuaoaodptetpurrdeieecnohasapiwdoehltflsbohlamthioeosistssbstwe"
testing_chunk = ""
last_index = 0

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
	found = None
	for line in f:
		if word == line.strip('\r\n'):
			return line.strip('\r\n')
	return False;

def parseScrambledText(test_string):
	start_index = 0
	end_index = 2
	last_index = len(test_string) - 1
	while end_index <= last_index:
		chunk = getTextChunk(test_string, start_index, end_index)
		anagrams = anagramsForChunk(chunk)
		word_found = False
		for word in anagrams:
			print word
			dictionary_match = findDictionaryMatch(word)
			if dictionary_match:
				print "Match!"
				print word, dictionary_match
				word_found = True
				# I have been working mostly in Javascript, so assigning string values below has been tricky for me.
				# test_string[start_index:end_index] = findDictionaryMatch(word)
				# line = line[:10].replace(';', ':') + line[10:]
				# test_string.replace(chunk, dictionary_match) # This will replace all instances, but in this problem this is not problematic.
				new_string = test_string[:start_index] + dictionary_match + test_string[end_index:]
				test_string = new_string
				start_index = end_index + 1
				end_index = start_index + 2
				break
		if word_found is False and end_index == max_word_length:
			char_at_start = test_string[start_index]
			new_string = test_string[:start_index].replace(char_at_start, '-') + test_string[start_index:]
			test_string = new_string
			start_index += 1
			end_index = start_index + 2
		if word_found is False and end_index != max_word_length:
			end_index += 1
	print test_string

parseScrambledText(test_string)
