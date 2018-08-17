# A great python library for reading and writing data.
import csv


# This is example code that loads each of the CSV files.
# Feel free to use this code in your solution. Don't forget
# to import csv
def main():
	learningOutcomes = loadLearningOutcomes()
	backgrounds = loadBackgrounds()

	outputList(learningOutcomes)
	outputList(backgrounds)


# Example loading for the problem on A/B testing.
# Returns a list of student data. Each student is a list
# with three elements: their id, their activity and their 
# learning outcome.
def loadLearningOutcomes():
	reader = csv.reader(open('learningOutcomes.csv'))
	learningOutcomes = []
	for row in reader:
		studentId = row[0]
		activity = row[1]
		outcome = float(row[2]) # make sure outcome is a number!
		learningOutcomes.append([studentId, activity, outcome])
	return learningOutcomes


# Example loading for the problem on A/B testing.
# Returns a list of student backgrounds. Each student is a list
# with two elements: their id, their background.
def loadBackgrounds():
	reader = csv.reader(open('background.csv'))
	backgrounds = []
	for row in reader:
		backgrounds.append(row)
	return backgrounds


# Example code for looping over a list in python. This 
# function prints out the list
def outputList(l):
	for row in l:
		print(row)
	print('\n----\n')


if __name__ == '__main__':
	main()
