#Problem        : Halloween Candy
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

N,M,MAX,X1,Y1,X2,Y2 = [int(x) for x in input().split()]

g = []
visited = [[False for i in range(M)] for j in range(N)]
for i in range(N):
    g.append([int(i) for i in input().split()])

ans=0

# don't visit the same house twice

def printGrid(g):
    for r in g:
        print(r)

def move(g,x,y,left,c):

    global ans
    # print(x,y,c,left)
    if x < 0 or x >= N or y < 0 or y >= M:  # bounds checker
        return
    if visited[x][y]:
        return
    if x==X2 and y==Y2:
        ans = max(ans,c)
        return
    if abs(X2-x)+abs(Y2-y) > left:
        return

    visited[x][y] = True
    move(g,x+1,y,left-1,c+g[x][y])
    move(g,x,y+1,left-1,c+g[x][y])
    move(g,x,y-1,left-1,c+g[x][y])
    move(g,x-1,y,left-1,c+g[x][y])
    visited[x][y] = False
    return


move(g,X1,Y1,MAX,0)
ans += g[X2][Y2]
print(ans)