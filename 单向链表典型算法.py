# 实现链表
class Node:
    def __init__(self, value):
        self.__value = value
        # __next is Node type
        self.__next = None
    
    def set_next(self, next_node):
        # next_node is Node type
        self.__next = next_node
    
    def get_next(self):
        return self.__next
    
    def get_value(self):
        return self.__value
    
class ArrayList:
    def __init__(self):
        self.__head = None
        
    def get_head(self):
        return self.__head
    
    def set_head(self, head_node):
        # head_node is Node type
        self.__head = head_node
    
    def __str__(self):
        # 标志当前节点
        current_node = self.__head
        # 输出字符串
        str_print = ''
        
        while current_node != None:
            str_print += (str(current_node.get_value()) + "->")
            current_node = current_node.get_next()
            
        return str_print[:-2]
                  
#创建一个链表
def create_arraylist(*args):
    assert len(args) > 0, "please input at least one data"    
    
    temp_node = Node(None)
    
    my_al = ArrayList()
    
    for value in args:
        # 创建一个新节点
        node = Node(value)
        
        # 如果是头节点则直接给链表的头节点赋值
        if my_al.get_head() == None:
            my_al.set_head(node)        
        else:
            # 一般节点则把当前节点指向上一轮的节点
            temp_node.set_next(node)
        
        # 把这个节点赋值给temp_node作为下一个节点的关联用
        temp_node = node
        
    return my_al

# 从尾到头打印链表
def print_arraylist_reverse(array_list):
    lst_nodes = []
    current_node = array_list.get_head()
    
    while current_node != None:
        lst_nodes.append(current_node.get_value())
        current_node = current_node.get_next()
        
    for node in lst_nodes[::-1]:
        print(node)

# 单链表反转(不借助新链表)
def reverse_LinkedList(al):
    if al.get_head() is None:
        return al
    new_head = Node(None) # 新头结点
    head=al.get_head() # 头节点
    
    while head is not None:
        temp=head.get_next() # 暂时存放当前head结点的下一节点
        head.set_next(new_head.get_next())
        new_head.set_next(head)
        head=temp
    
    al.set_head(new_head.get_next())    
    return al
	
# 单链表反转(创建新链表)
def reverse_arraylist(old_al):
    # 创建新的单向链表
    new_al = ArrayList()
    # 临时借位节点
    temp = Node(None)    
    
    # 判断旧列表是否还有节点
    while old_al.get_head() != None:
        # 把头指针的下一个指针指向temp
        temp = old_al.get_head().get_next()
        # 头指针指向新节点的头指针
        old_al.get_head().set_next(new_al.get_head())
        # 旧头指针变为新头指针
        new_al.set_head(old_al.get_head())
        # 旧头指针右移
        old_al.set_head(temp)
    
    return new_al

# 创建一个有环链表
def createCycle():
    al = ArrayList()
    head = Node(3)
    al.set_head(head)
    node_2=Node(4)
    head.set_next(node_2)
    node_3=Node(5)
    node_2.set_next(node_3)
    node_4=Node(7)
    node_3.set_next(node_4)
    node_5=Node(8)
    node_4.set_next(node_5)
    node_6=Node(9)
    node_5.set_next(node_6)
    node_6.set_next(node_4)    
    return al
    
# 链表中环的检测
def checkCycle(al):
    fast=al.get_head()
    slow=al.get_head()
    while fast is not None:
        fast=fast.get_next().get_next()
        slow=slow.get_next()
        if fast is slow:
            return True
    return False

