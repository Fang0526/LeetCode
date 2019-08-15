class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst_items = list(s)
        if len(lst_items) <= 0:
            return True
        elif len(lst_items)%2==1:
            return False
        
        # 设置存放已有左括号的列表
        temp = []
        i=0
        # 设置匹配对
        dict_cor={"}":"{",")":"(","]":"["}
        # 遍历所有括号
        while i<len(lst_items):
            # 获取当前括号
            item = lst_items[i]
            # 如果当前是左括号则放入列表中
            if item in ('{','(','['):
                temp.append(item)                
            # 如果当前是右括号并且左括号列表为空则判定为False
            elif item in ("}","]",")"):
                if len(temp) == 0:
                    return False
                # 如果存放的列表不为空
                else:
                    # 如果当前的右括号和左括号列表的最后一个相匹配则从左括号列表中移除匹配的左括号
                    if temp[-1] == dict_cor[item]:
                        temp.pop(-1)
                    # 如果当前右括号和左括号列表的最后一个不匹配则判定为False
                    else:
                        return False
            # 指针后移
            i+=1
        
        # 如果遍历完成左括号列表为空则判定为True
        if len(temp)==0:
            return True
        else:
            return False
        
