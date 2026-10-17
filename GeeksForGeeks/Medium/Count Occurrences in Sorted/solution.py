class Solution:
    def countFreq(self, arr, target):
        def boundary(first):
            low = 0
            high = len(arr) - 1
            ans = -1

            while low <= high:
                mid = low + (high - low) // 2

                if arr[mid] == target:
                    ans = mid

                    if first:
                        high = mid - 1
                    else:
                        low = mid + 1

                elif arr[mid] < target:
                    low = mid + 1

                else:
                    high = mid - 1

            return ans

        first = boundary(True)

        if first == -1:
            return 0

        last = boundary(False)

        return last - first + 1