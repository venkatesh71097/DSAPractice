class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Conditions to meet:
            # 1. N vertices -> N-1 edges - Check for cyclical connections
            # 2. Am I able to traverse thru all nodes from the start? Or is there a disconnect/break? Basically, can I get to 'n' nodes from the 0th node. 
        if len(edges) != n-1:
            return False
        from collections import defaultdict
        graph = defaultdict(list)
        # Edges: [[0,1],[0,2],[0,3],[1,4]]
        # We need to build an adjacency list...
        # {0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0], 4: [1]})        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  
            
        # Recursive...
        visited = set()
        # Start dfs
        def dfs(node, parent):
            # No need of any checks as node added for the first time
            visited.add(node)
            # Traverse thru the adjacency list
            for neighbor in graph[node]:
                # 0 -> 1 (1-> 0 is also possible, but let's not duplicate count - primary purpose of having parent node passed in!)
                if neighbor == parent:
                    continue
                # Iff the node ain't visited, you trigger the dfs
                if neighbor not in visited:
                    dfs(neighbor, node)
        # Have the start node as 0 and parent as -1 (meaning, no parent as yet)
        dfs(0, -1)
        # If the no. of nodes equal the visited nodes, it's not a cyclical graph
        return len(visited) == n

        # Iterative...
        # queue = deque([0])
        # visited = set()
        # while queue:
        #     node = queue.popleft()
        #     for neighbor in graph[node]:
        #         if neighbor not in visited:
        #             visited.add(neighbor)
        #             queue.append(neighbor)
        # return len(visited) == n