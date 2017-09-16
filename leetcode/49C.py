#!/bin/python3


fin = open('A.in', 'r')
fout = open('A.out', 'w')

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        leng = len(citations)
        if not leng:
            return 0
        
        citations.sort()
        
        i = 0
        while (i < leng and citations[i] < leng - i):
            i += 1
            
        return leng - i
        
                              

sol = Solution()
inp = [0,3,1,5,6]
r = sol.hIndex(inp)

print(r)


fin.close()
fout.close()