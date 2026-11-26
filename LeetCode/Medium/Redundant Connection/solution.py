class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n=len(edges)
        parent=[]

        for i in range(n+1):
            parent.append(i)
        
        def find(x):
            while x!=parent[x]:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        
        ans=[]
        for u,v in edges:
            a=find(u)
            b=find(v)

            if a==b:
                return [u,v]
            
            parent[b]=a
        return -1