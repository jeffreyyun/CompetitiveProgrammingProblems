class MyCalendarTwo:

    def __init__(self):
        self.bookings = []


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        conflicts = []
        for event in self.bookings:
            if not (start >= event[1] or end <= event[0]):
                conflicts.append((max(event[0], start), min(event[1], end)))

        for i in range(len(conflicts)):
            for j in range(i+1, len(conflicts)):
                if not (conflicts[i][0] >= conflicts[j][1] or conflicts[i][1] <= conflicts[j][0]):
                    return False
        self.bookings.append((start, end))
        return True
