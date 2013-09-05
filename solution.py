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
		return string
	def checkDuplicates(array):
		# Subroutine for selecting only unique anagram values
		res = []
		seen = {}
		for i in range(0, len(array)): # i=0; i < len(array); i++:
			temp_key = array[i][0];
			print temp_key
			if hasattr(seen, temp_key):
			# if not seen[array[i]]:
				print "MATCH"
				seen.temp_key = True
				res.push(temp_key)
		return res
	if isinstance(string, str):
		string = string.split()
	if index >= len(string):
		return ret
	for i in range(index, len(string)): # = index; i < len(string); i++:
		ret.append(placeLetters(string, index, i))
	return checkDuplicates(anagramsForChunk(string, index+1, ret))

def findDictionaryMatch(shuffled_testing_chunk):
	for line in f:
		if shuffled_testing_chunk == line.strip('\r\n'):
			return line.strip('\r\n')
		else:
			return False

test =  anagramsForChunk("cat", 0, [])
print test
# findDictionaryMatch("aardvark")