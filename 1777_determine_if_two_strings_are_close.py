from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Length must be same
        if len(word1) != len(word2):
            return False

        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # Same unique characters + same frequency distribution
        return set(freq1.keys()) == set(freq2.keys()) and \
               sorted(freq1.values()) == sorted(freq2.values())