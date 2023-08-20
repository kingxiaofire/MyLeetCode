#长度最小的子数组
#滑动窗口
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        fast, low, cur_sum = 0, 0, 0
        min_len = float('inf')

        while fast < len(nums):
            cur_sum += nums[fast]
           
            while cur_sum >= target:
                min_len = min(min_len, fast - low + 1)
                cur_sum -= nums[low]
                low += 1
            
            fast += 1

        return min_len if min_len != float('inf') else 0