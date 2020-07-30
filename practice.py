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
# %%
# string permutation （whether two string have same charater）
def is_permutation(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    if len(s1) != len(s2):
        return False
    for cha in s1:
        if cha in s2:
            s2 = s2.replace(c, '',1) # replace count only 1
    return len(s2) == 0


# %% Two SUM in one list
def two_sum(lst, target):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):  # !!!!!i+1
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
# set: unordered collection of unique element
# use two pointer
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
            

def pair_sum_2set(nums, target):
    seen =set()   # count dictionary
    output =set()
    if len(nums) <2:
        return None

    for num in nums:
        out = target - num

        if out not in seen:
            seen.add(num)
        else:
            output.add((min(num, out), max(num, out)))
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    return '\n'.join(map(str,list(output)))
    

print(pair_sum_2set([1,3,2,2], 4))
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
# K’th Smallest/Largest Element in Unsorted Array 

# quicksort: 2 seperate function, and recur
def quick_sort(lst, target):
    '''quick sort use pivot to ramdomly partition array, worst: O(n^2)
    The idea is, not to do complete quicksort, 
    but stop at the point where pivot itself is k’th smallest element. 
    Also, not to recur for both left and right sides of pivot, 
    but recur for one of them according to the position of pivot. '''
    # https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
    # https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array-set-2-expected-linear-time/

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
# nested while other use case: skip the nested while, not like above case to generate nested while
# 2 pointers inward to find is palindrome
def is_palindrome(s):
    i,j =0, len(s)-1

    while i<j:
        # nested while to skip space and continuing change 2 pointer
        # simply ignore non-alphanumeric characters by continuing to traverse further
        while i<j and not s[i].isalnum():
            i +=1
        # independent to above nested while
        while i<j and not s[j].isalnum():
            j -=1
        # isalnum and compare if same 
        if i<j and s[i].lower() != s[j].lower():
            return False
        i +=1
        j -=1
    return True
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
            return False   # want to all True
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

#def common_while(a, b):
    output = []
    i = 0
    j = 0
    
    # 2 iteration in one while!!!!!!!!!!!!!!!!!!!!
    # need to consider if elements doen't same, move index
    # BUT its woring, due to maybe next index has same value
    #while i <len(a) and j<(len(b)):
        #if a[i] == b[j]:
            #output.append(a[i])
        #i +=1
        #j +=1
    #return output   

# %%
# common element in two sorted array
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

a=[1,3,3,5,7,8,9]
b=[1,2,4,5,9,10,11]
#print(common_while(a,b))  # wrong: [1, 4] 
# due to '9' one located on last element, another is located before laste one
print(two_pointer_common(b,a)) # right, [1, 4, 9]
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
# %%
# MINE SWAEEPER 扫雷 ([[0,0],[0,1]], 3row, 4 columns)
# 3 arugments, bombs->list of bomb location, list of list matrix
# return 3*4 array, (-1) =bomb

# bombs =[ [0,1], [1,2] ]
# mark bombs like JSON, slice row_list first then col_list
def mine_sweeper(bombs, row, col):
    # make a metrix with all 0 value
    field = [[0 for c in range(col)]for r in range(row)]

    for bombs_list_loc in bombs:
        # simul arrange 2 variables as tuple from 1 list
        (b_row, b_col) = bombs_list_loc
        # mark bombs in field: JSON!!!!!!!!!!!!!!!
        field[b_row][b_col] = -1
    
    # return field： a all 0 metrix with 1 marked bomb
        # neibor 3*3 sub metrix
        row_neibor_range = range(b_row -1, b_row +2) # may has negative
        col_neibor_range = range(b_col -1, b_col +2) 

        for i in row_neibor_range:
            for j in col_neibor_range:
                # 3 restraint 
                if (0 <= i < row) and (0 <= j < col) and (field[i][j] != -1):
                    # update neibors
                    field[i][j] +=1   # neibor marka number
                    # in one bomb loop, each qualify cell can be mark as 1
                    # BUT for next bomb loop, same cell will incremently mark as 2,3,4
    return field



