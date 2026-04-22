class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs= {")": "(", "]": "[", "}": "{"}
        for b in s:
            if b in pairs.values():
                stack.append(b)
            else:
                if not stack: return False
                p = stack.pop()
                if pairs[b] != p: return False
        
        if stack:
            return False
        else:
            return True