class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=['+', '-', '*','/']
        stack=deque()
        for x in tokens:
            if x not in operators:
                stack.append(x)
            else:
                if x=='+':
                    a=int(stack.pop())
                    b=int(stack.pop())
                    stack.append(b+a)
                elif x=='-':
                    a=int(stack.pop())
                    b=int(stack.pop())
                    stack.append(b-a)
                elif x=='*':
                    a=int(stack.pop())
                    b=int(stack.pop())
                    stack.append(b*a)
                elif x=='/':
                    a=int(stack.pop())
                    b=int(stack.pop())
                    stack.append(int(b/a))
        return int(stack[0])