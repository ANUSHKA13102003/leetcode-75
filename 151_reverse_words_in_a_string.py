class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()      # splits by whitespace and removes extra spaces
        return " ".join(words[::-1])