from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr):
        freq = Counter(arr)          # count frequency of each number
        occurrences = list(freq.values())

        return len(occurrences) == len(set(occurrences))