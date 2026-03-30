class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = [0,0]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i] + nums[j] == target and i != j):
                    x[0] = j
                    x[1] = i
        
        return x