#!/usr/bin/env python
# coding: utf-8

# In[1]:


cards=[13,11,7,3,23,9,0]
query=7
output=2


# In[8]:


def locate_card(cards,query):
    pass


# In[9]:


result=locate_card(cards,query)
print(result)


# In[10]:


result==output


# In[11]:


test={'input':{
    'cards':[13,11,10,7,4,3,1,0],
    'query':7
},
     'output':3
     }


# In[12]:


locate_card(**test['input'])==test['output']


# ## test cases
# - the number query occurs somewhere in the middle
# - query is the first element in the cards
# - the query is the last element in the cards
# - the query is not present in the card
# - the cards is empty
# - the cards contains repeating numbers
# - the number query occurs in more than one posistion
# - the list cards contains only one number which is the query

# In[13]:


# query occurs in the middle
tests=[]
tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})


# In[14]:


# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})


# In[15]:


# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})


# In[16]:


# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})


# In[17]:


# cards does not contain query 
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})


# In[18]:


# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})


# In[19]:


# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})


# In[20]:


# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})


# In[22]:


len(tests)


# In[33]:


def locate_card(cards,query):
    low=0
    high=len(cards)-1
    while low<=high:
        mid=(low+high)//2
        mid_number=cards[mid]
        if mid_number==query:
            return mid
        elif mid_number<query:
            high=mid-1
        elif mid_number>query:
            low=mid+1
    return -1


# In[24]:


result=locate_card(test['input']['cards'],test['input']['query'])
result


# In[25]:


get_ipython().system('pip install jovian --upgrade --quiet')


# In[30]:


from jovian.pythondsa import evaluate_test_cases


# In[31]:


from jovian.pythondsa import evaluate_test_case


# In[34]:


evaluate_test_cases(locate_card,tests)


# In[37]:


def test_location(cards,query,mid):
    mid_num=cards[mid]
    if mid_num==query:
        if mid-1>=0 and cards[mid-1]==query:
            return 'left'
        else:
            return 'found'
    elif mid_num<query:
        return 'left'
    else:
        return 'right'


def locate_card(cards,query):
    low=0
    high=len(cards)-1
    while low<=high:
        mid=(low+high)//2
        result=test_location(cards,query,mid)
        if result=='found':
            return mid
        elif result=='left':
            high=mid-1
        elif result=='right':
            low=mid+1
    return -1


# In[38]:


evaluate_test_cases(locate_card,tests)


# ### 9. Analyze the algorithm's complexity and identify inefficiencies, if any.
# 
# Once again, let's try to count the number of iterations in the algorithm. If we start out with an array of N elements, then each time the size of the array reduces to half for the next iteration, until we are left with just 1 element.
# 
# Initial length - `N`
# 
# Iteration 1 - `N/2`
# 
# Iteration 2 - `N/4` i.e. `N/2^2`
# 
# Iteration 3 - `N/8` i.e. `N/2^3`
# 
# ...
# 
# Iteration k - `N/2^k`
# 
# 
# Since the final length of the array is 1, we can find the 
# 
# `N/2^k = 1`
# 
# Rearranging the terms, we get
# 
# `N = 2^k`
# 
# Taking the logarithm
# 
# `k = log N`
# 
# Where `log` refers to log to the base 2. Therefore, our algorithm has the time complexity **O(log N)**. This fact is often stated as: binary search _runs_ in logarithmic time. You can verify that the space complexity of binary search is **O(1)**.
# 
# 
# 
# 

# ## Problem - Rotated Lists
# 
# We'll solve the following problem step-by-step:
# 
# > You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of `O(log N)`, where N is the length of the list. You can assume that all the numbers in the list are unique.
# >
# > Example: The list `[5, 6, 9, 0, 2, 3, 4]` was obtained by rotating the sorted list `[0, 2, 3, 4, 5, 6, 9]` 3 times.
# >
# > We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list `[3, 2, 4, 1]` produces `[1, 3, 2, 4]`. 
# >
# >"Sorted list" refers to a list where the elements are arranged in the increasing order  e.g. `[1, 3, 5, 7]`.
# >

# ### 2. Come up with some example inputs & outputs. Try to cover all edge cases.
# 
# Our function should be able to handle any set of valid inputs we pass into it. Here's a list of some possible variations we might encounter:
# 
# 1. A list of size 10 rotated 3 times.
# 2. A list of size 8 rotated 5 times.
# 3. A list that wasn't rotated at all.
# 4. A list that was rotated just once. 
# 5. A list that was rotated `n-1` times, where `n` is the size of the list.
# 6. A list that was rotated `n` times (do you get back the original list here?)
# 7. An empty list.
# 8. A list containing just one element.
# 9. (can you think of any more?)
# 
# We'll express our test cases as dictionaries, to test them easily. Each dictionary will contain 2 keys: `input` (a dictionary itself containing one key for each argument to the function and `output` (the expected result from the function). Here's an example.

# In[5]:


tests=[]
tests.append({'input':
              {'nums':[6,10,22,-1,0,3]},
             'output':3})
              


# In[2]:


tests


# In[6]:


tests.append({'input':{'nums':[5,6,9,0,2,3,4]},
             'output':3})


# In[7]:


tests.append({'input':{'nums':[1,2,3,4,5,6]},
             'output':0})


# In[8]:


tests.append({'input':{'nums':[6,1,2,3,4,5]},
             'output':1})


# In[9]:


tests.append({'input':{'nums':[-1,0,3,6,10,22]},
             'output':0})


# In[10]:


tests.append({'input':{'nums':[]},
             'output':0})


# In[11]:


tests.append({'input':{'nums':[1]},
             'output':0})


# In[12]:


test={'input':{'nums':[5,6,9,0,2,3,4]},
             'output':3}


# In[13]:


del tests[5]


# ## Linear Search

# In[20]:


def count_rotations(arr):
    position=0
    while position<len(arr):
        if position>0 and arr[position-1]>arr[position]:
            return position
        position=position+1
        
    return 0
    


# In[11]:


result=count_rotations(test['input']['nums'])
result


# In[18]:


tests


# In[21]:


for test in tests:
    result=count_rotations(test['input']['nums'])
    print(result)


# ## Using Binary Search 

# - first intialise the low and the high value which is the first and the last index respectively
# - then run a while loop till low<=high
# - initialize the mid and mid element
# - check if the mid is greater than 0 and mid-1 ele is greater than mid ele if yes return mid 
# - otherwise if arr[mid]<arr[high] then the smallest number will be on the left side then high=mid-1
# - if arr[mid]>arr[high] the smallest number will be on the right side the low=mid+1

# In[3]:


def count_rotations(arr):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if mid>0 and arr[mid-1]>arr[mid]:
            return mid
        elif arr[mid]<arr[high]:
            high=mid-1
        else:
            low=mid+1


# In[14]:


for test in tests:
    result=count_rotations(test['input']['nums'])
    print(result)


# _**Q (Optional): Implement the `count_rotations` function using the generic `binary_search` function.**_
# 
# Hint: You'll need to define the condition which returns `"found"`, `"left"` or `"right"` by performing the appropriate check on the middle position in the range.

# In[ ]:


def test_location(arr,mid):
    mid_number=arr[mid]
    if mid-1>0 and arr[mid-1]==mid_number:
        return mid-1
        
def locate_card(arr):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if mid>0 and arr[mid-1]>arr[mid]:
            result=test_location(arr,mid)
        elif arr[mid]<arr[high]:
            high=mid-1
        else:
            low=mid+1
    return result


# In[ ]:


arr=[5,1,2,2,3,4]
ans=locate_card(arr)
print(arr)


# In[ ]:




