class Solution:
    def canmid(self, arr, mid, k):
        prev = arr[0]
        cows = 1

        for i in range(1, len(arr)):
            if arr[i] - prev >= mid:
                cows += 1
                prev = arr[i]
                if cows == k:
                    return True

        return False

    def aggressiveCows(self, arr, k):
        arr.sort()
        low, high = 1, arr[-1] - arr[0]

        while low < high:
            mid = (low + high + 1) // 2
            if self.canmid(arr, mid, k):
                low = mid
            else:
                high = mid - 1

        return low