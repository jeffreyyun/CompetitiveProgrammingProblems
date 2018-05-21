class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        # From Official Solution
        transition = {}
        for u, v, w in allowed:
            transition.setdefault((u, v), set())
            transition[(u, v)].add(w)

        seen = set()

        """ Tries all possible rows for given level """
        def solve(row):
            # Finished with pyramid
            if len(row) == 1:
                return True
            # Already tried the row
            if row in seen:
                return False

            seen.add(row)
            return any(solve(upper_cand) for upper_cand in build(row, []))


        """ Builds all possible top levels for a given row (construction using DFS)"""
        def build(row, ans, i=0):
            # Finished the row
            if i + 1 == len(row):
                yield "".join(ans)  # Pythonic, add candidate to generator
            else:
                # Could also use defaultdict to elegantly setdefault
                transition.setdefault((row[i], row[i+1]), set())

                for top in transition[row[i], row[i+1]]:
                    ans.append(top)
                    # Continue building from this place
                    for result in build(row, ans, i+1):
                        yield result
                    ans.pop()

        return solve(bottom)



sol = Solution()
bottom = "DACCDGDDCFCGCFAGFADF"
allowed = ["BGF","AGE","AGC","AGA","CCE","CCD","EGA","CCF","CCA","DCD","DCA","FGE","FGA","FGB","BFB","BFG","BFD","ECC","DBA","FAF","DBF","FDA","FDC","FDE","BEA","BEE","AEA","AEC","AED","EEE","DEA","DEC","EEA","CCG","EEC","DEG","CEE","CED","CEC","CEA","GEC","GEA","GEF","GEE","BDE","BDD","GCE","AFC","DDC","DDB","EFB","EFE","DDE","DDD","CBC","CBE","ACB","ACE","BCD","BCE","BCA","BCB","BCC","DGB","ECF","DGF","ECB","ECA","CGD","CGF","FCE","FEF","BBF","BBD","ADG","ADD","ADA","DFD","DFC","CDE","CDF","CDG","EDF","EDG","EDD","FBA","FBG","FBF","GDF","AAE","AAD","AAC","BAG","BAB","BAC","BAA","CAF","CAD","DAD","DAB","DED","EAD","EAG","EAF","FAC","GAD","GAC","GAB","ABA","ABF","EBD","EBF","EBA","EBB","EBC","CFF","CFE","CFC","GFC","GFA","GFG","GFD"]
result = sol.pyramidTransition(bottom, allowed)
print(result)