class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        graph=[[] for i in range(n)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen=set()
        for i in restricted:

            seen.add(i)
        
        visited=[False]*(n)
        queue=deque()
        queue.append(0)
        visited[0]=True
        count=1

        while queue:
            u=queue.popleft()

            if u in seen:
                continue
            for v in graph[u]:
                if not visited[v]:
                    if v not in seen:

                        visited[v]=True
                        count+=1
                        queue.append(v)
        return count