# File: bday.py
# A simple program illustrating birthday paradox.

import random
classSize = 45
numTrials = 1000
dupeCount = 0

for trial in range(numTrials):
	birthdayList = []
	for i in range(classSize):
		newBDay = random.randrange(365)
		birthdayList.append(newBDay)
	
	foundDupe = False
	for num in birthdayList:
		if birthdayList.count(num) > 1:
			foundDupe = True
		
	if foundDupe == True:
		dupeCount = dupeCount + 1
	
prob = dupeCount / numTrials
print("The probability of a shared birthday in a class of ", classSize, " is ", prob)
