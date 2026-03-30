class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr = ''.join(filter(str.isalnum,s)).lower()
        print(newStr)

        beg = 0
        end = len(newStr) - 1
        
        while beg < end:
            if newStr[beg] != newStr[end]:
                return False
            beg += 1
            end -= 1

        return True