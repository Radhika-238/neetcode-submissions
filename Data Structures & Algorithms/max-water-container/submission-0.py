class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        max_area = 0
        left = 0
        right = len(heights)-1
        while left < right:
            if heights[left] >= heights[right]:
                height = heights[right]
                width = right - left
                area = height * width
                max_area = max(area, max_area)
                right -= 1
            else:
                height = heights[left]
                width = right - left
                area = height * width
                max_area = max(area, max_area)
                left +=1
        return max_area

            
                