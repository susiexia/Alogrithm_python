# %%
# String question, 2
# LC 937: reorder log files
# First throught: loop list, and check if the second element starts with letter, then 
# append and sort them to a new list, then extend numerica list without sort

# time: sort: at least O(nlogn)
# space: new list: O(n)
# WRONG!!! 
def reorder(logs):
    '''input is list of string'''
    alpha_list = list()
    
    for log in logs:
        
        if log.split()[1].isalpha():
            alpha_list.append(log)
            logs.remove(log)

    alpha_list = sorted(alpha_list, key = lambda x: (x.split()[1]，x.split()[0]))  #!!!!! key can be a tuple, to compare multi order things  
    alpha_list.extend(logs)

    return alpha_list


# USE SORTED CUSTOM KEY to directly motify on original list
#time:O (M * nlogn)
# space: O(M⋅N+M⋅N)=O(M⋅N)
def custom_reorder(logs):

    # seperate fuction for sort keys, use tuple for multi order sort
    def sort_key(x):
        # use split(maxsplit =1) to assign 2 element simulatinously
        log_id, log_rest = x.split(' ', maxsplit=1)
        if log_rest[0].isalpha():
            return (0, log_rest, log_id)
        else:
            return (1, None, None)
    
    return sorted(logs, key = sort_key)

# %%
# LC 53: max subarray
# 3 ways: 1. Greedy, 2 DP 3. Divide and conquer

#1, O(n) | O(1)n constant space, ? since only 2 variables created for space?
def greedy_max_subarray(lst):
    cur_max = gol_max = lst[0]

    for i in range(1, len(lst)):
        cur_max = max(cur_max+lst[i], lst[i])  #### must campare that 2!!!!
        gol_max = max(cur_max, gol_max)
    return gol_max



# DP
# check previous single number is positive or negative, negative-> ignore all previous
def DP_maxSubarray(lst):
    max_sum = lst[0]

    for i in range(1, len(lst)):
        if lst[i-1]>0:      # previous single one is a positive number, update it as sum
            lst[i] += lst[i-1]
        # if previous is negative, use current number to compare
        max_sum = max(max_sum, lst[i])
    return max_sum

# %%
 # LC 239 sliding window maximum
 # brute force O(nk)

 def BF_slide_window(nums, k):
    n = len(nums)
    if n*k == 0:
        return []
    
    return list(max(nums[i:i+k]) for i in range(0, n-k+1))


# DP and deque 
# redo!!!!

# %%
# LC 121 Best Time to buy and sell stock
# first try: wrong!!!!
def stock_profit(prices):
    #buying_price, selling_price = min(prices), max(prices)
    #b_index = prices.index(buying_price)
    #s_index = prices.index(selling_price)
            
    #if b_index < s_index:
        #return selling_price- buying_price
    #else:
        #return 0

# need to finde the max diff for every i and j when i< j, same as two_sum
def stock_2iterators(prices):
    max_profit = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):

            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

    return max_profit

# DP: use if, DP is O(n)

def stock_dp(prices):
    min_price = float('inf')
    max_profit = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
    return max_profit

# DP, without if

def stock_max(prices):
    min_price = float('inf')
    max_profit = 0

    for i in range(len(prices)):
        min_price = min(prices[i], min_price)
        max_profit = max(prices[i]-min_price, max_profit)
    return max_profit
