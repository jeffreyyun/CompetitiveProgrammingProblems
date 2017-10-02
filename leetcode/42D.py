class Solution:
    def replaceWords(self, roots, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        """
        # Comment: Forums gave Pythonic trick to not manually continue the trie
        # Simply use
        import collections
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        """

        # adds the root words to a trie
        TERM = 1    # terminate
        trie = {}
        for rt in roots:
            curr = trie
            # for each letter
            for letter in rt:
                if letter not in curr:
                    curr[letter] = {}
                curr = curr[letter]
            curr[TERM] = rt
            # for letter in rt:
            #     if letter not in curr:
            #         curr[letter] = {}
            #     if TERM in curr:    # there is a shorter root so break
            #         break
            #     curr = curr[letter]
            # if TERM not in curr or len(rt) < len(curr[TERM]):
            #     curr[TERM] = rt

        def replace(word):
            curr = trie
            for letter in word:
                if TERM in curr:
                    return curr[TERM]
                elif letter not in curr:
                    break
                else:
                    curr = curr[letter]
            return word

        return ' '.join(map(replace, sentence.split()))