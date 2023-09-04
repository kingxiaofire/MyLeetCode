#三数之和
#双指针法
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                return result
            #第一个数大于0，则三数之和无法等于0

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            #跳过相同元素避免i重复

            left = i + 1
            right = len(nums) - 1

            while right > left:
                sum_ = nums[i] + nums[left] + nums[right]

                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1

                    right -= 1
                    left += 1
        return result  
   