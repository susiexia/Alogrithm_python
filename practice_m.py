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