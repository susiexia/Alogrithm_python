# %%
# make a class of stack:
class stack:
    # construct
    def __init__(self):
        self.stack = []
    
    # method #1
    def pop(self):
        # edge case
        if len(self.stack) < 1:
            return None
        # regular pop
        return self.stack.pop()

    # method 2
    def append(self, val):
        self.stack.append(val)
    
    # method 3 
    def size(self):
        return len(self.stack)



class queue:

    def __init__(self):
        self.queue = []

    # method 1
    def dequeue(self):
        if len(self.queue) <1:
            return None
        return self.queue[0]

    def enqueue(self, val):
        return self.queue.append(val)
    
    def size(self):
        return len(self.queue)


# %%
# palindrome two pionter: only isalphnum() count
# inwards
# nested while use more strictly condition and usually to count pointer
def inwards_palin(str):
    i,j = 0,len(str)-1

    while i<j:
        # nested while: inhert 
        while i<j and not str[i].isalphnum():
            i +=1
        while i<j and not str[j].isalphnum():
            j -=1
        if i<j and str[i].lower() != str[j].lower()
            return False
            break
        i +=1
        j -=1
    return True


# %%
# closet value on array, use bin search 
def closest(lst, target):
    # init a infinite large 
    mini_diff = float('inf')
    low = 0
    high = len(lst) -1
    output = None   # expect a single number, not a list

    # edge case: empty or only 1 element
    if len(lst) == 0:
        return None
    if len(lst) = 1:
        output = lst[0]
    
    while low <=high:
        mid = (high+low)//2

        
        mini_diff = abs(lst[mid] - target)


# %%
# Binary search and tree
# Closest Binary Search Tree Value

# init a class for bt's Treenode, only attach attribute to node
class Treenode:
    def __init__(self, val = 0, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right
# 不用写method, 只是给attribute
# r = Treennode(50)

# -------------------------------------------------------------------

# inorder list, recurive, backtrack order
def inorder_lst(root):
    
    if root is None:
        return []
    else:
        return inorder(root.left) + [root.val] +inorder(root.right)
# dont want a list
def inorder(root):
    if root is None:
        return None
    else:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# search (same as bin search) root is the mid!!!!!!!!!!!!!!!!!!!!
# O(h) TREE HEIGHT
def search(root, target):
    if root is None or root.val == target:
        return root
    else:
        if root.val > target:
            return search(root.left, target)
        else:
            return search(root.left, target)
    
# insert node
def insert(root, new_node):
    if root is None:
        root.val = new_node
    else:
        if root.val > new_node.val:
            if root.left is None:
                root.left = new_node
            else: # call left recursive
                insert(root.left, new_node)
        else:
            if root.right is None:
                root.right = new_node
            else: # call right recursive
                insert(root.right, new_node)

root = Treenode(50)
insert(root,Treenode(30))
insert(root,Treenode(20))
insert(root,Treenode(40))
insert(root,Treenode(70))
insert(root,Treenode(60))
insert(root,Treenode(80))

# inorder_lst(root)
inorder(root)

print(search(root, 30))  # return a treenode object 

# %%
# Lined List
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next