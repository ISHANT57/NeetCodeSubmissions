class Solution:
    def topKFrequent(self, nums, k):

        # Step 1: Count frequency
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        result = []

        # Step 2: Find top k frequent elements
        for _ in range(k):

            max_freq = -1
            max_key = None

            # find element with maximum frequency
            for key in freq:
                if freq[key] > max_freq:
                    max_freq = freq[key]
                    max_key = key

            result.append(max_key)

            # remove selected element
            del freq[max_key]

        return result
