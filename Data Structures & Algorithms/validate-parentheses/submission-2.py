class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '[': ']', '{': '}'}
        stack=deque()
        for x in s:
            if x in mapping:
                stack.append(x)
            else:
                if len(stack)==0 or mapping[stack.pop()]!=x:
                    return False
        if len(stack)!=0:
            return False
        return True
                


