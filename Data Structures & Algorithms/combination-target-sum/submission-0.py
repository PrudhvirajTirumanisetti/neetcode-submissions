class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtracking( i, currSum, total):
            if total == target:
                result.append(currSum[:])
                return 
            if i >=len(nums) or total > target: 
                return 
            
            currSum.append(nums[i])
            backtracking(i, currSum, total+nums[i])
            currSum.pop()
            backtracking(i+1, currSum, total)
        
        backtracking(0,[],0)
        return result