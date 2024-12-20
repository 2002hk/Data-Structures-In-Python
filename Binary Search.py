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

# In[ ]:




