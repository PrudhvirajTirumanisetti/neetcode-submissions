class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}        
        for index, num in enumerate(numbers):
            diff = target-num
            if diff in hashMap.keys():
                return [hashMap[diff] + 1, index + 1] # the indices are 1-indexed means the index starts at 1 not at 0
            hashMap[num] = index
        return []