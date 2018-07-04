class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):

        left = 0
        height, width = len(matrix), len(matrix[0])
        right = height * width - 1

        if right == -1:
            return False

        else:
            while left <= right:
                mid = (left + right) // 2
                current = matrix[int(mid/width)][mid % width]
                if current < target:
                    left = mid + 1
                elif current > target:
                    right = mid - 1
                else:
                    return True
            return False


if __name__ == "__main__":
    test = Solution()
    matrix = [[1,2,8,10,16,21,23,30,31,37,39,43,44,46,53,59,66,68,71],[90,113,125,138,157,182,207,229,242,267,289,308,331,346,370,392,415,429,440],[460,478,494,506,527,549,561,586,609,629,649,665,683,704,729,747,763,786,796],[808,830,844,864,889,906,928,947,962,976,998,1016,1037,1058,1080,1093,1111,1136,1157],[1180,1204,1220,1235,1251,1272,1286,1298,1320,1338,1362,1378,1402,1416,1441,1456,1475,1488,1513],[1533,1548,1563,1586,1609,1634,1656,1667,1681,1706,1731,1746,1760,1778,1794,1815,1830,1846,1861]]
    target = 1861
    rslt = test.searchMatrix(matrix, target)
    print(rslt)
