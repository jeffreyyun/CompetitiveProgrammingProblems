s = "smmaaggemgegmseeemaaemgmaaemaasasesmgmegaeaagmmegssggaammmaagseeamemeaeaaegsmseemmsesagaggeaagmgagma"
s = list(s)

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    start = 0
    end = 0
    N = len(s)
    dp = [[False for i in range(N)] for j in range(N)]
    # Base cases
    for i in range(N):
        dp[i][i] = True
        if i != N-1:
            dp[i][i+1] = s[i] == s[i+1]
            if dp[i][i+1]:
                start = i
                end = i+1
    for k in range(2, N):
        for i in range(N-k):
            j = i+k
            dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
            if dp[i][j]:
                start = i
                end = j
                i = N-k
    return s[start:end+1]

mxs = ""

for i in range(len(s)):
    temp = s[i]
    for j in range(26):
        s[i] = chr(ord('a')+j)
        res = longestPalindrome(''.join(s))
        if len(res) > len(mxs):
            mxs = res
    s[i] = temp

print(mxs)
