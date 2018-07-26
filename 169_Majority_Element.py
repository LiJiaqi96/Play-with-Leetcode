class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {}
        for index in nums:
            if(count_dict.has_key(index)):
                count_dict[index] += 1
            else:
                count_dict[index] = 1
        for key in count_dict.keys():
            if(count_dict[key] > len(nums)/2):
                return key
