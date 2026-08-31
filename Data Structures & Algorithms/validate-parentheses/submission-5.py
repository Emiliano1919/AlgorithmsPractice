class Solution:
    def isValid(self, s: str) -> bool:
        mappingClose = {')': '(', ']': '[', '}': '{'}
        stack=deque()
        for c in s:
            if c in mappingClose:
                if stack and mappingClose[c]==stack.pop():
                    continue
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True
