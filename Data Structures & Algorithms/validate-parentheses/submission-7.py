class Solution:
    def isValid(self, s: str) -> bool:
        mappingClose = {')': '(', ']': '[', '}': '{'}
        stack=deque()
        for x in s:
            if x in mappingClose:
                if not stack or stack.pop()!=mappingClose[x]:
                    return False
                
            else:
                stack.append(x)
        return len(stack)==0