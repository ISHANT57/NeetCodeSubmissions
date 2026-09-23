class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        g=[[] for i in range(n)]

        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        seen=set()
        def dfs(u):
            seen.add(u)

            for v in g[u]:
                if v not in seen:
                    dfs(v)

        ans=0

        for i in range(n):
            if i not in seen:
                ans+=1
                dfs(i)
        
        return ans
        
        