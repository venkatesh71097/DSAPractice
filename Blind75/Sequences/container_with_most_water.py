class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1
        # Min of the 2 heights will be the upper bound of the 2 heights, so that a rectangle can be formed. x axis is plain r - l so that's ok! 
        # You need to maximize the area, so you need to move the pointer if that specific pointer's height is the least of the 2 heights (l and r heights) compared! 
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(area, max_area)
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1
        return max_area
