import sys

def burgerOrientation(K, D):

    D.sort()
   
    layers = len(D)//2+1
    reference = [x for x in range(layers) for i in range(2)]
    # print(reference, D)

    error = 0
    for i in range(len(D)):
        error += (reference[i]-D[i])**2

    return error



sys.stdin = open("A-large-practice.in", "r")
sys.stdout = open("A-large.out", "w")

T = int(input())
for t in range(T):
    K = int(input())
    D = [int(x) for x in input().split()]
    print("Case #{}: {}".format(t+1, burgerOrientation(K, D)))