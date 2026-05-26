class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse=True)
        position, speed = zip(*cars)

        timeStack = []

        for index in range(len(position)):
            time = (target-position[index])/speed[index]

            if not timeStack or time > timeStack[-1]:
                timeStack.append(time)
        
        return len(timeStack)