'''
把给定数组内的所有大于0的数放到0右边，
所有小于0的数放到0左边
'''
class Solution(object):
    def sortByZero(self, lst):
        """
        :type lst: list
        :rtype: lst
        """
        
        # 0的位置
        mid = lst.index(0)
        # 把0和第一个数字互换以用来实行一次以0为基准数的快速排序
        lst[0],lst[mid] = lst[mid],lst[0]
        
        left = 1
        right = len(lst)-1

        while True:

            # 如果left数值小于0并且left在right左边
            while lst[left] < lst[0] and left<right:
                left+=1

            # 如果right数值大于0并且left<right
            while lst[right] > lst[0] and left<right:
                right-=1

            # left >= right的适合说明当前没有找到符合交换的位置，退出
            if left>=right:
                break;
            else:#当left和right停下来的时候说明各自找到了可以交换位置的数据
                lst[left],lst[right]=lst[right],lst[left]
                print(lst)

        lst[right-1],lst[0] = lst[0],lst[right-1]           

        return lst
        

solu=Solution()
result=solu.sortByZero([2,7,-4,6,-2,0,-8,3,-1])
print(result)
