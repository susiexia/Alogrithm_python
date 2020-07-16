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
def anagrams_3loop(str1, str2):
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
def sorted_anagrams(str1, str2):
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
def two_sum_oneDict_one_Loop(lst, target):
    dic = dict()
    for index, value in enumerate(lst):
        n = target - value
        if n not in dic:
            dic[value] = index            
        else:
            return (dic[n], index)

# %%
# array pair (sum [1,3,2,2], 4) ---> 2 pairs (1,3) (2,2)

def pair_sum(nums, target):
    if len(nums) <2:
        return None
    output = set()
    for i in range(len(nums)):
        for j in range(len(nums)-1,-1,-1):
            if nums[i] + nums[j] == target:
                output.add((min(nums[i], nums[j]), max(nums[i], nums[j])))
    return '\n'.join(map(str,list(output))
    

#print(pair_sum([1,3,2,2], 4))
            

def pair_sum_set(nums, target):
    if len(nums) <2:
        return None
    seen =set()   # count dictionary
    output =set()
    for num in nums:
        out = target - num

        if out not in seen:
            seen.add(num)
        else:
            output.add((min(num, out), max(num, out)))
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    return '\n'.join(map(str,list(output)))
    

print(pair_sum_set([1,3,2,2], 4))
# %%
# largest sum:
# take an array with positive and negative integers and find max sum of array

# set up same init max for index 0, then loop and compare that 2 max

def max_sum(arr):
    a =[]
    if len(arr) == 0:
        return None
    # init two variables at same time
    max_sum = current_sum = arr[0]

    for x in arr[1:]:
        #current_sum = max(current_sum+x, x)
        #current_sum = max(x, current_sum) # find max value
        current_sum = max(current_sum+x, current_sum)
        max_sum = max(current_sum, max_sum)
        a.append(max_sum)
    return '\n'.join(map(str,a))

arr = [7,1,2,-1,3,4,10,-12,3,21,-19]
print(max_sum(arr))

# %%
# reverse a string, sentence
# start = 'this is the best'
# end ='best the is this'

def reverse_sent(str):
    output =[]
    if len(str) == 0:
        return None
    words = str.split(' ')
    for word in words:
        output.append(word)
    output.reverse()
    return ' '.join(output)

print(reverse_sent('this is the best'))

# one line code method
def one_str_reverse(str):
    return ' '.join(reversed(str.split()))
    # return ' '.join(reversed(str.split()[::-1]))

print(one_str_reverse('this is the best'))

#!!!!!!!!!!!!!!!!!!!!!!
#  two nested while index way, due to one loop for sentence, one for each word
def use_index_reverse(string):
    white_space = [' ']  # use list due to NOT IN, 
    i = 0
    outputs =[]

    while i < len(string):
        if string[i] not in white_space:
            # is a word starting
            word_start_pos = i

            #!!!!!
            # nested loop for every word between space:
            while i < len(string) and string[i] not in white_space:
                i +=1
            # slice out the word, end the nested while
            outputs.append(string[word_start_pos:i])
        
        # space count
        i+=1
    return ' '.join(reversed(outputs))

print(use_index_reverse('this is the best'))
# %%
# array rotation
# 2 arrays without duplicate, determine is one a rotaion of another
# same size and elements but start index is different

# method 1: loop second array to find the start index, break it when find it.
# then loop first array use % to make a new index to array2

# print(0%5) => 0 (4%7) =>4

def mod_rotation(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    l2_start_pos = 0

    for i in range(len(lst2)):
        if lst2[i] == lst1[0]:
            l2_start_pos = i
            break
    if l2_start_pos == 0:
        return False
    
    # !!!!!!!!!!!!!!!!!!!!!!!!
    for x in range(len(lst1)):
        l2_new_i = (x+l2_start_pos) % len(lst1)

        if lst1[x] != lst2[l2_new_i]:
            return False
    return True


a=[4,5,6,7,1,2,3]
b=[1,2,3,4,5,6,7]
print(mod_rotation(b,a))


# %%
# two array histrogram
# use enumerate and hist
def enu_hist_rotation(a, b):
    
    hist = {item :i for i, item in enumerate(a)}
    for key in hist:
        if key not in b:
            return False
        else:
            b_index = hist[key]
        if 


# not good
def enu_rotation(a, b):
    value =0
    for i, e in enumerate(a):
        if e in b:
            value = b.index(e)
            print(value) 
        else:
            return False
    return value
    
print(enu_rotation(['a','b','c','d'],['b','c','d','a']))

# %%
# common element in two sorted array
# use while, and set up two iteration for 2 array! no need nested!!!!
# because this is a sorted array, same opstion should have same element if common

def common_while(a, b):
    output = []
    i = 0
    j = 0
    
    # 2 iteration in one while!!!!!!!!!!!!!!!!!!!!
    # need to consider if elements doen't same, move index
    while i <len(a) and j<(len(b)):
        if a[i] == b[j]:
            output.append(a[i])
        i +=1
        j +=1
    return output   

# !!!!!!!!!!!!!!!!two pointer ofr two array!!!!!!!!!!
def two_pointer_common(a, b):
    output = []
    i = 0
    j = 0

    while i <len(a) and j<(len(b)):
        # option 1
        if a[i] == b[j]:
            output.append(a[i])
            i +=1
            j +=1
        elif a[i] > b[j]:
            j +=1
        else:
            i +=1
    return output  

print(common_while(a,b))  # wrong: [1, 4]
print(two_pointer_common(a,b)) # right, [1, 4, 9]
# %%
# O(n^2)
def find_common_element(a, b):
    output =[]
    if a == b:
        return a
    for x in a:
        for y in b:
            if x==y:
                output.append(x)
    return output

# O(n), space O(n)
def find_hist(a,b):
    result = []
    dit = {item :i for i, item in enumerate(a)}
    for key in dit:
        if key in b:
            result.append(key)
    return result

a=[1,3,4,6,7,9]
b=[1,2,4,5,9,10]
print(find_common_element(a,b))
print(find_hist(a,b))