class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        R = len(image)
        C = len(image[0])

        def add(r, c):
            if r < 0 or r >= R or c < 0 or c >= C:
                return
            elif image[r][c] == oldColor:
                st.append((r, c))
            return

        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        st = []
        st.append((sr, sc))
        while len(st) > 0:
            r, c = st.pop()
            add(r+1, c)
            add(r-1, c)
            add(r, c+1)
            add(r, c-1)
            image[r][c] = newColor

        return image
