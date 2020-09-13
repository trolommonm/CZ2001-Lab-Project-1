def computeLpsArray(pattern):
    i = 0
    lpsArray = [0] * len(pattern)
    for k in range(1, len(lpsArray)):
        if pattern[i] == pattern[k]:
            lpsArray[k] = i + 1
            i += 1
            
    return lpsArray
            
def kmpStringMatcher(text, pattern):
    indexes = []
    lpsArray = computeLpsArray(pattern)
    m = len(text)
    n = len(pattern)
    j = 0
    i = 0
    while (i < m):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == n:
            indexes.append(i - n)
            j = lpsArray[j-1]
        elif i < m and text[i] != pattern[j]:
            if j > 0:
                j = lpsArray[j-1]
            else:
                i += 1
                
    return indexes
        
