# %%
# meeting room (sort , two pointer but related )

def canAttendMeetings(intervals):
    if len(intervals) <2:
        return False
        
    intervals = sorted(intervals, key = lambda x:x[0])
        
        
    i = 0
    j = 1
        
    while i <len(intervals) and j < len(intervals)+1 and j-i == 1:
            
        if intervals[i][0] == intervals[j][0] or intervals[i][1] > intervals[j][0]:
            return i,j
            
        i +=1
        j +=1
            
    return True
print(canAttendMeetings([[6,10],[13,14],[12,14]]))

# meeting arrange
# since j = i+1, so only use i to iterate !!!!!!!!!!
def meeting_interval(lst, k):
    lst = sorted(lst)

    for i in range (len(lst)-1):
        if lst[i+1][0] < lst[i][1]:
            return False
    return True

# %%
# 失败
# 253 meeting room minimum
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) ==0:
            return 0
        total = 1
        
        def not_overlap(a, b):
            if a[0] <= b[0]:
                if b[0] not in range(int(a[0]),int(a[1]+1)) and b[1] not in range(int(a[0]),int(a[1]+1)):
                    return False
                else:
                    return True
            else:
                if a[0] not in range(int(b[0]),int(b[1]+1)) and a[1] not in range(int(b[0]),int(b[1]+1)):
                    return False
                else:
                    return True
                
        intervals = sorted(intervals, key = lambda x:x[0])       
        for i in range(len(intervals)-1):
            for j in range(i+1, len(intervals)):
                if  not_overlap(intervals[i],intervals[j]):
                    total += 1
                
        return total

# %%
def minMeetingRooms(intervals):
    if len(intervals) ==0:
        return 0
    total = 1
        
    def not_overlap(a, b):
        if (b[0] < = a[1] and b[0] >= a[0]) or (b[1] < = a[1] and b[1] >= a[0]):
            return True
        else:
            return False
                
        for i in range(len(intervals)-1):
            for j in range(i+1, len(intervals)):
                if  not_overlap(intervals[i],intervals[j]):
                    total += 1
                if  not_overlap(intervals[j],intervals[i]):
                    total += 1
        return total
