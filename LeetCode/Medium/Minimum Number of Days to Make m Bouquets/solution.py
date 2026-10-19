class Solution(object):
    def canmakebouquet(self,bloomday,mid,k):
        consecutive=0
        bouquet_count=0
        for i in range(len(bloomday)):
            if bloomday[i]<=mid:
                consecutive+=1
            else:
                consecutive=0
            if consecutive==k:
                bouquet_count+=1
                consecutive=0
        return bouquet_count

    def minDays(self,bloomday,m,k):
        n=len(bloomday)
        if m*k>n:
            return -1
        start=min(bloomday)
        end=max(bloomday)
        res=-1
        while start<=end:
            mid=start+(end-start)//2
            if self.canmakebouquet(bloomday,mid,k)>=m:
                res=mid
                end=mid-1
            else:
                start=mid+1
        return res