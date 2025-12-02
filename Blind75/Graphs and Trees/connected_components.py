class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        from collections import defaultdict
        visited = set()
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        print(graph)
        # Queue - BFS
        from collections import deque
        c = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                queue = deque([i])
                while queue:
                    node = queue.popleft() # Make it .pop() for LIFO (Stack)! .popleft() for FIFO (Queue). 
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                c += 1
        return c

        # # Stack - DFS
        # for i in range(n):
        #     if i not in visited:
        #         stack = [i]
        #         visited.add(i)
        #         while stack:
        #             node = stack.pop()
        #             for neighbor in graph[node]:
        #                 if neighbor not in visited:
        #                     visited.add(neighbor)
        #                     stack.append(neighbor)
        #         components += 1