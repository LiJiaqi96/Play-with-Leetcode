class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        else:
            temp_length = [1 for x in range(len(nums))]

            length = 1

            for i in range(1, len(nums)):
                for j in range(0, i):
                    if(nums[j] < nums[i]):
                        temp_length[i] = max(temp_length[j]+1, temp_length[i])
                        length = max(length, temp_length[i])

            return length
