# %%
# anagrams: two strings have same character but diff order, rearrange

# brute force (hashtable: O(n) due to histogram. 
# space: O(1): Although we do use extra space, the space complexity is O(1) 
# because the table's size stays constant(only 26) no matter how large n is.)
def anagrams(str1, str2):
    # clean
    str1_filtered = filter(lambda c: c.isalnum(), str1)
    str2_filtered = filter(lambda c: c.isalnum(), str2)

    str1 = str1_filtered.replace(' ', '').lower()
    str2 = str2_filtered.replace(' ', '').lower()

    # create a histogram
    hist = {}
    temp =[]
    for cha in str1:
        hist[cha] = hist.get(cha, 0)+1
    for c in str2:
        if c in hist and hist[c]>0:
            hist[c] -=1
            temp.append(c)
            # return hist.keys
    if len(str1) != len(temp):
        return False
    elif len(str1) != len(str2):
        return False
    else:
        return True

# 三个循环。 用一个DICT 在第二个str中减去, 最后循环dict看是不是全是O
def anagrams(str1, str2):
    # clean
    if len(str1) != len(str2):
        return False
    # create a histogram
    count = {}
    for cha in str1:
        if cha in count:
            count[cha] +=1
        else:
            count[cha] = 1
    for cha in str2:
        if cha in count:
            count[cha] -=1
        else:
            count[cha] = 1
    # loop the count dictionary 
    for k in count:
        if count !=0:
            return False

    return True


# easy way:O(n logn) due to sort, and space: O(1)
def anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        if sorted(str1) == sorted(str2):
            return True

# %% Two SUM in one list
def two_sum(lst, target):
    for i in range(len(lst)-1):
        for j in range(i, len(lst)):
            lst[i]+lst[j] == int(target)
            return (i, j)

# enumerate() and dictionary:
def two_sum(lst, target):
    dic = dict()
    for index, value in enumerate(lst):
        n = target - value
        if n not in dic:
            dic[value] = index            
        else:
            return (dic[n], index)

# %%
# array pair (sum [1,3,2,2], 4) --- 2 pairs (1,3) (2,2)

def pair_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)-1,-1,-1):
            if nums[i] + nums[j] == target:
                return  (nums[i], nums[j])
    

pair_sum([1,3,2,2], 4)
            

# %%
