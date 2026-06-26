class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0

        # Count vowels in first window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        # Slide window
        for i in range(k, len(s)):
            # Remove left character
            if s[i - k] in vowels:
                count -= 1

            # Add new right character
            if s[i] in vowels:
                count += 1

            max_count = max(max_count, count)

        return max_count