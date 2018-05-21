class Solution:
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Inspired by Minimum Number of Arrows to Shoot Balloons
        # We greedily add numbers off the end of the interval
        def verifyTwo(start, end):
            found_one = False
            found_two = False
            for i in picks:
                if i >= start and i <= end:
                    if not found_one:
                        found_one = True
                    else:
                        found_two = True
                        return
            if not found_two:
                if end not in picks:
                    picks.add(end)
                elif end-1 not in picks:
                    picks.add(end-1)


        intervals.sort(key=lambda x: x[1])
        picks = set()
        end = -float('inf')

        for interval in intervals:
            if interval[0] > end:
                picks.add(interval[1])
                end = interval[1]

        for start, end in intervals:
            verifyTwo(start, end)

        return len(picks)



class Solution:
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        picks = []
        # Sort intervals by ending points
        # Greedily select two largest numbers in interval as needed
        intervals = sorted(intervals, key=lambda x: x[1])

        for start, end in intervals:
            if len(picks) == 0:
                picks.append(end)
                picks.append(end-1)
            elif picks[-1] < start:     # No numbers already selected
                picks.append(end)
                picks.append(end-1)
            elif picks[-2] < start:     # One number already selected
                if picks[-1] == end:
                    picks.append(end-1)
                else:
                    picks.append(end)
            else:                       # picks[-2] and picks[-1] already in picks
                continue    

        return len(picks)
