class Solution(object):
    def tempArea(self, heights):
        heights.append(0)
        stack = [-1]
        temp_area = 0
        for idx, height in enumerate(heights):
            while height < heights[stack[-1]]:
                a = heights[stack.pop()]
                b = idx - stack[-1] - 1
                area = max(a*b, temp_area)
            stack.append(idx)
        heights.pop()
        return temp_area
        
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        heights = [0] * len(matrix[0])
        area = 0
        for row in matrix:
            for col, item in enumerate(row):
                heights[col] = heights[col] + 1 if item == '1' else 0
            area = max(area, self.tempArea(heights))
        return area
