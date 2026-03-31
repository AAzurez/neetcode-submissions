class Solution:
    def search(self, nums: List[int], target: int) -> int:

        x = 0
        y = len(nums) - 1
        
        while x <= y:
            i = (x + y) // 2
            if nums[i] == target:
                return i
            elif nums[i] < target:# look larger
                x = i + 1
            elif nums[i] > target:#smaller
                y = i - 1
        return -1