print(mine_sweeper([[0,0],[1,2]], 3, 4))

# %%
output1 = set()
output2 = set()
resualt = []
for n in range(1,11):
    for m in range(1,6):
        resualt.append((n,m))
        output1.add((n,m))
        output2.add((m,n))
        
print(len(output), len(output2), len(resualt))
print(output1 == output2)

# %%
# MINE SWAEEPER some throught
# two independent loop to make a matrix
def my_minesweeper(bombs, row,col):
    field = []
    output =[]
    
    for c in range(col):
        c =0
        field.append(c)
    for r in range(row):
        output.append(field)
    print(output)

print(my_minesweeper(1, 3,4))

# %%
def matrix_maker(bombs, num_rows, num_cols):
    field = [[0 for c in range(num_cols)] for r in range(num_rows)]
    print(field)
# This is how to make empty 3*4 matrix, column first
print(matrix_maker(None, 3,4))


def tuple_matrix(bombs, num_rows, num_cols):
    field = [[(r,c) for c in range(num_cols)] for r in range(num_rows)]
    print(field)

print(tuple_matrix(None, 3,4))

def list_compre_nested(bombs, num_rows, num_cols):
    field = [(r,c) for c in range(num_cols) for r in range(num_rows)]
    print(field)  # only one large list contains tuple
    # !!!!!!!!!!!!!!
    # tuple_matrix function is two independent loops, run col loop frist, then list them to second loop
    # list_compre_nested is nested loop and first cols is outer loop, run the nested loop first as regular sequence

print(list_compre_test(None, 3,4))

def flatten_matrix(matrix):
    flatten = [x for sublist in matrix for x in sublist]
    flatten.sort()
    # nested loop, write the outer loop first!!!!!!!!!!!
    return flatten

print(flatten_matrix([[1, 4, 7], [2, 3], [6, 6, 10, 9]]))

def flatten_matrix_conditional(matrix):
    output = [v for sublist in matrix for v in sublist if len(v) > 6]
    return sorted(output)

