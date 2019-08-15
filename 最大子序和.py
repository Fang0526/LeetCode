class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        max=nums[0]
        index_lst=[]
        for i in range(0, len(nums)):
            num=nums[i]
            # 如果当前和小于0则放弃从当前值开始累加
            if sum<0:
                sum=num
                index_lst=[]
            else:
                sum+=num
                index_lst.append(i)
                
            # 比较当前累加值与当前最大和的值，取大的赋值给max
            if max<sum:
                max = sum
        print(index_lst)
        return max


        
