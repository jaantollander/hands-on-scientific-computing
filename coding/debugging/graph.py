from collections import defaultdict, deque

class Graph:
    def __init__(self, edges):
        self.__neighbours = defaultdict(set)
        for v1, v2 in edges:
            self.__neighbours[v1].add(v2)
            self.__neighbours[v2].add(v1)

    def neighbours(self, vertex):
        return self.__neighbours[vertex]

    def eccentricity(self, vertex):
        """
        The eccentricity of a vertex is the biggest shortes path 
        between that vertex and all the other vertices.
        
        BFS is used to calculate eccentricity of a given vertex.

        Args:
            vertex - graph vertex (int)

        Returns:
            maxdist - maximum distance between vertex and
            all other vertices (int)
        """

        seen = dict.fromkeys(self.__neighbours.keys(),
                False)
        q = deque()

        # Start from the given vertex
        q.append((vertex, 0))
        seen[vertex] = True
        maxdist = 0

        # Start the BFS
        while q:
            v, dist = q.popleft()
            vertices = self.neighbours(v)
            maxdist = max(maxdist, dist)
            for neighbour in vertices:
                if not seen[neighbour]:
                    q.append((neighbour, dist))
                    seen[neighbour] = True

        # All the vertices should be seen in a connected graph
        for v in self.__neighbours.keys():
            if not seen[v]:
                raise ValueError("eccentricity is only \
                            defined for connected graphs")

        return maxdist

    def diameter(self):
        """
        The diameter of a graph is the longest shortest path
        between any two vertices of the graph.
        
        Returns:
            The biggest eccentricity among all vertices (int)
        """

        vertices = set(self.__neighbours.keys())
        return max([self.eccentricity(v) for v in vertices])
