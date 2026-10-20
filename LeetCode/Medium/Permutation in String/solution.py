class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        s1_dict = {}
        s2_dict = {}

        p = 0
        while p < len(s1):
            s1_dict[s1[p]] = s1_dict.get(s1[p], 0) + 1
            p += 1

        i = 0
        j = 0

        while j < len(s2):
            s2_dict[s2[j]] = s2_dict.get(s2[j], 0) + 1

            if j - i + 1 == len(s1):
                if s1_dict == s2_dict:
                    return True

                s2_dict[s2[i]] -= 1

                if s2_dict[s2[i]] == 0:
                    del s2_dict[s2[i]]

                i += 1

            j += 1

        return False