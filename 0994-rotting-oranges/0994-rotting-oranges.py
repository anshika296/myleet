class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        #keep track of rotten oranges and keep track of fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c))
                if grid[r][c]==1:
                    fresh+=1
        minutes=0
        #directions
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        #bfs
        while queue and fresh>0:# while queue is not empty and there are fresh oranges
            for _ in range(len(queue)):
                r,c=queue.popleft()
                for dr,dc in directions:
                    nr=dr+r
                    nc=dc+c
                    if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        fresh-=1
                        queue.append((nr,nc))
            minutes+=1
        if fresh==0:
            return minutes
        else:
            return -1


        