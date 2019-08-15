class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)>0:
            pre=nums[0]
            i=1
            while i<len(nums):
                if nums[i] == pre:
                    del nums[i]
                    # nums.pop(i)
                else:
                    pre=nums[i]
                    i+=1
            #print(nums)
        return len(nums)
        
