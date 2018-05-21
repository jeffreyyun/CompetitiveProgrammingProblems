class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if len(S) == 0:
            return 0
            
        first = {}
        last = {}
        for i, c in enumerate(S):
            first.setdefault(c, i)
            last[c] = i

        letters = [(first[x], last[x], x) for x in first.keys()]
        letters.sort(key=lambda x: x[0])

        sizes = []
        start = 0
        end = letters[0][1]
        count = 0
        for s, e, _ in letters:
            if s > end:
                sizes.append(end - start + 1)
                start = s
            end = max(e, end)

        sizes.append(end - start+1)

        return sizes






        
sol = Solution()
letters = ""

res = sol.partitionLabels(letters)
print(res)

