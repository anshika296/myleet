class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        #build the graph and calculate indegree
        count=0
        indegree=[0]*numCourses
        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course]+=1
        #put indegree 0 courses in queue
        queue=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        #start bfs
        while queue:
            course=queue.popleft() #marking as course done
            count+=1
            for neighbor in graph[course]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        return count==numCourses

        