# 两个有序链表合并(不借助新链表)
def CombineTwoLinkedList(l_1,l_2):
    pre=Node(None)
    cur2=l_2.get_head()
    cur1=l_1.get_head()
    # 暂时把pre当作2的head
    pre.set_next(cur2)
    l_2.set_head(pre)
    # 假定选2作为底，1的内容插入到2中
    while cur1 != None and cur2 != None:
        if cur1.get_value()<cur2.get_value():
            temp = cur1.get_next()
            cur1.set_next(cur2)
            pre.set_next(cur1)
            pre=cur1
            cur1=temp
        else:
            pre=cur2
            cur2=cur2.get_next()
    
    if cur1 != None:
        pre.set_next(cur1)
    l_2.set_head(l_2.get_head().get_next())
        
    return l_2
  
# 合并两个有序链表(借助新链表)
def combine_two_sorted_arraylist(al_1,al_2):  
    # 以链表2为基准链表
    # 链表2的当前节点
    node_2_cur = al_2.get_head()
    # 链表3前一个节点
    node_2_pre = al_2.get_head()
    
    # 如果表头1小于表头2，更换表头，前一个节点指向表头1
    if al_1.get_head().get_value() < node_2_cur.get_value():
        # 获取表头1
        node_1 = al_1.get_head()  
        # 把标志节点（前一个）赋值为表头1
        node_2_pre = node_1
        # 暂时存放表头1的下一个节点（成为新的表头1）
        temp = node_1.get_next()
        # 表头1的下一个节点指向当前表头2
        node_1.set_next(node_2_cur)
        # 表头2指向表头1，此处完成重置表头2
        al_2.set_head(node_1)
        # 指定新的表头2
        al_1.set_head(temp)
    
    while al_1.get_head() != None and node_2_cur != None:
        if al_1.get_head().get_value() < node_2_cur.get_value(): # 如果表头1小于当前表2节点，则实行表头1插入表2当前节点之前的操作
            # 获取表头1
            node_1 = al_1.get_head()  
            # 暂时存放表头1的下一个节点（成为新的表头1）
            temp = node_1.get_next()
            # 表头1的下一个节点指向当前表头2
            node_1.set_next(node_2_cur)
            # 表头2的前一节点指向表头1，此处完成表头1插入表2的过程
            node_2_pre.set_next(node_1)
            # 把标志节点（前一个）赋值为表头1
            node_2_pre = node_1
            # 指定新的表头2
            al_1.set_head(temp)
        else:  # 如果表头1大于当前表2节点，则将标志位 前一节点和当前节点 向后移动一位
            node_2_pre = node_2_cur
            node_2_cur = node_2_cur.get_next()
    
    # 如果表2走完表1还未走完，则把表1剩余部分通过表2最后节点指向表1头指针的方式进行一次性合并
    if al_1.get_head() != None:
        # 当表2走完，node_2_pre标志表2的最后一个节点
        node_2_pre.set_next(al_1.get_head())
    
    return al_2  

# 删除链表倒数第n个结点
def theLastNthNode(ll,n):
    if ll is None or ll.get_head() is None or n<=0:
        return None
    
    fast=ll.get_head()
    slow=ll.get_head()
    pre=None
    cnt = 0
    # 快指针先走n步，当结束时慢指针指向的就是倒数第n个结点
    while fast != None:        
        if cnt < n:
            fast=fast.get_next()
            cnt+=1
        else:
            fast=fast.get_next()
            pre=slow
            slow=slow.get_next()
    
    # 如果退出时pre未动，说明n大于等于整个链表长度
    if pre is None:
        if cnt==n: #n等于链表长度，则删掉表头结点
            ll.set_head(slow.get_next())
            return ll
        else: # 否则返回None
            return None
    
    # 删除倒数第n个结点
    pre.set_next(slow.get_next())    
    return ll
    
# 求链表的中间结点
def getMidNode(ll):
    if ll is None or ll.get_head() is None:
        return None
    
    slow=ll.get_head()
    fast=ll.get_head()
    while fast != None:
        fast=fast.get_next()
        if fast == None:
            return slow.get_value()
        fast=fast.get_next()
        if fast == None:
            return slow.get_next().get_value()
        slow=slow.get_next()
        
    return None