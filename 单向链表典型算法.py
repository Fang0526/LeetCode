# ʵ������
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
        # ��־��ǰ�ڵ�
        current_node = self.__head
        # ����ַ���
        str_print = ''
        
        while current_node != None:
            str_print += (str(current_node.get_value()) + "->")
            current_node = current_node.get_next()
            
        return str_print[:-2]
                  
#����һ������
def create_arraylist(*args):
    assert len(args) > 0, "please input at least one data"    
    
    temp_node = Node(None)
    
    my_al = ArrayList()
    
    for value in args:
        # ����һ���½ڵ�
        node = Node(value)
        
        # �����ͷ�ڵ���ֱ�Ӹ������ͷ�ڵ㸳ֵ
        if my_al.get_head() == None:
            my_al.set_head(node)        
        else:
            # һ��ڵ���ѵ�ǰ�ڵ�ָ����һ�ֵĽڵ�
            temp_node.set_next(node)
        
        # ������ڵ㸳ֵ��temp_node��Ϊ��һ���ڵ�Ĺ�����
        temp_node = node
        
    return my_al

# ��β��ͷ��ӡ����
def print_arraylist_reverse(array_list):
    lst_nodes = []
    current_node = array_list.get_head()
    
    while current_node != None:
        lst_nodes.append(current_node.get_value())
        current_node = current_node.get_next()
        
    for node in lst_nodes[::-1]:
        print(node)

# ������ת(������������)
def reverse_LinkedList(al):
    if al.get_head() is None:
        return al
    new_head = Node(None) # ��ͷ���
    head=al.get_head() # ͷ�ڵ�
    
    while head is not None:
        temp=head.get_next() # ��ʱ��ŵ�ǰhead������һ�ڵ�
        head.set_next(new_head.get_next())
        new_head.set_next(head)
        head=temp
    
    al.set_head(new_head.get_next())    
    return al
	
# ������ת(����������)
def reverse_arraylist(old_al):
    # �����µĵ�������
    new_al = ArrayList()
    # ��ʱ��λ�ڵ�
    temp = Node(None)    
    
    # �жϾ��б��Ƿ��нڵ�
    while old_al.get_head() != None:
        # ��ͷָ�����һ��ָ��ָ��temp
        temp = old_al.get_head().get_next()
        # ͷָ��ָ���½ڵ��ͷָ��
        old_al.get_head().set_next(new_al.get_head())
        # ��ͷָ���Ϊ��ͷָ��
        new_al.set_head(old_al.get_head())
        # ��ͷָ������
        old_al.set_head(temp)
    
    return new_al

# ����һ���л�����
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
    
# �����л��ļ��
def checkCycle(al):
    fast=al.get_head()
    slow=al.get_head()
    while fast is not None:
        fast=fast.get_next().get_next()
        slow=slow.get_next()
        if fast is slow:
            return True
    return False

# ������������ϲ�(������������)
def CombineTwoLinkedList(l_1,l_2):
    pre=Node(None)
    cur2=l_2.get_head()
    cur1=l_1.get_head()
    # ��ʱ��pre����2��head
    pre.set_next(cur2)
    l_2.set_head(pre)
    # �ٶ�ѡ2��Ϊ�ף�1�����ݲ��뵽2��
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
  
# �ϲ�������������(����������)
def combine_two_sorted_arraylist(al_1,al_2):  
    # ������2Ϊ��׼����
    # ����2�ĵ�ǰ�ڵ�
    node_2_cur = al_2.get_head()
    # ����3ǰһ���ڵ�
    node_2_pre = al_2.get_head()
    
    # �����ͷ1С�ڱ�ͷ2��������ͷ��ǰһ���ڵ�ָ���ͷ1
    if al_1.get_head().get_value() < node_2_cur.get_value():
        # ��ȡ��ͷ1
        node_1 = al_1.get_head()  
        # �ѱ�־�ڵ㣨ǰһ������ֵΪ��ͷ1
        node_2_pre = node_1
        # ��ʱ��ű�ͷ1����һ���ڵ㣨��Ϊ�µı�ͷ1��
        temp = node_1.get_next()
        # ��ͷ1����һ���ڵ�ָ��ǰ��ͷ2
        node_1.set_next(node_2_cur)
        # ��ͷ2ָ���ͷ1���˴�������ñ�ͷ2
        al_2.set_head(node_1)
        # ָ���µı�ͷ2
        al_1.set_head(temp)
    
    while al_1.get_head() != None and node_2_cur != None:
        if al_1.get_head().get_value() < node_2_cur.get_value(): # �����ͷ1С�ڵ�ǰ��2�ڵ㣬��ʵ�б�ͷ1�����2��ǰ�ڵ�֮ǰ�Ĳ���
            # ��ȡ��ͷ1
            node_1 = al_1.get_head()  
            # ��ʱ��ű�ͷ1����һ���ڵ㣨��Ϊ�µı�ͷ1��
            temp = node_1.get_next()
            # ��ͷ1����һ���ڵ�ָ��ǰ��ͷ2
            node_1.set_next(node_2_cur)
            # ��ͷ2��ǰһ�ڵ�ָ���ͷ1���˴���ɱ�ͷ1�����2�Ĺ���
            node_2_pre.set_next(node_1)
            # �ѱ�־�ڵ㣨ǰһ������ֵΪ��ͷ1
            node_2_pre = node_1
            # ָ���µı�ͷ2
            al_1.set_head(temp)
        else:  # �����ͷ1���ڵ�ǰ��2�ڵ㣬�򽫱�־λ ǰһ�ڵ�͵�ǰ�ڵ� ����ƶ�һλ
            node_2_pre = node_2_cur
            node_2_cur = node_2_cur.get_next()
    
    # �����2�����1��δ���꣬��ѱ�1ʣ�ಿ��ͨ����2���ڵ�ָ���1ͷָ��ķ�ʽ����һ���Ժϲ�
    if al_1.get_head() != None:
        # ����2���꣬node_2_pre��־��2�����һ���ڵ�
        node_2_pre.set_next(al_1.get_head())
    
    return al_2  

# ɾ����������n�����
def theLastNthNode(ll,n):
    if ll is None or ll.get_head() is None or n<=0:
        return None
    
    fast=ll.get_head()
    slow=ll.get_head()
    pre=None
    cnt = 0
    # ��ָ������n����������ʱ��ָ��ָ��ľ��ǵ�����n�����
    while fast != None:        
        if cnt < n:
            fast=fast.get_next()
            cnt+=1
        else:
            fast=fast.get_next()
            pre=slow
            slow=slow.get_next()
    
    # ����˳�ʱpreδ����˵��n���ڵ�������������
    if pre is None:
        if cnt==n: #n���������ȣ���ɾ����ͷ���
            ll.set_head(slow.get_next())
            return ll
        else: # ���򷵻�None
            return None
    
    # ɾ��������n�����
    pre.set_next(slow.get_next())    
    return ll
    
# ��������м���
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