class Solution:

    def encode(self, strs):
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            # Find the delimiter '#'
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])  # length of the string
            i = j + 1

            # Extract the string
            res.append(s[i:i + length])
            i = i + length

        return res
