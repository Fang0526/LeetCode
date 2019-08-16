'''
仙字号解法：if len(lst) == len(set(lst))
利用Python自带方法
'''
class Solution(object):
    def ifHasDup(self, lst):
        """
        :type lst: list
        :rtype: True/False
        """
        if len(lst)==0:
            return False
        else:
            temp = lst[0]
            dict_data_index = {}
            
            for i in range(0,len(lst)):
                dict_data_index[lst[i]]=i
                
            for i in range(0,len(lst)):
                if lst[i] in dict_data_index and i != dict_data_index[lst[i]]:
                    return True

            return False

solu=Solution()
result = solu.ifHasDup([])
print(result)
