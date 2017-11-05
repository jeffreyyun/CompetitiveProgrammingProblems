class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        ind = 0

        i = 0
        while i < len(chars):
            prev = chars[i]
            count = 0
            while i < len(chars) and chars[i] == prev:
                i += 1
                count += 1
            chars[ind] = prev
            ind += 1

            if count > 1:
                count_str = str(count)
                for c in count_str:
                    chars[ind] = c
                    ind += 1

        return ind
