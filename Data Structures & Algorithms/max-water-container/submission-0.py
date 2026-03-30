class Solution:
    def maxArea(self, heights: List[int]) -> int:
       #Find the furtherest and biggest 
       #find the current distance and times by lowest bar
       #keep track of area
       
        left = 0
        right = len(heights)-1

        largestArea = (right - left) * min(heights[left], heights[right])

        leftV = heights[left]
        rightV = heights[right]

        while left < right:
            currentArea = (right - left) * min(heights[left], heights[right])
            if largestArea < currentArea:
                largestArea = currentArea
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return largestArea