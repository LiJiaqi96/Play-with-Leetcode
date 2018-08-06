class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def judge(vertice, color):
            if vertice in colormap:
                if colormap[vertice] == color:
                    return True  
                else:
                    return False
            else:
                colormap[vertice] = color
                for u in graph[vertice]:
                    if not judge(u, (color+1)%2):
                        return False
                return True

        colormap = {}
        for vertice in range(len(graph)):
            if vertice not in colormap:
                if judge(vertice, 0) is False:
                    return False

        return True