# %%
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        使用优先队列算法, 生成优先队列, 代表已开的房间, 先将时间段按照开始时间排序, 遍历时间段, 如果没有多余的房间, 则将这个会议的加到队列里, 如果有多余的房间且目前会议的起始之间在上个会议的终止时间之后, 更新队列.
Time: O(n)
Space: O(1)
        """
        # sort the intervals by start time
        intervals.sort(key = lambda x: x.start)
        heap = []
        for interval in intervals:
            if heap and interval.start >= heap[0]:
                # room is already used in last meeting and continue to use the same room for this meeting
                heapq.heapreplace(heap, interval.end)
                
            else:
                heapq.heappush(heap, interval.end)
                
        return len(heap)

# %%
# alien dict
# time save: order built a dictionary with value is key
# nest loops, one is for the list, pairwise compare, inner loop for !=
# two loops both use iterator 

def alien(words, order):
    order_dict = {}
    for i,v in enumerate(list(order)):
        order_dict[v] = i
        
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
            
            
        for c in range(min(len(word1), len(word2))):
                
            if word1[c] != word2[c]:
                if order_dict[word1[c]] > order_dict[word2[c]]:
                    return False
            else: break
            
        else:    # related to nested loop
            if len(word1) > len(word2):
                return False
    return True

a = ["hello","leetcode"]
b = "hlabcdefgijkmnopqrstuvwxyz"

print(alien(a,b))

# %%
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# %%
def is_prime(n):
    isPrime_bool = [True]* (n+1) # a list of all true, from 0
    #isPrime_bool = [True for x in range(n+1)]
    for i in range(2, int(n**0.5) +1): # all number
        if isPrime_bool[i] is True:
                            # usually start point can be i*i
            for j in range(i*2,n+1, i): # mark the multiple of i
                isPrime_bool[j] = False
    isPrime_bool[0] = False
    isPrime_bool[1] = False
    # return counts
    #return len([x for x in range(2,n+1) if isPrime_bool[x] is True])
    # print out
    count = 0
    for x in range(2,n+1):
        if isPrime_bool[x] is True:
            count +=1
            #yield x
    
    return count
print(is_prime(30))

# %%
def sqrt_prime(n):
    if n < 2:
        return None
    if n ==2 or n== 3:
        return True
    for i in range(2, int(n**0.5)+1):
        for j in range(2, i):
            if i%j == 0:
                print(i,'not prime')
                break
        else:
            print(i, 'is prime')
print(sqrt_prime(30))

# %%
# valid parenthesis
# stack can help us process this recursively 
# i.e. from outside to inwards.

# Time complexity : O(n)O(n) because we simply traverse the given string one character at a time 
# and push and pop operations on a stack take O(1)O(1) time.
#Space complexity : O(n)O(n) as we push all opening brackets onto the stack 
def stack_parent(s):
    b_dict = {')':'(', ']':'[','}':'{'}
    stack =[]

    if len(s) %2 != 0:
        return False
    #if len(s) == 0:
        #return True

    for x in s:
        if x not in b_dict:
            stack.append(x)
        else:
            if len(stack) >0 and stack[-1] == b_dict[x]:
                stack.pop()
            
    if len(stack) >0:
        return False
    return True

# %%
 # matrix, recursive, DFS !!!!!!!!!!!

 def num_islands(grid):
    root_total =0
     # dfs, recursive
    row_range = len(grid)
    col_range = len(grid[0])

    if row_range <1:
        return 0
    def part_island(grid, i, j):
        # base case
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return None
            else:
                grid[i][j] = "-1"   # or -1 or whatever
            # recursive all posssible neibors
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1))

    
    for r in range(row_range):
        for c in range(col_range): # only length range
            if grid[r][c] == '1':
                # add count first!! this is the root
                root_total +=1
                # call function to mark non-root to -1
                part_island(grid,r,c)
    return root_total

# %% 414
# find the 3rd maximun value, if not, return maximun
# use set to remove dupilcate value

# O(n), space O(1)
def max_3_set(lst):
    max_set = set()

    for x in lst:
        if x not in max_set:
            max_set.add(x)
            # after add, immediately check lenth
            if len(max_set) > 3:
                max_set.remove(min(max_set))
    if len(max_set) ==3:
        return min(max_set)
    return max(max_set)


# # O(n), space O(n)In the worst case, the HashSet is the same size as the input Array, and so requires O(n)O(n) space to store.
def regular_max3(lst):
    num_set = set(lst)

    first_max = max(num_set)
    if len(num_set) <3:
        return first_max
    else:
        # remove first and second
        num_set.remove(first_max)
        second = max(num_set)
        num_set.remove(second)

        return max(num_set)
# list also have remove(element), pop(i), del list[1:] del list[0] 
# set dont have del, unless del whole set, and del in list is for position, slice

# %%
# two sorted list, a:m > b:n, merge B into A and sort again
# 88 LC
# quick sort:  o(m+n log m+n) | o(log m+n)
def quick_sort_merge(a,b):
    a[m:] =b
    return sorted(a)

# two pointer from start, WHILE
# O(m+n) | O(m+n)
def two_pointer_merge(a,b,m,n):
    cut_a = a[:m]
    a[:] =[]  #  since ask directly modify on A
    i = 0
    j = 0
    while i < m and j < n:
        if cut_a[i] < b[j]:
            a.append(a[i])
            i +=1
        else:
            a.append(b[j])
            j +=1
    # rest part
    if i <m:
        a[i+j:] = cut_a[i:]
    if j<n:
        a += b[j:]

# O(m+n) | O(1)
# two pointers but backforward
def back_merge(a,b,m,n):
'''redo!!!!!'''    
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1
        
        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] =  nums1[p1]
                p1 -= 1
            p -= 1
        
        # add missing elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]

# %%
# dictionary sort 
def topKFrequent(nums, k):
    hist = {}
    
    for x in nums:
        hist[x] = hist.get(x,0)+1
            
    lst = [key for key, v in sorted(hist.items(), key = lambda x:x[1], reverse =True)]
    
    return lst[:k]

a = [1,1,1,2,2,3]
k = 2
print(topKFrequent(a,k))

# %%
