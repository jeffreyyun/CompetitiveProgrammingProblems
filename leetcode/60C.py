class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        pairs = True
        while pairs == True:
            N = len(asteroids)
            pairs = False
            i = 0
            new_ast = []
            while i < N:
                if i<N-1 and asteroids[i] > 0 and asteroids[i+1] < 0:
                    pairs = True
                    if asteroids[i] == -asteroids[i+1]:
                        pass
                    elif asteroids[i] < -asteroids[i+1]:
                        new_ast.append(asteroids[i+1])
                    else:
                        new_ast.append(asteroids[i])
                    i += 2
                else:
                    new_ast.append(asteroids[i])
                    i += 1
            asteroids = [a for a in new_ast]
        return asteroids
