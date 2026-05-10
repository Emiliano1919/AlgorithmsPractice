class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        rt=0 # We count rotations (There are better ways to do it but im practicing queues)
        fullRt=False
        n=len(students)
        while fullRt==False:
            if rt!=n:
                if students[0]==sandwiches[0]: #You are always checking the front
                    students.pop(0)
                    sandwiches.pop(0)
                    n-=1
                    rt=0
                else:
                    back=students.pop(0)
                    students.append(back)
                    rt+=1
            else:
                fullRt=True
        return n