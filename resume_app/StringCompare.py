import re

def funcCompDescrAndSkill(Listing, Skills):
	chars = [',','!',".",";","?"]
	noWords = ['a', 'the', 'of', 'on', 'at', 'with ', 'in', 'under', 'over']#add more here
	myListing = (Listing.translate(None, ''.join(chars))).lower()
	temp_regex = re.compile(r'\b%s\b' % r'b|\b'.join(map(re.escape, noWords)))
	myListing= temp_regex.sub(' ', myListing)
	mySkills = (Skills.translate(None, ''.join(chars))).lower()
	temp_regex = re.compile(r'\b%s\b' % r'b|\b'.join(map(re.escape, noWords)))
	mySkills= temp_regex.sub(' ', myListing)
	
		

	nextString = None
	total = 0;
	wordListing = myListing.split()
	wordSkills = mySkills.split()
	for i in wordListing:
		for j in wordSkills:
			total += edit_distance(i,j)
	normalizedRatio = total*1.0/len(myListing)
	return normalizedRatio

def matchWords(Listing, Skills):
	chars = [',','!',".",";","?"]
	#noWords = ['a', 'the', 'of', 'on', 'at', 'with ', 'in', 'under', 'over']#add more here
	myListing = (Listing.translate(None, ''.join(chars))).lower()
	mySkills = (Skills.translate(None, ''.join(chars))).lower()
	nextString = None
	total = 0;
	wordListing = myListing.split()
	wordSkills = mySkills.split()
	for i in wordListing:
		for j in wordSkills:
			if i == j:
				total += 1
	return total
#test line:
#print(funcCompDescrAndSkill("A member of the Free Syrian Army stands guard at a checkpoint they took over early on Monday after clashes with pro-government forces in Salqin city in Idlib October 22, 2012. ", "Hi guys! THis sentence has nothing to do with the previous one!"))






