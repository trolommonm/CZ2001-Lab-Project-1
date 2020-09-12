from algo.naive import naiveStringMatcher
from algo.kmp import kmpStringMatcher
from algo.bmh import boyerMooreHorspoolStringMatcher
from timeit import default_timer as timer

import sys

if __name__ == "__main__":
    try:
        pattern = sys.argv[1]
        fnaFile = open(sys.argv[2])
        genomeSequence = ''.join(fnaFile.readlines()[1:]).replace('\n', '')

        # Using Naive Algorithm
        print('---------------------------------------------')
        print('Naive (Brute-Force) Algorithm:')
        print('')

        start = timer()
        indexOfOccurencesNaive = naiveStringMatcher(genomeSequence, pattern)
        end = timer()

        print('Indexes found:')
        if indexOfOccurencesNaive:
            print(indexOfOccurencesNaive) 
        else:
            print('No index of occurences found!')
        print('')

        print('Time elapsed: ' + str(end - start))

        print('---------------------------------------------')

        print('')

        # Using KMP Algorithm
        print('---------------------------------------------')
        print('Knuth-Morris-Pratt (KMP) Algorithm')
        print('')

        start = timer()
        indexOfOccurencesKmp = kmpStringMatcher(genomeSequence, pattern)
        end = timer()

        print('Indexes found:')
        if indexOfOccurencesKmp:
            print(indexOfOccurencesKmp)
        else:
            print('No index of occurences found!')
        print('')

        print('Time elapsed: ' + str(end - start))
        
        print('---------------------------------------------')
        print('')

        # Using BMH Algorithm
        print('---------------------------------------------')
        print('Boyer-Moore-Horspool (BMH) Algorithm')
        print('')

        start = timer()
        indexOfOccurencesBmh = boyerMooreHorspoolStringMatcher(genomeSequence, pattern)
        end = timer()

        print('Indexes found:')
        if indexOfOccurencesBmh:
            print(indexOfOccurencesBmh)
        else:
            print('No index of occurences found!')
        print('')

        print('Time elapsed: ' + str(end - start))
        
        print('---------------------------------------------')

    except IndexError:
        print('Please input your pattern and/or path to the .fna file!')
