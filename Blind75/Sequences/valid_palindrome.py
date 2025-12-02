class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c.lower() for c in s if c.isalnum()])

        # One shot! 
        return sanitized == sanitized[::-1]

        # Aliter: 2 pointers - not a very big fan of grokking 'patterns' to code curbing my natural instinct
        # start = 0
        # end = len(s) - 1
        # while start <= end:
        #     if s[start] == s[end]:
        #         start += 1
        #         end -= 1
        #         continue
        #     else:
        #         return False
        # return True
