cost = {}
vowels = ['a', 'e', 'i', 'o', 'u']
curr = 1
for i in range(26):
    letter = chr(ord('a') + i)
    if letter in vowels:
        cost[letter] = 1
    else:
        cost[letter] = curr
        curr += 1
for i in range(26):
    letter = chr(ord('a') + i)
    uletter = chr(ord('A') + i)
    cost[uletter] = cost[letter]*2

with open("tests.txt", "r") as f:
    text = ''.join(f.readlines())
    print(text)
    ans = 0
    for c in text:
        if c.isalpha():
            ans += cost[c]
    print(ans)
