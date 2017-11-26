class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for event in self.bookings:
            if not (start >= event[1] or end <= event[0]):
                return False
        self.bookings.append((start, end))
        return True
