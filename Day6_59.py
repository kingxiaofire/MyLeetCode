#59. 螺旋矩阵 II

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0 # 起始点
        loop, mid = n // 2, n //2 # 迭代次数、n为奇数时，矩阵的中心点
        count = 1 # 计数

        for offset in range(1, loop+1):
            for i in range(starty, n - offset):# 从左至右，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset):
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1):
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1): # -1是指递减
                nums[i][starty] = count
                count += 1
            startx += 1
            starty += 1
        
        if n % 2 != 0:
            nums[mid][mid] = count
        return nums

