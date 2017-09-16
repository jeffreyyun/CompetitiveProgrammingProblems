class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        if n == k:
            return "0"
        
        st = []
        for d in num:
            while (k > 0 and st and int(st[-1]) > int(d)):    # remove digits if followed by lesser digits
                st.pop()
                k -= 1
            st.append(d)
            
        while (k > 0):                              # removes last digits if they are largest left
            st.pop()
            k -= 1
            
        while st and st[0] == '0':                  # removes leading 0's
            st.pop(0)                
            
        return ''.join(st) or "0"