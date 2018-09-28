
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        reslt = []
        insertPos = 0
        for interval in intervals:
            if interval.end < newInterval.start:
                reslt.append(interval)
                insertPos += 1
            elif interval.start > newInterval.end:
                reslt.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
        reslt.insert(insertPos, newInterval)
        return reslt




