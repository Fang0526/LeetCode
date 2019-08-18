class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        mid=-1
        
        while left<right:
            mid=left+(right-left)/2
            print(left,mid,right,nums[mid])
            if nums[mid]<nums[mid+1] and nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[mid]<nums[right]:
                right=mid-1
            else:
                left=mid+1
        
        return nums[left]
        