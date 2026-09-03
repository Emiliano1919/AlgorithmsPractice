class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=deque()
        opr=['+', '-', '*', '/']
        for x in tokens:
            if x in opr:
                b=int(stack.pop())
                a=int(stack.pop())
                if x=='+':
                    stack.append(a+b)
                elif x=='-':
                    stack.append(a-b)
                elif x=='*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(x))
        print(stack)
        return stack[0]