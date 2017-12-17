# After the Contest: Looking at leaderboard
# Of course, we can use hash tables in this case!


class WordFilter:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.ht = {}

        for W, w in enumerate(words):
            pre = ""
            L = len(w)
            for i in range(-1, min(10, L)):
                suf = ""
                if i != -1:
                    pre += w[i]
                for j in range(-1, min(10, L)):
                    if j != -1:
                        suf += w[-(j+1)]
                    self.ht[pre + "$" + suf] = W

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        key = prefix + "$" + suffix[::-1]
        if key not in self.ht:
            return -1
        return self.ht[key]





# Time Limit Exceeded....

class TrieNode:
    def __init__(self):
        self.val = None
        self.children = {}

class Trie:
    def __init__(self, suffixTrie):
        self.root = TrieNode()
        self.suff = suffixTrie

    def insert(self, word, val):
        # insert word (its prefix or suffix) into Trie
        node = self.root
        i_word = word[::-1] if self.suff else word
        for i in i_word[:10]:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.val = val

    def getMatches(self, substr):
        matches = []
        node = self.root
        # Reach starting node
        for i in substr:
            if i not in node.children:
                return []
            node = node.children[i]
        # Get matches starting from children
        matchNodes = []
        matchNodes.append(node)
        while len(matchNodes) > 0:
            node = matchNodes.pop()
            matches += node.vals
            for n in node.children:
                matchNodes.append(node.children[n])
        return sorted(matches)


class WordFilter:

    def __init__(self, words):              #O(N) --- up to 20
        """
        :type words: List[str]
        """
        self.words = words
        self.prefixTrie = Trie(suffixTrie=False)
        self.suffixTrie = Trie(suffixTrie=True)
        for i, w in enumerate(words):
            self.prefixTrie.insert(w, i)
            self.suffixTrie.insert(w, i)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        """
        get weights of all words with this prefix
        get weights of all words with this suffix

        find common element with largest weight (start searching from end)
        """
        preVals = self.prefixTrie.getMatches(prefix)[::-1]
        sufVals = self.suffixTrie.getMatches(suffix[::-1])[::-1]
        # find smallest matching element in both Tries matches lists
        i = 0
        j = 0
        while i < len(preVals) and j < len(sufVals):
            if preVals[i] == sufVals[j]:
                return preVals[i]
            elif preVals[i] < sufVals[j]:
                j += 1
            else:
                i += 1
        return -1
