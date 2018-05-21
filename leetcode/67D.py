class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        def isPair(a, b):
            a, b = min(a, b), max(a, b)
            if a%2 == 0 and a+1 == b:
                return True
            else:
                return False

        # Greedy approach -- pair all unmatched couples
        unmatched = {}
        for i in range(len(row))[::2]:
            a = row[i]
            b = row[i+1]
            if not isPair(a, b):
                # no match, add to set
                unmatched[a] = b
                unmatched[b] = a

        swaps = 0
        # while unmatched in set, increment swapcount
        for i in range(len(row))[::2]:
            other = unmatched.get(row[i], -1)
            if other == -1:
                continue

            # Match a with its partner by swapping with the person next to a
            aind = i
            a = row[i]
            b = a+1 if a%2==0 else a-1
            bind = row.index(b)
            row[i+1], row[bind] = row[bind], row[i+1]
            unmatched[a] = -1
            unmatched[b] = -1

            # See if swap helped the other person
            other_ind = bind-bind%2
            aa, bb = row[other_ind], row[other_ind+1]
            if isPair(aa, bb):
                unmatched[aa] = -1
                unmatched[bb] = -1

            print(a, b, row)
            swaps += 1

        return swaps

        
sol = Solution()
row = [5,6,4,0,2,1,9,3,8,7,11,10]

res = sol.minSwapsCouples(row)
print(res)
