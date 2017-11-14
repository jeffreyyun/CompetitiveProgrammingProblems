class Solution:
    
    def UF_init(self, N):
        self.DS = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.groups = N
        
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return
        if self.rank[rootA] > self.rank[rootB]:   # rank
            self.DS[rootA] = rootB
        else:
            self.DS[rootB] = rootA
            if self.rank[rootA] == self.rank[rootB]:
                self.rank[rootB] += 1
        self.groups -= 1
        
    def find(self, a):
        while a != self.DS[a]:
            self.DS[a] = self.DS[self.DS[a]]    # path compression by halving (iterative version)
            a = self.DS[a]
        return a            

    def findCircleNum(self, M):
        N = len(M)
        self.UF_init(N)
        
        for i in range(N):
            for j in range(i+1):
                if M[i][j]:
                    self.union(self.DS[i], self.DS[j])
                    
        return self.groups
