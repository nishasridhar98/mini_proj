'''Processing Skewed Names'''
'''Problem Statement:
Students have entered their names with unnecessary special characters and numbers in-between.
Try and remove these without distorting the names.But do not remove the spaces between their first and last names.'''

name=[]
a=input("enter ur name: ")

for l in a:
	if l.isdigit():
		continue
	elif l.isalpha() or l==" ":
		name.append(l)
	else:
		continue

s=''.join(name)

print(s)