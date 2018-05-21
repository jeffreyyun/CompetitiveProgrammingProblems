import queue

class Solution:
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        # Heap approach: O(N log N) time, O(count) space
        # Iterative, extra-list approach: O(N * count) time, O(count) space
        pq = queue.PriorityQueue()
        courses.sort(key= lambda k: k[1])

        # Greedily add the courses which end first
        # Pop the longest course if we go overtime
        count = 0
        time_spent = 0
        for time, end in courses:
            count += 1
            time_spent += time
            pq.put(-time)
            # Effect of this:
            # If take current course and time exceeded, 
            # we must replace the longest length taken course with the current course
            # If the current course has the longest length, then we can't fit it in greedily, 
            # and we end up popping that from our priority queue
            if time_spent > end:
                time_spent += pq.get()
                count -= 1

        return count





sol = Solution()
courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
result = sol.scheduleCourse(courses)
print(result)