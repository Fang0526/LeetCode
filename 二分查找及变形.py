def BinarySearch(lst,tar):
    if len(lst)<=0:
        return -1
    
    left=0
    right=len(lst)-1
    while left<=right:
        mid=int(left+(right-left)/2)
        if lst[mid]==tar:
            return mid
        elif lst[mid]<tar:
            left=mid+1
        else:
            right=mid-1
    return -1

'''
查找第一个值等于给定值的元素
'''
def theFirstEqual(lst,tar):
    if len(lst)<=0:
        return -1
    left=0
    right=len(lst)-1
    while left<=right:
        mid=int(left+(right-left)/2)
        if lst[mid]==tar:
            if mid==left or lst[mid-1]!=tar:
                return mid
            else:
                right=mid-1
        elif lst[mid]>tar:
            right=mid-1
        else:
            left=mid+1
    return -1
        

'''
查找最后一个值等于给定值的元素
'''
def theLastEqual(lst,tar):
    if len(lst)<=0:
        return -1
    left=0
    right=len(lst)-1
    while left<=right:
        mid=int(left+(right-left)/2)
        if lst[mid]==tar:
            if mid==right or lst[mid+1] != tar:
                return mid
            elif lst[mid]>tar:
                right=mid-1
            else:
                left=mid+1
    return -1

'''
查找第一个大于等于给定值的元素
'''
def theFirstLargeThan(lst,tar):
    if len(lst)<=0:
        return -1
    left=0
    right=len(lst)-1
    while left<=right:
        mid=int(left+(right-left)/2)
        if lst[mid]<tar:
            left=mid+1
        elif lst[mid]>=tar:
            if mid==left or lst[mid-1]<tar:
                return mid
            else:
                right=mid=-1
    return -1

'''
查找最后一个小于等于给定值的元素
'''
def theLastLessThan(lst,tar):
    if len(lst)<=0:
        return -1
    left=0
    right=len(lst)-1
    while left<=right:
        mid=int(left+(right-left)/2)
        if lst[mid]>tar:
            right=mid-1
        elif lst[mid]<=tar:
            if mid==right or lst[mid+1]>tar:
                return mid
            else:
                left=mid+1
    return -1



lst=[]
result=theLastLessThan(lst,8)
print(result) # -1

lst=[2]
result=theLastLessThan(lst,-2)
print(result) # -1 
lst=[2]
result=theLastLessThan(lst,2)
print(result) # 0
lst=[2]
result=theLastLessThan(lst,3)
print(result) # 0

lst=[2,5]
result=theLastLessThan(lst,1)
print(result) # -1 
result=theLastLessThan(lst,2)
print(result) # 0
result=theLastLessThan(lst,3)
print(result) # 0
result=theLastLessThan(lst,5)
print(result) # 1
result=theLastLessThan(lst,6)
print(result) # 1

lst=[2,2,5,5]
result=theLastLessThan(lst,1)
print(result) # -1 
result=theLastLessThan(lst,2)
print(result) # 1
result=theLastLessThan(lst,3)
print(result) # 1
result=theLastLessThan(lst,5)
print(result) # 3
result=theLastLessThan(lst,6)
print(result) # 3


lst=[2,4,5,6,8,9,11,14]
result=theLastLessThan(lst,1)
print(result) # -1
result=theLastLessThan(lst,2)
print(result) # 0
result=theLastLessThan(lst,5)
print(result) # 2
result=theLastLessThan(lst,7)
print(result) # 3
result=theLastLessThan(lst,11)
print(result) # 6
result=theLastLessThan(lst,10)
print(result) # 5
result=theLastLessThan(lst,14)
print(result) # 7
result=theLastLessThan(lst,15)
print(result) # 7

lst=[2,2,4,5,6,6,8,9,9,11,14,14]
result=theLastLessThan(lst,2)
print(result) # 1 
result=theLastLessThan(lst,6)
print(result) # 5
result=theLastLessThan(lst,9)
print(result) # 8
result=theLastLessThan(lst,14)
print(result) # 11

'''
lst=[]
result=theFirstEqual(lst,8)
print(result) # -1

lst=[2]
result=theFirstEqual(lst,-2)
print(result) # -1 
lst=[2]
result=theFirstEqual(lst,2)
print(result) # 0
lst=[2]
result=theFirstEqual(lst,3)
print(result) # -1

lst=[2,5]
result=theFirstEqual(lst,1)
print(result) # -1 
result=theFirstEqual(lst,2)
print(result) # 0
result=theFirstEqual(lst,3)
print(result) # -1
result=theFirstEqual(lst,5)
print(result) # 1
result=theFirstEqual(lst,6)
print(result) # -1

lst=[2,2,5,5]
result=theFirstEqual(lst,1)
print(result) # -1 
result=theFirstEqual(lst,2)
print(result) # 0
result=theFirstEqual(lst,3)
print(result) # -1
result=theFirstEqual(lst,5)
print(result) # 2
result=theFirstEqual(lst,6)
print(result) # -1


lst=[2,4,5,6,8,9,11,14]
result=theFirstEqual(lst,-2)
print(result) # -1 
result=theFirstEqual(lst,1)
print(result) # -1
result=theFirstEqual(lst,2)
print(result) # 0
result=theFirstEqual(lst,5)
print(result) # 2
result=theFirstEqual(lst,6)
print(result) # 3
result=theFirstEqual(lst,11)
print(result) # 6
result=theFirstEqual(lst,10)
print(result) # -1
result=theFirstEqual(lst,13)
print(result) # -1
result=theFirstEqual(lst,14)
print(result) # 7
result=theFirstEqual(lst,15)
print(result) # -1
result=theFirstEqual(lst,18)
print(result) # -1

lst=[2,2,4,5,6,6,8,9,9,11,14,14]
result=theFirstEqual(lst,2)
print(result) # 0 
result=theFirstEqual(lst,6)
print(result) # 4
result=theFirstEqual(lst,9)
print(result) # 7
result=theFirstEqual(lst,14)
print(result) # 10


lst=[]
result=BinarySearch(lst,8)
print(result) # -1

lst=[2]
result=BinarySearch(lst,-2)
print(result) # -1 
lst=[2]
result=BinarySearch(lst,2)
print(result) # 0
lst=[2]
result=BinarySearch(lst,3)
print(result) # -1

lst=[2,5]
result=BinarySearch(lst,1)
print(result) # -1 
lst=[2,5]
result=BinarySearch(lst,2)
print(result) # 0
lst=[2,5]
result=BinarySearch(lst,3)
print(result) # -1
lst=[2,5]
result=BinarySearch(lst,5)
print(result) # 1
lst=[2,5]
result=BinarySearch(lst,6)
print(result) # -1

lst=[2,4,5,6,8,9,11,14]
result=BinarySearch(lst,-2)
print(result) # -1 
result=BinarySearch(lst,1)
print(result) # -1
result=BinarySearch(lst,2)
print(result) # 0
result=BinarySearch(lst,5)
print(result) # 2
result=BinarySearch(lst,6)
print(result) # 3
result=BinarySearch(lst,11)
print(result) # 6
result=BinarySearch(lst,10)
print(result) # -1
result=BinarySearch(lst,13)
print(result) # -1
result=BinarySearch(lst,14)
print(result) # 7
result=BinarySearch(lst,15)
print(result) # -1
result=BinarySearch(lst,18)
print(result) # -1
'''
