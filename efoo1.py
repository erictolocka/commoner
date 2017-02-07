#count occurrences, keep or eliminate given specified constraint

import itertools, collections
from collections import Counter

def answer(data, n):
    ba = Counter(data)
    bb = dict((k, v) for (k, v) in ba.items() if v < n+1)
    bc = [x for x in data if x in bb]
    print(bc)

#test cases
answer([1, 2, 3, 4], 6)
answer([1, 3, 5, 6, 7, 7, 7, 7, 8, 9], 2)