class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left = 0
        sum_right = sum(nums)
        for i in range(len(nums)):
            if sum_left == sum_right-nums[i]:
                return i
            sum_left += nums[i]
            sum_right -= nums[i]
        return -1
