class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        currentList = []
        #Need to practice this more
        def dfs(i,currentList,total):
            if total == target: #This makes sense
                res.append(currentList.copy())
                return
            if i>=len(nums) or total > target: #This to stop looking endlessly
                return
            currentList.append(nums[i]) #Explore path
            dfs(i,currentList,total+nums[i]) #Check if the current number works, multiple times
            currentList.pop() #If it doesn't work explore different path
            dfs(i+1,currentList,total) #Exploring different
        dfs(0,[],0)
        return res