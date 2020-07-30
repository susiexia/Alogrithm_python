# %%
'''
1. return 后门直接写 Boolean的公式，如 a==b 这样function会自动回True or Flase
2. set.add(), set.discard('specified item') similar to set.remove(), 
set.pop() due to no order, set pop remove a random element


'''


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
        if i<j and str[i].lower() != str[j].lower():
            return False
            break
        i +=1
        j -=1
    return True


# %%
# closet value on array, use bin search 
# !!!!!!!!!!!!!ask mini diff, 
# when you have mid number, outward to its neibor and compare min_diff to neibors, 
# not mid because no other compare to

a = [2,5,6,7,8,8,9]   # target 4, ask minimun diff

def closest_bs(lst, target):
    # init a infinite large 
    mini_diff = float('inf')  # init as positive inf 
    low = 0
    high = len(lst) -1
    output = None   # expect a single number, not a list

    # edge case: empty or only 1 element
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        output = lst[0]
    
    while low <=high:
        mid = (high+low)//2

        # compare mid neibors to determine direction
        if mid +1 < len(lst):
            right_diff = abs(lst[mid+1] - target)  # abs only one argument!!!!!
        if mid -1 >0:
            left_diff = abs(lst[mid-1] - target)
        # compare to init and update
        if right_diff < mini_diff:
            mini_diff = right_diff
            output = lst[mid+1]

        if left_diff < mini_diff:
            mini_diff = left_diff 
            output = lst[mid-1]
        
        # regular bin search mid-point move
        if lst[mid] > target:
            high = mid -1
        elif lst[mid] < target:
            low = mid +1
        else:
            output = lst[mid]

    return output

print(closest_bs(a, 5.7))


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

# -----------------root means every node--------------------------------------------------
# use recursive and the end leaf is the base case, reach it then backtrack
# inorder list, recurive, backtrack order
# root/ node is None, means it dont have left and right
def inorder_lst(root):
    if root is None:
        return []
    else:
        return inorder(root.left) + [root.val] +inorder(root.right)

# dont want a list
def inorder(root):
    if root is None:  #Base case
        return None
    else:
        inorder(root.left)
        print(root.val)    # recursive code
        inorder(root.right)

# search (same as bin search) root is the mid!!!!!!!!!!!!!!!!!!!!
# O(h) TREE HEIGHT
def search(root, target):
    if root is None or root.val == target:    #Base case
        return root   # recursive code
    else:
        if root.val > target:
            return search(root.left, target)
        else:
            return search(root.left, target)
    
# insert node
def insert(root, new_node):
    if root is None:   #Base case
        root.val = new_node  # recursive code
    else:
        if root.val > new_node.val:
            if root.left is None:
                root.left = new_node   # recursive code
            else: # call left recursive
                insert(root.left, new_node)
        else:
            if root.right is None:
                root.right = new_node
            else: # call right recursive
                insert(root.right, new_node)

# use L= R= to store the length
def depth(root):
    
    if root is None:   #Base case
        return -1    #not O,not None
        # due to leaf node execution max(-1,-1) +1 = 0 !!!!!
    L = depth(root.left)
    R = depth(root.right)
    #ans = max(ans, L+R+1)
    return max(L,R) +1   # 1 is the root node
                # recursive code

root = Treenode(50)
insert(root,Treenode(30))
insert(root,Treenode(20))
insert(root,Treenode(40))
insert(root,Treenode(70))
insert(root,Treenode(60))
insert(root,Treenode(80))

# inorder_lst(root)
inorder(root)

print(depth(root))  # return a treenode object 


# %%
# bt depth-first search
# LC 543 # bt diameter:  the length of the longest path between any two nodes in a tree

# max(depth of node.left, depth of node.right) + 1.
def diameter_depth(root):
    #num_nodes = 1
    if root is None:
        return -1
    L = depth(root.left)
    R = depth(root.right)
    #num_nodes = max(num_nodes, L+R+1)  
    return max(L,R) +1


# %%
# Lined List
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next




# %%
# digit by digit addtion, column by column
# array + one integer  : Time and Space Complexity: O(max(N, log K))
# !!!!!! the last digit add the whole target, and leave 1 as its digit, 
# repeat process until reaching the first element
'''Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
'''
# divmod(x,y) => Return the tuple (x//y, x%y).
def addtion_array(lst, target):
    
    # add whole numbers of target in the last digit
    lst[-1] = lst[-1]  + target   # due to list is mutable
    print(lst[-1])
    for i in range(len(lst)-1,-1,-1): # from large to small
        
        # this digit number, due to its a muteble list, str cannot change directly
        carry, lst[i] = divmod(lst[i], 10)
        if i > 0: # ensure i-1 not < 0
            lst[i-1] += carry
    print(lst)
    if carry >0:    # the vary first digit, in this case its 1000
        lst = list(map(int, str(carry))) + lst

    return lst

A = [2,1,5]
K = 806
print(addtion_array(A, K))

# %%
# find a metrix overall median, n*m is odd
def median_matrix(mat):
    lst = []
    for r_num in range(len(mat)):
        lst.extend(mat[r_num])
    lst.sort

    return int(lst[len(lst)//2])

a = [1,3,5]
b = [2,6,9]
c = [3,6,9]
mat = [a,b,c]
print(median_matrix(mat))



# %% # single number LC 136
# linear runtime
#Given a non-empty array of integers, 
# every element appears twice except for one. Find that single one.

# dict, O(n) | O(n) for dict
# !!!!!!!!!!!search dict only take O(1) !!!!!!!!!!!!!!!!
def single_num(lst):
    hist ={}
    for x in lst:
        hist[x] = hist.get(x,0)+1
    for k,v in hist.items():
        if v == 1:
            return k 

A = [4,1,2,1,2]
print(single_num(A))

# O(n2) use list
def single_num_nodict(lst):
    temp =[]
    for x in lst:
        if x not in temp:
            temp.append(x)
        else:
            temp.remove(x)
    return temp.pop()
print(single_num_nodict(A))

# %%
# LC 202 how to get the next number, divmod method

def get_next(n):
    total_sum = 0
    while n>0:
        n, digit = divmod(n,10)
        # right now n is continue loop
        total_sum = total_sum + digit **2
    return total_sum


# check if the number total_sum =1, 1 true
def happy_number(num): 

    def get_next(n):
        total_sum = 0
        while n>0:
            n, digit = divmod(n,10)
            # right now n is continue loop
            total_sum = total_sum + digit **2
        return total_sum

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    if n ==1:
        return True

# %%
# LC 219 # find min range of 2 duplicate numbers in array

def range_duplicate(nums, k):
    min_range = len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)-1,-1,-1):
                
            if i<j and nums[i] == nums[j]:
                cur_range = abs(j-i)
                min_range = min(cur_range, min_range)
        
    return min_range 
print(range_duplicate([1,2,3,1,2,3],2))