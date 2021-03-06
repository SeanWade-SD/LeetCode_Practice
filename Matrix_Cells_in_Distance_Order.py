# We are given a matrix with R rows and C columns has cells with integer coordinates (r, c),
# where 0 <= r < R and 0 <= c < C.
#
# Additionally, we are given a cell in that matrix with coordinates (r0, c0).
#
# Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from
# smallest distance to largest distance. Here, the distance between two cells (r1, c1) and (r2, c2)
# is the Manhattan distance, |r1 - r2| + |c1 - c2|.
# (You may return the answer in any order that satisfies this condition.)
#
# Source：（LeetCode）
# Link：https://leetcode-cn.com/problems/matrix-cells-in-distance-order



class Solution1:
    def allCellsDistOrder(self, R, C, r0, c0):
        matrix = [[] for i in range(R+C)]
        result = []
        for c in range(C):
            for r in range(R):
                dist = abs(r0 - r) + abs(c0 - c)
                matrix[dist].append([r, c])

        for i in matrix:
            if i:
                result.extend(i)
            else:
                pass

        return result


class Solution2:
    def allCellsDistOrder(self, R, C, r0, c0):
        matrix = [(i, j) for i in range(R) for j in range(C)]
        matrix.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0)) #sort(key = lambda function)
        return matrix


class Solution3:
    def allCellsDistOrder(self, R, C, r0, c0):
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        bucket = collections.defaultdict(list)
        dist = lambda r1, c1, r2, c2: abs(r1 - r2) + abs(c1 - c2)

        for i in range(R):
            for j in range(C):
                bucket[dist(i, j, r0, c0)].append([i, j])

        ret = list()
        for i in range(maxDist + 1):
            ret.extend(bucket[i])

        return ret


class Solution3:
    def allCellsDistOrder(self, R, C, r0, c0):
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        row, col = r0, c0
        ret = [[row, col]]
        for dist in range(1, maxDist + 1):
            row -= 1
            for i, (dr, dc) in enumerate(dirs):
                while (i % 2 == 0 and row != r0) or (i % 2 != 0 and col != c0):
                    if 0 <= row < R and 0 <= col < C:
                        ret.append([row, col])
                    row += dr
                    col += dc
        return ret



