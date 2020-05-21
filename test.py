class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) < 2: return len(nums)
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]: # 当出现升序时, 和**有效**的降序数量上加1
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(down, up)

s = Solution()
print(s.wiggleMaxLength([1,1,1,1]))