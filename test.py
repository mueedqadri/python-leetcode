class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_string: str = ''  
        n = len(s)
        for i in range(n):
            for j in range(n+1):
                if len(s[i:j])> 1:
                    if self.isPalindrome(s[i:j]):
                        if len(longest_string) < len(s[i:j]):
                            longest_string = s[i:j]
        return longest_string

    def isPalindrome(ss: str)-> bool:
        l: int= len(ss)
        if ss[0] == ss[l-1] and (l == 2 or l == 3):
            return True
        elif ss[0] == ss[l-1] and self.sPalindrome(ss[1:l-1]):