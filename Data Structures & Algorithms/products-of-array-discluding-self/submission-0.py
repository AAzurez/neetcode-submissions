class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        result = []

        pre = 1
        for i in range(len(nums)):
            left[i] = pre
            pre *= nums[i]

        suf = 1
        for j in range(len(nums)-1, -1, -1):
            right[j] = suf
            suf *= nums[j]

        for k in range(len(nums)):
            result.append(left[k] * right[k])

        return result