class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        currList = dict()
        for i in range(len(nums)):
            if nums[i] in currList:
                currList[nums[i]] += 1
            else:
                currList[nums[i]] = 1
        result = sorted(currList, key=currList.get, reverse=True)
        return result[:k]