#双指针法
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        left, right, index = 0, len(nums) - 1, len(nums) - 1
        res = [float('inf')] * len(nums)

        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                res[index] = nums[right] ** 2
                right -= 1
            else:
                res[index] = nums[left] ** 2
                left += 1
            index -= 1
        return res