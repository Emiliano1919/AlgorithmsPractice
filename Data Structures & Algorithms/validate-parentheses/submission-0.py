class Solution:
    def isValid(self, s: str) -> bool:
        stack=list(s)
        closed=[]
        mapping = {'(': ')', '[': ']', '{': '}'}
        while len(stack) > 0:
            i=stack.pop()
            if i==']' or i==')' or i=='}':
                closed.append(i)
            else:
                if len(closed)>0 and closed[-1]==mapping[i]:
                    closed.pop() # We found the pair (we already poped stack so pop closed)
                else:
                    # If you dont find the pair at any point it is False
                    return False
        if len(closed)>0 or len(stack)>0:
            return False
        else:
            return True