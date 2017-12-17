class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        def createCount(str):
            freq = [0 for i in range(26)]
            for c in str:
                c = c.upper()
                if c >= 'A' and c <= 'Z':
                    freq[ord(c)-ord('A')] += 1
            return freq

        def compareFreq(lpFreq, wordFreq):
            for i in range(26):
                if lpFreq[i] > wordFreq[i]:
                    return False
            return True


        # char count for licensePlate
        lpFreq = createCount(licensePlate)

        min_len = 1000
        min_word = None

        # check char count for each word
        for w in words:
            wordFreq = createCount(w)
            if compareFreq(lpFreq, wordFreq):
                if len(w) < min_len:
                    min_len = len(w)
                    min_word = w

        return min_word