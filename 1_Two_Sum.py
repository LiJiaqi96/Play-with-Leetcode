class Solution(object):
    def twoSum(self, nums, target):
        flag = 0
        for i in range(len(nums)):
            num2 = target - nums[i]
            for j in range(1,len(nums)-i):
                if(nums[len(nums)-j] == num2):
                    return [i,len(nums)-j]
                    flag = 1
                    break
            if(flag):
                break    
