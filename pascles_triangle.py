class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            tri = [[1], [1, 1]]
            for i in range(2, numRows):
                t = [1]
                for j in range(1, i):
                    t.append(tri[-1][j-1]+tri[-1][j])
                t.append(1)
                tri.append(t)
        return tri
