'''Fixing Blog Titles
A title to a blog is written with each letter of the first word as a capital letter. 
But no spaces are given.Try and figure out the words and separate them by spaces.
'''

n =[]
words = input("enter the title: ")

n.append(words[0])

for l in words[1:]:
	if l.isupper():
		n.append(" ")
		n.append(l)
	else:
		n.append(l)

s=''.join(n)
print(s)