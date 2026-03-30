class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        thing = set()
        long = 0
        
        for i in range(len(nums)):
            thing.add(nums[i])

        for num in thing:
            if num - 1 not in thing:   # start of sequence
                curr = num
                length = 1

                while curr + 1 in thing:
                    curr += 1
                    length += 1

                if length > long:
                    long = length

        return long