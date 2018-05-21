class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True

    def findDiff(self, word, node, diff=False):
        for _, i in enumerate(word):
            if i not in node.children:
                if diff:
                    return False
                else:
                    # different at this position
                    result = False
                    for k in node.children:
                        result = result or self.findDiff(word[_+1:], node.children[k], diff=True)
                    return result
            else:
                # different at this position
                for k in node.children:
                    if k != i:
                        if self.findDiff(word[_+1:], node.children[k], diff=True):
                            return True
                node = node.children[i]
        return diff

sol = Solution()
board = ["O  ", "   ", "   "]
board = ["XOX", "OXO", "XOX"]
# board = ["XXX", "   ", "OOO"]
# board = ["XOX", "O O", "XOX"]
res = sol.validTicTacToe(board)
print(res)
