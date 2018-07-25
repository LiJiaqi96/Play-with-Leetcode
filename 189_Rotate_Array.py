class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp1 = nums[len(nums)-k:]
        temp2 = nums[:len(nums)-k]
        nums[:] = temp1 + temp2
        
