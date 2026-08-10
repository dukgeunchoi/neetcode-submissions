class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            try:
                n = int(t)
                nums.append(n)
            except:
                n1 = nums.pop()
                n2 = nums.pop()
                res = 0
                if t == "+": res = n1 + n2
                elif t == "-": res = n2 - n1
                elif t == "*": res = n1 * n2
                elif t == "/": res = n2 / n1
                nums.append(int(res))
        
        return nums[-1]