class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums) # [1,1,1,1]

        leftMul = 1 # 1 [1, 1, 1, 1]
        for i in range(len(nums)):
            result[i] *= leftMul # 1 [1,1,1,1] -> 1, [1,1,1,1] -> 2 [1,1,2,1] -> 4 [1,1,2,8]
            leftMul *= nums[i]
        # [1,1,2,8]

        rightMul = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= rightMul
            rightMul *= nums[i]
        return result



        