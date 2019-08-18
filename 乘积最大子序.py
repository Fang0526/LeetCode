class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_multi=nums[0]
        imax,imin=nums[0],nums[0]
        for num in nums[1:]:
            if num<0:
                imax,imin=imin,imax
            imax=max(imax*num,num) 
            imin=min(imin*num,num)
			#imax,imin=max(imax*num,num,imin*num),min(imin*num,num,imax*num) # ¸üPyronicµÄÐ´·¨
            max_multi=max(max_multi,imax)
        
        return max_multi
            
        