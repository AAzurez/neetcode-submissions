class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        thing = dict()
        for i in range(len(numbers)):
            if target - numbers[i] not in thing:
                thing[numbers[i]] = i
            else:
                array = [thing.get(target - (numbers[i])) + 1,i + 1]
                return array