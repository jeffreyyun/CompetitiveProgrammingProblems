class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        # last ones and last zeroes
        count_ones = 0
        count_zeroes = 0
        for i in range(len(bits)-1, -1, -1):
            if count_ones == 0 and bits[i] == 0:
                count_zeroes += 1
            elif bits[i] == 1:
                count_ones += 1
            else:
                break
        if count_zeroes >= 2 or count_ones % 2 == 0:
            return True
        else:
            return False
