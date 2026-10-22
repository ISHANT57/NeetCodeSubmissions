class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels = "aeiou"
        i = 0
        j = 0
        total = 0
        max_count = 0

        while j < len(s):
            if s[j] in vowels:
                total = total + 1

            if j - i + 1 > k:
                if s[i] in vowels:
                    total = total - 1
                i += 1

            if j - i + 1 == k:
                if total > max_count:
                    max_count = total

            j += 1

        return max_count