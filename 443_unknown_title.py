class Solution:
    def compress(self, chars):
        write = 0   # position to write compressed chars
        i = 0
        n = len(chars)

        while i < n:
            char = chars[i]
            count = 0

            # Count repeating characters
            while i < n and chars[i] == char:
                i += 1
                count += 1

            # Write character
            chars[write] = char
            write += 1

            # Write count if > 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write