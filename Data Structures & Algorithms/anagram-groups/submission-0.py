class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) # we need to return list of lists, so why not maintain values in list
        for word in strs:
            hashMap["".join(sorted(word))].append(word) 
            # sorted(word) will return a list of all letters/chars in the word( sorted alphabetical order)
        return list(hashMap.values())