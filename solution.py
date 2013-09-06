f = open('mowords.txt', 'r')
max_length = 28
min_length = 2
test_string = "etaelehoyrnrsweeneiornvtsdelreiolrertsrhotruongpmghwsihlxtdeelaneeetldosheeralithtndareluttelderrocltaeiwrtodeoeyladfswpsremeucraddfvrntaiansudynaeytnaidthioicheegblyoeielsvvneoliiwudveieuaoaodptetpurrdeieecnohasapiwdoehltflsbohlamthioeosistssbstwe"
testing_chunk = ""
last_index = 0

# while len(testing_chunk) <= 7:

# for line in f:
	# if len(line.strip('\r\n')) > max_length:
	# 	max_length = len(line.strip('\r\n'))
	
def anagramsForChunk(string, index, ret):
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

def findDictionaryMatch(shuffled_testing_chunk):
	for line in f:
		if shuffled_testing_chunk == line.strip('\r\n'):
			return line.strip('\r\n')
		else:
			return False

print anagramsForChunk("cat", 0, [])
# findDictionaryMatch("aardvark")