print(flatten_matrix_conditional([['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] ))
# %%
# one array, most frequent occurance
a =[ 2, 4, 7, 1,5, 5,5]

# ? O(n^2) or O(2*n)
def array_hist(lst):
    hist = {}
    max_value =0
    for x in a:
        hist[x] = hist.get(x, 0) +1
    for k, value in hist.items():
        max_value = max(max_value, value)
        output = k

    return output
print(array_hist(a))


# only loop once: O(n), no dict loop
def most_frequent_oneLoop(lst):
    hist = {}
    max = 0
    max_item = None

    for x in lst:
        hist[x] = hist.get(x, 0)+1
        # stay in same list loop, and x must IN histogram
        if hist[x] > max:
            max = hist[x]
            max_item = x
    return x

print(most_frequent_oneLoop(a))

# %%
# whether all character in a string are unique?

# 1. use hist -=1 and check if len !=0
def try_is_unique(string):
    string = string.replace(' ','').lower() # clean space
    hist = {}
    for cha in string:
        hist[cha] = hist.get(cha, 0)+1
    for k,v in hist.items():
        if v != 1:
            return False
    return True

a = 'I am bcdef'
print(try_is_unique(a))

# ！！！！！！！！！！与 two sum 似！！！！！！！
# use set unique to find duplicate cha
def set_unique(string):
    string = string.replace(' ','').lower() 
    unique_cha = set()

    # ONLY ONE LOOP FOR STRING
    for cha in string:
        if cha in unique_cha:
            return False
        else:
            unique_cha.add(cha)
    return True

a = 'I am bcdef'
print(set_unique(a))


# 3. use set to string, compare to 
# set is unordered collection of unique element
def set_string_unique(string):
    string = string.replace(' ','').lower() 
    # string dont need to be a list
    if len(set(string)) != len(string):
        return False
    return True
a = 'I am bcdef'
print(set_string_unique(a))

# %%
# FIRST NON REPEAT element in string;
# a string, return character that never repeat, if multiple uniques 
# return only first unique

# use dictionary, 2 independent str loop 
# O(2n)
def non_repeating(s):
    s = s.replace(' ','').lower()
    hist ={}
    for cha in s:
        hist[cha] = hist.get(cha, 0)+1
    
    for x in s:
        if hist[x] == 1:
            return x
    return None


# O(2n)
# use dictionary, loop dict 
def dict_repeating(s):
    s = s.replace(' ','').lower()
    hist ={}
    for cha in s:
        hist[cha] = hist.get(cha, 0)+1
    for k, v in hist.items():
        if v == 1:
            return k
    return None

a = 'I am Susie XIA, HOW R U'
print(non_repeating(a))
print(dict_repeating(a))
# %%
# SROTED DICT WITH UNIQUE
# sorted dictrionary.items() and key pick up hist

def sorted_unique(s):
    s = s.replace(' ','').lower()
    s = filter(lambda cha:cha.isalpha(), s)
    hist ={}
    for cha in s:
        hist[cha] = hist.get(cha, 0)+1
    all_quniue_lst = []
    # use key and lambda: due to items() return a tuple(original is (cha, hist)), 
    # lambda choose second item in each tuple to rank
    rank = sorted(hist.items(), key=lambda t: t[1], reverse = False)

    for  t in rank:
        if t[1] == rank[0][1]:   # hist is 1
            all_quniue_lst.append(t)
    return all_quniue_lst

def michigan_sorted_unique(s):
    s = s.replace(' ','').lower()
    s = filter(lambda cha:cha.isalpha(), s)
    hist ={}
    for cha in s:
        hist[cha] = hist.get(cha, 0)+1
    output =[(a,b) for b,a in sorted([(v,k) for k,v in hist.items()], reverse=True)]
    return [x for x in output if x[1] == 1]

a = 'I am Susie XIA, HOW R U'
print(sorted_unique(a), '\n')
print(michigan_sorted_unique(a))

# %%
# Binary search_ one array and one target number
def binary_search(lst,target):
    low = 0
    high = len(lst)-1
    

    while low <= high:  # = also is true
        mid = (high + low)//2
        if lst[mid] == target:
            return mid
        if lst[mid] > target:
            high = mid-1
        else:
            low = mid +1
    return None

# no loop use recursive binary search
def recursive_bin_search(lst, target, low, high):
    if low> high:   # !!!!!!!!!!!base case of recursive
        return False
    else:
        mid = (high+low)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            return recursive_bin_search(lst,target,low, mid-1)
        else:
            return recursive_bin_search(lst, target,mid+1, high)

a = [1,2,4,6,7,8,9,15,21,32]

print(binary_search(a,9))
print(recursive_bin_search(a,9,0,len(a)-1))  # argument can be function





# %%
# recursion nuatrual and factorial, and a corresonding while loop
def sum_n(n):
    if n ==1:   # base cse, terminal case
        return 1
    else:
        return n + sum_n(n-1)    # pushing function into call stack and pop as FILO
            # return 1 + recur means a counter!!
print(sum_n(10))

def factorial(n):
    if n<0:
        return -1
    elif n<2:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

# while 
def while_sum(n):
    i = 0
    total = 0
    while i<= n:
        total = total+i   # total + or * the iteration!!!
        i +=1
    return total
print(while_sum(10))

# sum of the number of digit
# 125 -> 8
def sum_digit(n):
    if n//10 == 0:
        return n
    else:
        return n%10 + sum_digit(n//10)


# %%
# basic fibonacci sequence
def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b, a+b
    return a, b

print(fib(10))