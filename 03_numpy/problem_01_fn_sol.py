"""
You should write all of your functions in this file. That way we can
use parts of this file later in the course.
"""
# this line imports numpy as np, csv, os, etc.
from util import *
################################ Constants ####################################
# degree -> salaries
# college -> salaries
# Note that we do not save the percent change between starting/mid salary.
START_SAL, MED_SAL, MID_10, MID_25, MID_75, MID_90 = range(6)

################################ Loading ######################################
"""
Write your load_degrees(...) function here.
Hints:
- use f.readline() to read the first line, then
- use csv.reader() to parse the rest of the file
- use s.replace(old, new) to remove commas from the dollar amounts
- use s.strip(characters) to remove leading/trailing characters like $ sign
- use items.index(s) to find the index of a particular string.
- use items.pop(n) to remove the nth element from the string (indexed from 0)
- if your list of strings is called line,
       use line[1:] to access the second element onwards
"""
def load_degrees(degree_fpath):
	degree_dict = {}
	headers = []
	#header = headies.strip().split(',') for headies in headers
	with open(degree_fpath, 'r') as f:
		headers = f.readline()
		headers = headers.strip().split(',')
		poptarget = headers.index('Percent change from Starting to Mid-Career Salary')
		headers.pop(poptarget)
		headers.pop(0)
		#pull percentage index for headers and apply with the .pop command in the for loop
		for line in csv.reader(f):
			line = [degree.strip('$').replace(',', '') for degree in line]
			line.pop(poptarget)
			key = line[0]
			START_SAL, MED_SAL, MID_10, MID_25, MID_75, MID_90 = line[1:]
			degree_dict[key] = [float(START_SAL), float(MED_SAL), float(MID_10), float(MID_25), float(MID_75), float(MID_90)]
			
			
	return headers, degree_dict

"""
Write your load_colleges(...) function here.
Hints:
- some schools appear in both CSVs, but their salary values are the 
  same in both sheets. However, you should make sure you still parse those 
  lines as they will contain information about the school region or type.
- the headers for the college_dict values will
  be the same as those for the degree_dict from load_degrees(...), so we
  do not need to redefine those.
- ```type``` is a keyword, so use a different name (e.g., college_type)
- N/A should be represented as -1.
- For the latter two dictionaries, check if the type/region exists in
  the dictionary first. If it doesn't, create an empty list as the value.
  Then add the college name to the list.
- If a school already exists in college_dict, you can either use the 
  ```continue``` keyword to go to the next line, or you can encapsulate what
  you have in a conditional.
"""
def load_colleges(salaries_type_fpath, salaries_region_fpath):
	college_dict, type_to_colleges, region_to_colleges = {}, {}, {}
	with open(salaries_type_fpath, 'r') as file1:
		file1.readline()
		for line in csv.reader(file1):
			key1 = line[0]
			key2 = line[1]
			line[2:] = [salary.strip('$').replace(',', '').replace('N/A', '-1') for salary in line[2:]]
			#print(line)
			#print(key1)
			#print(key2)
			START_SAL, MED_SAL, MID_10, MID_25, MID_75, MID_90 = line[2:]
			college_dict[key1] = [float(START_SAL), float(MED_SAL), float(MID_10), float(MID_25), float(MID_75), float(MID_90)]
			if key2 not in type_to_colleges:
				type_to_colleges[key2] = []
			type_to_colleges[key2].append(key1)
	with open(salaries_region_fpath, 'r') as file2:
		file2.readline()
		for line in csv.reader(file2):
			key3 = line[0]
			key4 = line[1]
			line[2:] = [salary.strip('$').replace(',', '').replace('N/A', '-1') for salary in line[2:]]
			#print(line)
			#print(key3)
			#print(key4)
			START_SAL, MED_SAL, MID_10, MID_25, MID_75, MID_90 = line[2:]
			if key3 not in college_dict:
				college_dict[key3] = [float(START_SAL), float(MED_SAL), float(MID_10), float(MID_25), float(MID_75), float(MID_90)]
			if key4 not in region_to_colleges:
				region_to_colleges[key4] = []
			region_to_colleges[key4].append(key3)
			

	return college_dict, type_to_colleges, region_to_colleges

"""
Write your write_colleges(...) function here.
The CSV should be sorted by the name of the college.
Hints:
- Create a new dictionary with college names as the keys, and
  the college region and college type as values.
- The default is N/A for both college region and college type.
- Go through the college keys in **sorted order** and create
  a list of lists, where each sublist is a row of the target csv.
- Use the write_csv function from util that you implemented in lecture.
"""
def write_colleges(college_fpath, salary_headers, college_dict, type_to_colleges, region_to_colleges):
	tups = []
	college_keys = [k for k, v in college_dict.items()]
	sorted_college_list = sorted(college_keys)
	master_dict = {}
	for college in sorted_college_list:
		key1 = college
		college_type = 'N/A'
		college_region = 'N/A'
		for k, v in college_dict.items():
			if k == key1:
				START_SAL, MED_SAL, MID_10, MID_25, MID_75, MID_90 = v
		for k, v in type_to_colleges.items():
			if key1 in v:
				college_type = k
		for k, v in region_to_colleges.items():
			if key1 in v:
				college_region = k
		master_dict[key1] = [college_region, college_type, float(START_SAL), float(MED_SAL), float(MID_10), float(MID_25), float(MID_75), float(MID_90)]
	full_list = []
	for college, values in master_dict.items():
		templist = [college] + values
		full_list.append(templist)
	new_header = ['School Name'] + ['Region'] + ['School Type'] + salary_headers
	tups = [new_header] + full_list
	write_csv(college_fpath, tups, log=True)

