class Solution:
    def isValid(self, s: str) -> bool:
        match = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for b in s:
            if b in match:
                stack.append(b)
            else:
                if not stack or b != match[stack.pop()]:
                    return False
        
        return not stack