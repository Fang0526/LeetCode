class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)<=0:
            return ""
        i=0
        # 找到长度最小的第一个字符串
        min_len=len(strs[0])
        min_len_p=0
        result=""
        for i in range(len(strs)):
            if min_len>len(strs[i]):
                min_len_p=i
                min_len=len(strs[i])
        
        # 设置哨位
        right = int((min_len-1)/2)
        end=min_len-1
        i=0
        
        while 0 <=right and right<=end:
            temp=strs[min_len_p][0:right+1] # 二分法查找
            flag=True # 标志是否全部匹配
            for j in range(0,len(strs)):
                if strs[j][0:right+1] != temp:
                    end=right-1
                    right=int(right/2)
                    flag = False
                    #print(right,temp,result,end)
                    break;
            if flag:
                right=max(right+int((end-right)/2),right+1)
                result=temp
                #print(right,result,end)
            i+=1
            if i>=10:
                break
            
        return result;
    
solu=Solution()

result=solu.longestCommonPrefix(["flower","flow","flight"])
print(result)
result=solu.longestCommonPrefix(["flower"])
print(result)

result=solu.longestCommonPrefix([])
print(result)

result=solu.longestCommonPrefix(["flower","fiow","flight"])
print(result)

result=solu.longestCommonPrefix(["flower","flow","floweight"])
print(result)
result=solu.longestCommonPrefix(["flower","flow","alight"])
print(result)
result=solu.longestCommonPrefix(["blower","flow","flight"])
print(result)

