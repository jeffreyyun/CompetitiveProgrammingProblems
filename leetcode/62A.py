class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for l in letters:
            if l > target:
                return l
        return letters[0]

# simple brute force passes
# binary search would be faster though