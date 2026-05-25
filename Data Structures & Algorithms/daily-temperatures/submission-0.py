class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmer = [0]*len(temperatures)
        for index, temp in enumerate(temperatures):
            j = index+1
            while j < len(temperatures):
                if temperatures[j] > temp:
                    warmer[index] = j-index
                    break
                j+=1            
        return warmer

