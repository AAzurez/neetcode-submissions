class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        array = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                old = stack.pop()
                array[old] = i - old
            stack.append(i)

        return array