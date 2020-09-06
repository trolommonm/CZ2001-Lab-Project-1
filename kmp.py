def computeLpsArray(pattern):
    i = 0
    j = 1
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
            if j == n - 1:
                indexes.append(i - n + 1)
                j = lpsArray[max(j - 1, 0)]
            else:
                j += 1
                i += 1
        else:
            if j > 0:
                j = lpsArray[max(j - 1, 0)]
            else:
                i += 1
                
    if not indexes:
        return "---None---"
    else:
        return indexes
        
