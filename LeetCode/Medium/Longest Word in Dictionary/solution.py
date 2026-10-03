class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        ans=""
        wordsset=set(words)

        for word in words:
            prefix=""
            valid=True

            for ch in word:
                prefix+=ch

                if prefix not in wordsset:
                    valid=False
                    break
            if valid:
                if len(ans)<len(word):
                    ans=word

                elif len(ans)==len(word) and ans>word:
                    ans=word

        return ans
        