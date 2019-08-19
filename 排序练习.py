class Solution():
    '''
    冒泡排序
    '''
    def maopao(self,lst):
        for i in range(1,len(lst)): # 标志这是第几轮 共进行n-1轮
            for j in range(0,len(lst)-i):
                if lst[j] > lst[j+1]:
                    lst[j],lst[j+1] = lst[j+1],lst[j]
        return lst

    '''
    选择排序
    '''
    def xuanze(self,lst):
        for i in range(0,len(lst)-1): # 每轮初始位置
            min_i=i
            for j in range(i+1,len(lst)):
                if lst[min_i]>lst[j]:
                    min_i=j
            lst[i],lst[min_i]=lst[min_i],lst[i]
        return lst

    '''
    插入排序
    '''
    def charu(self,lst):
        for i in range(1,len(lst)): # 默认第一个元素本身为有序，从第二个开始插入
            j=i
            while j>0 and lst[j]<lst[j-1]: # 从有序数组的最后一位开始比较
                lst[j],lst[j-1]=lst[j-1],lst[j] # 若带插入元素小于当前的有序数组元素则两者交换位置
                j-=1 # 位置向前
        return lst
        
    '''
    快速排序
    '''
    def QuickSort(self,lst):
        self.enQuickSort(lst,0,len(lst)-1)

    def enQuickSort(self,lst,left,right):
        if left>= right:
            return;
        else:
            position = self.PartitionHandle(lst,left,right) # 返回该轮确定位置的元素，该元素左边比它小右边比它大
            self.enQuickSort(lst,left,position-1)
            self.enQuickSort(lst,position+1,right)    

    def PartitionHandle(self,lst,left,right):
        tar = lst[left]
        i=left
        while True:
            while left<right and lst[right]>tar:
                right-=1
            while left<right and lst[left]<=tar:
                left+=1
            if left>=right:
                lst[i],lst[right]=lst[right],lst[i]
                break;
            else:
                lst[left],lst[right]=lst[right],lst[left]
        return right
                

solu=Solution()

lst=[5]
solu.QuickSort(lst)
print(lst)
lst=[5,23]
solu.QuickSort(lst)
print(lst)
lst=[23,14]
solu.QuickSort(lst)
print(lst)

lst=[5,23,14,2,3,6,1,7,4]
solu.QuickSort(lst)
print(lst)

lst=[5,23,14,2,3,6,1,7,34]
solu.QuickSort(lst)
print(lst)
lst=[23,14,2,3,6,1,7,4]
solu.QuickSort(lst)
print(lst)

'''result=solu.maopao([2,3,6,1,7,4])
print(result)
result=solu.maopao([2])
print(result)
result=solu.maopao([2,4])
print(result)
result=solu.maopao([6,1])
print(result)
result=solu.xuanze([2,3,6,1,7,4])
print(result)
result=solu.xuanze([2])
print(result)
result=solu.xuanze([2,4])
print(result)
result=solu.xuanze([6,1])
print(result)
result=solu.charu([11,2,3,6,1,7,4])
print(result)
result=solu.charu([2])
print(result)
result=solu.charu([2,4])
print(result)
result=solu.charu([6,1])
print(result)
'''
