"""
Codecademy Pro
Learn Python
FInal Project
Markov Chain Text Generator
15 November 2018

"""

"""
import module here
"""

import fetch_data
from markov_python.cc_markov import MarkovChain


#initiate Markov Chain generator
mc = MarkovChain()
#links to a book
book = {"https://www.gutenberg.org/files/74/74-0.txt" : "The Adventures of Tom Sawyer"}

print
print "Welcome to quote generator from famous books."
print
print "Accessing the book..."
for link in book:
	print "The famous book is " + book[link]
	mc.add_string(fetch_data.get_data(link))


length = 10

while True:
	try:
		temporary = mc.generate_text(length)
		formatted = " ".join(temporary)
		print ("Passage #1: " + formatted)
		print
		break
	except UnicodeEncodeError:
		pass