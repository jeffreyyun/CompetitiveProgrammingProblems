#!/bin/python3


fin = open('A.in', 'r')
fout = open('A.out', 'w')

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for w in dict:
            try:
                self.d[len(w)].append(w)
            except:
                self.d[len(w)] = [w]


    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        # compare with all letters of same-length words
        # can choose to change one letter from each word -> 26*len(words) combinations
        try:
            for w in self.d[len(word)]:
                letter = 0
                for i in range(len(word)):
                    letter += (word[i] != w[i])
                    if (letter >= 2):
                        break
                if (letter == 1):
                    return True
        except:
            pass
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
        
                              

sol = Solution()
inp = [0,3,1,5,6]
r = sol.hIndex(inp)

print(r)


fin.close()
fout.close()