def computeBadHeuristicTableArray(pattern):
    # build an array with 5 elements, since a dna sequence will only contain 'A', 'T', 'G', 'C', 'U'
    # reserve index 0 for 'A', 1 for 'T', 2 for 'G', 3 for 'C', 4 for 'U'
    # first initialise all indexes to -1 (-1 represents the character does not exist in the pattern)
    n = len(pattern)
    badHeuristicArray = [-1] * 5
    for i in range(0, n):
        if pattern[i] == 'A':
            badHeuristicArray[0] = i
        elif pattern[i] == 'T':
            badHeuristicArray[1] = i 
        elif pattern[i] == 'G':
            badHeuristicArray[2] = i 
        elif pattern[i] == 'C':
            badHeuristicArray[3] = i 
        elif pattern[i] == 'U':
            badHeuristicArray[4] = i
        else:
        	print('Invalid character: ' + pattern[i] + ', detected in query string!')
            
    return badHeuristicArray

def indexOfChar(char):
    if char == 'A':
        return 0
    elif char == 'T':
        return 1
    elif char == 'G':
        return 2
    elif char == 'C':
        return 3
    elif char == 'U':
        return 4
    else:
        print('Invalid character: ' + char + ', detected in text string for DNA!')
    
def boyerMooreHorspoolStringMatcher(text, pattern):
    indexes = []
    m = len(text)
    n = len(pattern)
    
    badHeuristicArray = computeBadHeuristicTableArray(pattern)
    
    s = 0
    while (s < m - n + 1):
        i = n - 1
        
        while i >= 0 and pattern[i] == text[i + s]:
            i -= 1
            
        if i < 0:
            indexes.append(s)
            
            s += n - badHeuristicArray[indexOfChar(text[s + n])] if s + n < m else 1
        else:
            s += max(i - badHeuristicArray[indexOfChar(text[s + i])], 1)
                
    return indexes
    
            