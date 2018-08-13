'''Processing Skewed Names'''
'''Problem Statement:
Students have entered their names with unnecessary special characters and numbers in-between.
Try and remove these without distorting the names.But do not remove the spaces between their first and last names.'''

a=input("enter ur name: ")
def corrector():
	name=[]
	for l in a:
		if l.isdigit():
			continue
		elif l.isalpha() or l==" ":
			name.append(l)
		else:
			continue

	return ''.join(name)

mod_name=corrector()
print(mod_name)
