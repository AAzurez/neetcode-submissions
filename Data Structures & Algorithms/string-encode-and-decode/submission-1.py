class Solution:
    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            amt = len(strs[i])
            string = str(amt) + "x" + strs[i]
            strs[i] = string
        return ''.join(strs)

    def decode(self, s: str) -> List[str]:
        final_list = []
        i = 0

        while i < len(s):
            beg = i

            while s[i] != "x":
                i += 1

            num = int(s[beg:i])
            word = s[i+1:i+num+1]

            final_list.append(word)

            i = i + num + 1

        return final_list