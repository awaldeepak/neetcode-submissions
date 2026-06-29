"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        can_schedule = True
        # [(0,30), (5,10), (15,20)]
        for i in range(len(sorted_intervals)-1):
            if sorted_intervals[i].end > sorted_intervals[i+1].start:
                return False
            else:
                can_schedule = True
        return can_schedule