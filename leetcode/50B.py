import sys
import operator

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.keys = []
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.d[key] = val
        self.keys.append(key)
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        count = 0
        nd = [val for key,val in self.d.items() if key.startswith(prefix)]
        return sum(nd)


# Your MapSum object will be instantiated and called as such:
result = [""]*10
obj = MapSum()
obj.insert("apple",3)
result[0] = obj.sum("ap")
obj.insert("app", 2)
result[1] = obj.sum("ap")

print(result)
