class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_result={}
        lst_result=[]
        for i in range(0,len(nums)):
            dict_result[nums[i]] = i

        for j in range(0,len(nums)):
            complete = target - nums[j]
            if complete in dict_result and dict_result[complete] != j and [dict_result[complete],j] not in lst_result:
                lst_result.append([j,dict_result[complete]])
                
 
        return lst_result

solu=Solution()
result=solu.twoSum([3,6,4,1,2,5,9,8,7],9)
print(result)
