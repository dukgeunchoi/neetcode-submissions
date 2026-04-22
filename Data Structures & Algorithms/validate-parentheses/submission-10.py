class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for b in s:
            if b == "(" or b == "[" or b == "{":
                stack.append(b)
            else:
                if not stack: return False
                p = stack.pop()
                if b == ")" and p != "(": return False
                if b == "]" and p != "[": return False
                if b == "}" and p != "{": return False
        
        if stack:
            return False
        else:
            return True