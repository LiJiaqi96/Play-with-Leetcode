class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        number = 4
        def recSum(number,nums,target):
            result = []
            if(number == 1):
                for i in range(1,len(nums)+1):
                    if(nums[len(nums)-i] == target):
                        return [nums[len(nums)-i]]
                        break
                    else:
                        pass
            else:
                result = []
                former = None
                for i in range(len(nums)-number+1):
                    if(nums[i] != former):
                        new_target = target - nums[i]
                        rec = recSum(number-1,nums[i+1:],new_target)
                        if(rec == None or len(rec) == 0):
                            pass
                        elif(len(rec) == 1):
                            if(type(rec[0]) is list):
                                temp = [nums[i]] + rec[0]
                            else:
                                temp = [nums[i]] + rec
                            result.append(sorted(temp))
                        else:
                            for j in range(len(rec)):
                                temp = [nums[i]] + rec[j]
                                result.append(sorted(temp))
                    else:
                        pass
                    former = nums[i]
                return result
        nums = sorted(nums)
        results = recSum(number,nums,target)
        print(results)
    #     indexs = []
    #     for i in range(len(results)-1):
    #         for j in range(i+1,len(results)):
    #             if(results[i] == results[j]):
    #                 indexs.append(j)
    #             else:
    #                 pass
    #     indexs = list(set(indexs))
    #     indexs = sorted(indexs,reverse=True)
    #     print(indexs)
    #     for k in indexs:
    #         del results[k]
        return results
