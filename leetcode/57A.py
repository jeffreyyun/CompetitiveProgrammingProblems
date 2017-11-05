class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        def checkWord(w):
            for i in range(1,len(w)):
                if w[:i] not in wdict:
                    return False
            return True

        wdict = {}
        for w in words:
            wdict[w] = True

        lword = ""
        lwordlen = 0

        for w in words:
            if len(w) >= lwordlen:
                if checkWord(w):
                    if len(w) > lwordlen:
                        lword = w
                        lwordlen = len(w)
                    else:
                        lword = min(w, lword)

        return lword
