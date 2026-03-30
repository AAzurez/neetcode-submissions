class Solution:
    def trap(self, height: List[int]) -> int:

        #look for surrounding for smaller and larger numbers
        
        left = 0
        right = len(height)-1
        leftMax = height[left]
        rightMax = height[right]

        currentNumb = 0

        while left < right:

            if height[left] >= height[right]:
                right -= 1
                if height[right] < rightMax:
                    currentNumb += rightMax - height[right]
                else:
                    rightMax = height[right]
            else:
                left += 1
                if height[left] < leftMax:
                    currentNumb += leftMax - height[left]
                else:
                    leftMax = height[left]
        return currentNumb