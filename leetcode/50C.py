


class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        temp = []
        curr_left, last_left, curr_ast, last_ast = 0,0,0,0
        for i in range(len(s)):
        	if s[i] == '(':
        		st.append('(')
        		curr_left += 1
        	elif s[i] == '*':
        		temp.append('*')
        		curr_ast += 1
        	else:
        		last_ast, last_left = curr_ast, curr_left
        		curr_ast, curr_left = 0, 0
        		while len(st) and st[-1] == '*':
        			temp.append(st.pop())
        		if len(st):
        			st.pop()	# remove '('
        		elif len(temp):
        			temp.pop()	# use '*'
        		else:
        			return False
        print(st, temp)


        # after processing
        if len(st) > len(temp):
        	return False

        st, temp = [], []
        for i in range(len(s)):
        	if s[i] == '(':
        		st.append('(')
        	else:
        		if len(st):
        			st.pop()	# remove '('
        		else:
        			continue
        print(st)
        if len(st):
        	return False


        return True




sol = Solution()
inp = "(((*)((*)(*"
r = sol.checkValidString(inp)

print(r)