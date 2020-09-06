from naive import naiveStringMatcher
from kmp import kmpStringMatcher

import sys

if __name__ == "__main__":
	try:
		pattern = sys.argv[1]
		fnaFile = open(sys.argv[2]) 
		genomeSequence = ''.join(fnaFile.readlines()[1:]).replace('\n', '')

		print('Naive Algorithm:')
		print(naiveStringMatcher(genomeSequence, pattern))

		print('Knuth-Morris-Pratt Algorithm')
		print(kmpStringMatcher(genomeSequence, pattern))
	except IndexError:
		print('Please input your pattern and/or path to the .fna file!')
