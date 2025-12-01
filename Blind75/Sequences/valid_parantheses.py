class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "]": "[", "}": "{"}
        stack = []
        for i in s:
            if stack and i in brackets and stack[-1] == brackets[i]:
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0