class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if newColor==image[sr][sc]:
            return image
        start = image[sr][sc]
        def go_deeper(location):
            image[location[0]][location[1]] = newColor
            for i,j in [[1,0],[-1,0],[0,1],[0,-1]]:
                if(location[0]+i < 0 or location[0]+i >= len(image)):
                    pass
                elif(location[1]+j < 0 or location[1]+j >= len(image[0])):
                    pass
                elif(image[location[0]+i][location[1]+j] != start):
                    pass
                else:
                    go_deeper([location[0]+i,location[1]+j])
        go_deeper([sr,sc])
        return image
