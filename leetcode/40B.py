class Solution:
    def parse(self, eq, ind):
        # parses until = (LHS) or end (RHS)
        total_x = 0
        total_coeff = 0
        curr_c = 1
        sign = 1
        isCoeff = False

        def update(sign, curr_c, isCoeff, total_x, total_coeff):
            if isCoeff:
                total_coeff += sign*curr_c
            else:
                total_x += sign*curr_c
            return total_x, total_coeff

        i = ind
        while i < len(eq):
            #print(eq[i])
            if eq[i] == '=':
                total_x, total_coeff = update(sign, curr_c, isCoeff, total_x, total_coeff)
                break
            elif eq[i] == '+':
                if i != ind:
                    total_x, total_coeff = update(sign, curr_c, isCoeff, total_x, total_coeff)
                sign = 1
                curr_c = 1
            elif eq[i] == '-':
                if i != ind:
                    total_x, total_coeff = update(sign, curr_c, isCoeff, total_x, total_coeff)
                sign = -1
                curr_c = 1
            elif eq[i].isdigit():
                isCoeff = True
                curr_c = int(eq[i])
                i += 1
                while i < len(eq) and eq[i].isdigit():
                    curr_c *= 10
                    curr_c += int(eq[i])
                    i += 1
                i -= 1
            elif eq[i] == 'x':
                isCoeff = False
            i += 1

        if i >= len(eq):
            #print(sign, curr_c, isCoeff, total_x, total_coeff)
            total_x, total_coeff = update(sign, curr_c, isCoeff, total_x, total_coeff)

        return total_x, total_coeff, i


    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        LHS_x, LHS_c, equal_sign = self.parse(equation, 0)
        RHS_x, RHS_c, _ = self.parse(equation, equal_sign + 1)

        #print(LHS_x, LHS_c, equal_sign, RHS_x, RHS_c)

        LHS_val = LHS_x - RHS_x
        RHS_val = RHS_c - LHS_c

        if LHS_val == 0:
            if RHS_val == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x={}".format(RHS_val//LHS_val)
