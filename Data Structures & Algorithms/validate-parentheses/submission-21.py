class Solution:
    def isValid(self, s: str) -> bool:
        match = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for i in range(0, len(s)):
            if s[i] in match:
                stack.append(s[i])
            else:
                if not stack or s[i] != match[stack.pop()]: return False
        
        # if stack is empty -> true
        return not stack