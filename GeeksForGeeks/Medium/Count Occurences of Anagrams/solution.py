class Solution:
    def search(self, pat, txt):
        n = len(txt)
        k = len(pat)

        if k > n:
            return 0

        pat_freq = {}
        window_freq = {}

        p = 0
        while p < k:
            pat_freq[pat[p]] = pat_freq.get(pat[p], 0) + 1
            p += 1

        i = 0
        j = 0
        count = 0

        while j < n:
            window_freq[txt[j]] = window_freq.get(txt[j], 0) + 1

            if j - i + 1 == k:
                if window_freq == pat_freq:
                    count += 1

                window_freq[txt[i]] -= 1

                if window_freq[txt[i]] == 0:
                    del window_freq[txt[i]]

                i += 1

            j += 1

        return count