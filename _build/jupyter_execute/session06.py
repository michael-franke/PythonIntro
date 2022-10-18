#!/usr/bin/env python
# coding: utf-8

# ## Finishing the basics: more on functions, loops, dictionaries, and files
# 
# The concepts introduced in previous sessions have additional functionalities worth introducing. In this session, we will therefore look at advanced (combined) uses of functions, loops, and file I/O, which allow you to code more efficiently. 

# ### Handling functions more efficiently
# 
# **Recap**:  
# 
# Functions are **reusable blocks of code that perform an action, like computing a value, on the basis of potentially changing parameters**. Functions are defined by a **def statement**, which specifies the name and arguments of the function. The indented code inside of the function block is the **body of the function**. Functions are executed by calling them; **function calls** use the function's name followed by parentheses, possibly containing a number of arguments within the parentheses. 

# In[1]:


import itertools

def sort_text(file):
    words = list()
    lines = [line.strip().split() for line in file] #list comprehension: for each line of text, strip it of white spaces and split it into separate strings per word  
    for word in itertools.chain.from_iterable(lines): #iterate through nested list
        words.append(word) #add all words to flattened list of words
    words.sort() #sort list
    return words
    
unsorted_file = open("hitchhikers_guide_full.txt", "r")

print(sort_text(unsorted_file))


# **Function calls are expressions, therefore they evaluate to objects** (see session 02). This means you can directly operate on them:

# In[2]:


unsorted_file = open("hitchhikers_guide_full.txt", "r")

sorted_tuple = tuple(sort_text(unsorted_file))


# Note also that **if you use the result of a function call only once it is unnecessary to assign it to a variable**: 

# In[3]:


unsorted_file = open("hitchhikers_guide_full.txt", "r")

#inefficient code:
sorted_file = sort_text(unsorted_file)
print(sorted_file)

#more efficiently:
print(sort_text(unsorted_file))


# Some functions and methods **don't return anything** (= return *None*), but **still modify the objects** passed as their arguments:

# In[4]:


#inefficient
sorted_file = sorted_file.sort(reverse = True) 

#more efficient
sorted_file.sort(reverse = True)


# **Don't forget that functions can call other functions!**

# In[24]:


def count_word_occurence(file):
    sorted_file = sort_text(file) #function call to user-defined function "sort_text"
    word = input()
    return "The word '{}' occurs {} times in the text.".format(word,sorted_file.count(word)) #note that we can use placeholders {} in the string, filled by the two objects named later

unsorted_file = open("hitchhikers_guide_full.txt", "r")

count_word_occurence(unsorted_file)


# ### More on loops
# 
# 

# In[ ]:




