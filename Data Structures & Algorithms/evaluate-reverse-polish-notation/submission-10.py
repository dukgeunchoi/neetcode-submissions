class Solution:
    def isInt(self, char: str) -> bool:
        try:
            int(char)
            return True
        except ValueError:
            return False

    
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        res = 0
        for t in tokens:
            if self.isInt(t):
                print(t)
                numStack.append(int(t))
                res = int(t)
            else:
                n2 = numStack.pop()
                n1 = numStack.pop()
                if t == '+': res = n1 + n2
                elif t == '-': res = n1 - n2
                elif t == '*': res = n1 * n2
                else: res = int(n1 / n2)
                numStack.append(res)
            print(numStack)
        return res
