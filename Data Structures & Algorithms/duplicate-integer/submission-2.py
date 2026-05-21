class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(nums)!=len(set(nums))
        # if len(nums) == 0: return False
        # hashMap = defaultdict(int)
        # for num in nums: 
        #     hashMap[num]+=1
        # return True if max(hashMap.values())>1 else False
        hashSet = set()
        nums.sort()
        for num in nums: 
            if num in hashSet: return True
            hashSet.add(num)
        return False
        