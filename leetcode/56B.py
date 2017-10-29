class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 1
        ind = 0
        prev = chars[0]
        for i in range(1, len(chars)):
            if chars[i] == prev:
                count += 1
            elif count < 2:
                count = 1
                chars[ind] = prev
                prev = chars[i]
                ind += 1
            else:
                chars[ind] = prev
                prev = chars[i]
                count_len = len(str(count))
                temp = count_len
                while count_len:
                    count_len -= 1
                    chars[ind+count_len+1] = str(int(count % 10))
                    count /= 10
                ind += 1 + temp
                count = 1
        if count > 1:
            chars[ind] = prev
            count_len = len(str(count))
            temp = count_len
            while count_len >= 1:
                count_len -= 1
                chars[ind+count_len+1] = str(int(count % 10))
                count /= 10
            ind += 1 + temp
        else:
            chars[ind] = prev
            ind += 1    # last one

        #print(chars)
        return ind
