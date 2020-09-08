def naiveStringMatcher(text, pattern):
    indexes = []
    m = len(text)
    n = len(pattern)
    for i in range(0, m - n):
        for j in range(0, n):
            if text[i+j] != pattern[j]:
                break
            
            if j == n - 1 and text[i+j] == pattern[j]:
                indexes.append(i)
                
    return indexes
