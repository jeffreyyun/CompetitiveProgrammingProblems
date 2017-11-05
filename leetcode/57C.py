class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        NEWLINE = "`"
        code = ""

        for line in source:
            code += line + NEWLINE

        start = 0
        output = ""
        in_block = False
        in_comment = False

        #print(code)

        # Rules: Reset start and output when hit a comment or block
        for i in range(len(code)-1):
            if code[i] == NEWLINE:
                if in_comment:
                    start = i
                    in_comment = False

            if code[i:i+2] == "/*" and not in_comment and not in_block and i >= start:
                output += code[start:i]
                in_block = True
                start = i+2

            elif code[i:i+2] == "//" and not in_block and not in_comment and i >= start:
                output += code[start:i]
                start = i+2
                in_comment = True

            elif in_block and not in_comment:
                if i >= start and code[i:i+2] == "*/":
                    in_block = False
                    start = i+2
                else:
                    continue

        if not in_comment:
            output += code[start:]

        output = output.split(NEWLINE)
        output = [o for o in output if len(o) > 0]

        return output
