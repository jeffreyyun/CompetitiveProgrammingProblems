def gcd(x, y):
   # Euclidian algorithm to find GCD of two numbers

   while y:
       x, y = y, x % y
   return x

def lcm(x, y):
   # Returns LCM of two numbers

   lcm = (x*y)//gcd(x,y)
   return lcm

p, q, s = map(int, input().split())
LCM = lcm(p, q)
ans = "yes" if LCM <= s else "no"
print(ans)
