class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Start with getting rows and col count
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        from collections import deque

        # BFS - queue
        #Time: O(M*N), Space: O(min(M,N))       
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    queue = deque([(i, j)]) # Start with the current cell
                    grid[i][j] = '0'  # mark visited
                    while queue: 
                        r, c = queue.popleft() #If you make it .pop(), it'll be DFS (Stack). .popleft() is BFS (Queue).
                        # Check 4 directions
                        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:  
                            nr, nc = r + dr, c + dc 
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'  # mark visited
                                queue.append((nr, nc)) # Add to queue 
        return islands

        """
        # DFS - recursion. Drill down all connected lands: 
        #Time: O(M*N), Space: O(M*N) in worst case (grid filled with lands)
        def dfs(graph, a, b):
            if a < 0 or b < 0 or a >= rows or b >= cols or grid[a][b] == '0':
                return
            graph[a][b] = '0'
            dfs(graph, a-1, b)
            dfs(graph, a+1, b)
            dfs(graph, a, b-1)
            dfs(graph, a, b+1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(grid, i, j)
        return islands
        """