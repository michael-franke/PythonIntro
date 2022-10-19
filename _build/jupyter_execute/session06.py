#!/usr/bin/env python
# coding: utf-8

# ## Finishing the basics: more on functions, loops, dictionaries, and files
# 
# The concepts introduced in previous sessions have additional functionalities worth introducing. In this session, we will therefore look at advanced (combined) uses of functions, loops, and file I/O, which allow you to code more efficiently. 

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


# ### Handling functions more efficiently
# 
# **Recap**:  
# 
# Functions are **reusable blocks of code that perform an action, like computing a value, on the basis of potentially changing parameters**. Functions are defined by a **def statement**, which specifies the name and arguments of the function. The indented code inside of the function block is the **body of the function**. Functions are executed by calling them; **function calls** use the function's name followed by parentheses, possibly containing a number of arguments within the parentheses. 

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

# In[4]:


def count_word_occurence(file):
    sorted_file = sort_text(file) #function call to user-defined function "sort_text"
    word = input()
    return "The word '{}' occurs {} times in the text.".format(word,sorted_file.count(word)) #note that we can use placeholders {} in the string, filled by the two objects named later

unsorted_file = open("hitchhikers_guide_full.txt", "r")

count_word_occurence(unsorted_file)


# ### More on loops
# 
# **Recap on *ranges***: One of the most basic iterables is the range. The *range* function generates iterable sequences of numbers based on upto 3 input parameters: *range(i,n,k)* produces integers in the range from *i* to *n*-1, but only produces every *k*th integer in that sequence.
# 
# Ranges are **widespread and versatile for iterating over collections of elements** (lists, tuples, sets, dictionaries).

# In[21]:


for i in range(len(sorted_file)): #iterate over full length of list
    for j in range(17,20): #iterate over sequence of integers between 17 and 19
        if len(sorted_file[i])==j:
            print("The string '{}' has {} letters".format(sorted_file[i], j)) 


# **An issue for you to think of**: Try to understand the order of operations with nested loops. Why does the loop above not print output ordered by increasing string length, first printing all strings of length 17, then 18, 19,...? 

# **File handles are iterables**: As you can see from the first code block in this session, loops can iterate over lines in a file. 
# 
# Note, though, that **file handles have *states***, that is, they **'remember where (in the file) they are'**. For this reason, you have to reset the state of the file handle if you want to loop over file handles multiple times, using ***file.seek(0)***.

# In[37]:


unsorted_file = open("hitchhikers_guide_full.txt", "r")
print("The first 20 lines of the book are:\n")
for line in range(20):
    print(unsorted_file.readline())

#unsorted_file.seek(0) (use this command to reset the file handle)
print("\nBut if we loop over the file contents again, we continue where we left off:\n")
#this doesn't do what you think it might:
for line in range(20):
    print(unsorted_file.readline())


# ***While* loops, or "Anything you can do, *for* can do better"?**
# 
# We saw in an earlier session that *for* loops and *while* loops can be used to achieve the same outcome. So how should you decide which loop to choose in the first place?  
# 
# - *While* loops continue until a condition is False. *For* loops iterate over collections, iterable objects or generator functions.
# - As such, *for* loops are the natural choice for data structures that are already iterable.
# - *While* loops can be used on data structures that are not iterable. 
# - *While* loops may also be prefered if you do not know the number of required iterations beforehand.

# In[ ]:


from random import randrange

playlist = ["Let It Be","Hey Jude","Here Comes The Sun","Something","Taxman","Eleanor Rigby","Yellow Submarine","Love You Do"]

command = "start"

print("Please choose an  option: \n 'repeat' -- repeat current song \n 'stop' -- stop playback \n other/no input -- continue playback\n")

while command !="stop":
    if command == "repeat":
        print("Repeating song:", current_song)
    else:
        current_song = playlist[randrange(7)]
        print("Now playing: ", current_song ) 
    command = input()
print("Playback stopped.")   


# ### Sorting, reverse sorting, sorting by key
# 
# So far we've primarily relied on the **default sorting order**, which is in **ascending** order (numerically or alphabetically). 
