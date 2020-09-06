from naive import naiveStringMatcher
from kmp import kmpStringMatcher
from timeit import default_timer as timer

import sys

if __name__ == "__main__":
    try:
        pattern = sys.argv[1]
        fnaFile = open(sys.argv[2])
        genomeSequence = ''.join(fnaFile.readlines()[1:]).replace('\n', '')

        print('----------------')
        print('Naive Algorithm:')
        print('----------------')
        print('Indexes found: ')
        print(naiveStringMatcher(genomeSequence, pattern))
        print('------------------------------------------------')
        print('Calculating total time taken for 50 searches...')
        totalTimeElapsed = 0
        for i in range(50):
            start = timer()
            naiveStringMatcher(genomeSequence, pattern)
            end = timer()
            totalTimeElapsed += end - start
        averageTimeElapsed = totalTimeElapsed/50
        print('Calculating average time taken for 1 search...')
        print('Average time taken for Naive (Brute-Force) Algorithm: ', averageTimeElapsed, ' seconds')
        print('----------------------------------------------------------------------------------')

        print('----------------------------')
        print('Knuth-Morris-Pratt Algorithm')
        print('----------------------------')
        print('Indexes found: ')
        print(kmpStringMatcher(genomeSequence, pattern))
        print('------------------------------------------------')
        print('Calculating total time taken for 50 searches...')
        totalTimeElapsed = 0
        for i in range(50):
            start = timer()
            kmpStringMatcher(genomeSequence, pattern)
            end = timer()
            totalTimeElapsed += end - start
        averageTimeElapsed = totalTimeElapsed/50
        print("Calculating average time taken for 1 search...")
        print('Average time taken for KMP Algorithm: ', averageTimeElapsed, ' seconds')
        print('-----------------------------------------------------------')

    except IndexError:
        print('Please input your pattern and/or path to the .fna file!')
