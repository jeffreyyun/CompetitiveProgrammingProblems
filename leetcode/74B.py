import bisect
import collections

class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        # ht --> binary search
        ht = collections.defaultdict(list)
        for i, c in enumerate(S):
            ht[c].append(i)

        def isSubstring(w):
            S_ind = 0
            for c in w:
                if ht[c] == [] or S_ind > ht[c][-1]:
                    return False
                m_ind = bisect.bisect_left(ht[c], S_ind)
                S_ind = ht[c][m_ind]+1
            return True

        count = sum(isSubstring(w) for w in words)
        return count

sol = Solution()
S="abcde"
words=["a","bb","abc","de"]
res = sol.numMatchingSubseq(S, words)
print(res)
