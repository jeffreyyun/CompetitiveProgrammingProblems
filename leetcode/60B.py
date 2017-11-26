class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        d = {}
        if len(words1) != len(words2):
            return False
        
        for p1, p2 in pairs:
            if p1 not in d:
                d[p1] = set()
                d[p1].add(p1)
            d[p1].add(p2)

            if p2 not in d:
                d[p2] = set()
                d[p1].add(p2)
            d[p2].add(p1)

        for i, w in enumerate(words1):
            if words2[i] == w:
                continue
            if w not in d or words2[i] not in d[w]:
                return False

        return True
