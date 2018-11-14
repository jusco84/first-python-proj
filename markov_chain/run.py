import os
from markov_python.cc_markov import MarkovChain

mc = MarkovChain()
#print os.getcwd()
mc.add_file("test.txt")
print mc.generate_text(5)