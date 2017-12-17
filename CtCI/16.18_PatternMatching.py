def matchPattern(pattern, value):
    """
    Input:  pattern, a string, 1 < length < 1000000
            value, a string, 1 < length < 1000000
    Assumptions: pattern contains only a and b
    """
    # count occurrences of a and b in the pattern
    # Comments refer "a" to whatever is pattern[0], "b" to the other one
    count_1 = 0
    count_2 = 0
    c1 = pattern[0]
    for i in range(len(pattern)):
        if pattern[i] == c1:
            count_1 += 1
        else:
            count_2 += 1

    # find number of a's initially e.g. "aaabbabb" has init_count_1 = 3
    for i in range(len(pattern)):
        if pattern[i] != c1:
            init_count_1 = i
            break

    N = len(value)
    for len_1 in range(N//count_1 + 1):
        len_2 = (N - len_1 * count_1) / count_2     # find length of b based on length of a
        if len_2 != int(len_2):         # b must be of integral length
            continue
        str_1 = value[: len_1]
        str_2 = value[len_1*init_count_1 : len_1*init_count_1 + len_2]
        if check(str_1, str_2, pattern, value):
            return True

    return False


def check(str_1, str_2, pattern, value):

    len_1, len_2 = len(main), len(alt)
    i = 0
    c1 = pattern[0]
    for c in pattern:
        if c == c1:
            if value[i : i + len_1] != str_1:
                return False
            i += len_1
        else:
            if value[i : i + len_2] != str_2:
                return False
            i += len_2
    return True


pattern = "abab"
value = "aabababababababababababab"

res = matchPattern(pattern, value)
print(res)                          # False