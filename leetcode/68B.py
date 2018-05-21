import queue

class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        q = queue.PriorityQueue()
        count = {}
        for i in set(S):
            q.put((-S.count(i), i))

        s = ""
        # Greedily add keys
        while not q.empty():
            freq, c = q.get()
            if len(s) != 0 and c == s[-1]:
                putback = (freq, c)
                if not q.empty():
                    freq, c = q.get()
                if c == putback[1]:
                    return ""       # too many of this char
                q.put(putback)
            # add the char to s, update freq of the char
            s += c
            freq += 1
            putback = (freq, c)
            if freq < 0:
                q.put(putback)

        return s

sol = Solution()
S = "abacadaeafaga"

res = sol.reorganizeString(S)
print(res)
