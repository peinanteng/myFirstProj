class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            s = nums[i] + nums[l] + nums[r]
            while l + 1 < r:
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l + 1 < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l + 1 < r and nums[r] == nums[r + 1]:
                        r -= 1
            if l < r and nums[l]!= nums[l - 1] and nums[r] != nums[r + 1]:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
        return res

ans = Solution().threeSum([1, 1, 1, 0], 100)
pass