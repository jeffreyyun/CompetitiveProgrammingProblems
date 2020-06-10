#Problem        : Lost in the Logs
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

class Log:
    def __init__(self, t, a, u=None, p=None):
        self.t=t
        self.a=a
        self.u=u
        self.p=p
    
T = int(input())
P = int(input())
probs = {}
logs = {}
points = {}
for _ in range(P):
    s = input().split()
    S, p = int(s[0]), s[1]
    probs[p] = S
N = int(input())
for _ in range(N):
    line = input().split()
    if len(line) == 3:
        t, a, i = line
        logs.setdefault(i, [])
        logs[i].append(Log(t, a))
    else:
        t, a, i, u, p = line
        logs.setdefault(i, [])
        logs[i].append(Log(t, a, u, p))

for i in logs.keys():
    # for each valid submit, if later accepted (with the hash), give them points
    # --> can brute force
    for line in logs[i]:
        if line.a == 'SUBMIT' and line.t <= T:
            line.a = 
        
        
        
        




# somehow award first solvers --> give them .001 points by last problem solved
        

# Sort scores and display
