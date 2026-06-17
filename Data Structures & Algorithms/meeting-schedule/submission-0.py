"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start)

        for i in range(1, len(intervals)):
            meeting1 = intervals[i-1]
            meeting2 = intervals[i]

            if meeting1.end > meeting2.start: 
                return False
        return True
