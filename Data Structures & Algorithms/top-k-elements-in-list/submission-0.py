class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap= defaultdict(int)
        for num in nums: 
            hashMap[num]+=1
        
        result = []
        sortedHashMap = dict(sorted(hashMap.items(), key=lambda item:item[1], reverse=True))
        #learn about the dict sorting, helps in all critical solutions.        
        for key,value in sortedHashMap.items():
            if len(result)<k:
                result.append(key)
        return result