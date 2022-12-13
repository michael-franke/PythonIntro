#!/usr/bin/env python
# coding: utf-8

# ## Finishing the basics: more on functions, loops, dictionaries, and files (December 13, 2022)
# 
# The concepts introduced in previous sessions have additional functionalities worth introducing. In this session, we will therefore look at advanced (combined) uses of functions, loops, and file I/O, which allow you to code more efficiently. 
# 
# Let's start by looking at an example for a function that will accompany us throughout this session. LLet's figure out what this does:

# In[1]:


#an example
import itertools

def sort_text(file): #takes a plaintext file as input
    words = list()
    lines = [line.strip().split() for line in file] 
    print("For your reference, this is what lines looks like now: ", lines[1:10])   
    for word in itertools.chain.from_iterable(lines): 
        words.append(word) 
    words.sort()
    return words
    
unsorted_file = open("hitchhikers_guide_full.txt", "r")

print(sort_text(unsorted_file)[1:500]) #prints part of the output, not the full book


# Here is the same code again, but commented for its functionality:

# In[2]:


#an example
import itertools

def sort_text(file): #takes a plaintext file as input
    words = list()
    lines = [line.strip().split() for line in file] #list comprehension: for each line of text, strip it of white spaces and split it into separate strings per word  
    for word in itertools.chain.from_iterable(lines): #iterate through /nested/ list - important since lines from the book are nested lists in *lines*  
        words.append(word) #add all words to flattened list of words - i.e., no more nesting now!
    words.sort() #sort list
    return words
    
unsorted_file = open("hitchhikers_guide_full.txt", "r")

print(sort_text(unsorted_file)[1:500])#prints part of the output, not the full book


# ### Handling functions more efficiently
# 
# **Recap**:  
# 
# Functions are **reusable blocks of code that perform an action, like computing a value, on the basis of potentially changing parameters**. Functions are defined by a **def statement**, which specifies the name and arguments of the function. The indented code inside of the function block is the **body of the function**. Functions are executed by calling them; **function calls** use the function's name followed by parentheses, possibly containing a number of arguments within the parentheses. 

# **Function calls are expressions, therefore they evaluate to objects** (see session 02). This means you can directly operate on them:

# In[3]:


unsorted_file.seek(0) #reset file handle. I'll explain this in a bit...

sorted_tuple = tuple(sort_text(unsorted_file)) #transform return value from function to a tuple before storing in variable


# Note also that **if you use the result of a function call only once it is unnecessary to assign it to a variable**: 

# In[4]:


unsorted_file.seek(0) #reset file handle. I'll explain this in a bit...

#inefficient code:
sorted_file = sort_text(unsorted_file)
print(sorted_file[1:500])

unsorted_file.seek(0) 
#more efficiently:
print(sort_text(unsorted_file)[1:500])


# Some functions and methods **don't return anything** (= return *None*), but **still modify the objects** passed as their arguments. The list method *sort()* is such an example. Trying to assign the result of the function call to a new variable (presumably, you'd want a sorted list from *sort()*?) will not have the effect you want:

# In[5]:


#don't do this!
sorted_file_v2 = sorted_file.sort() #sorted_file is a list, but sort() does not return a new (sorted) list.
print(type(sorted_file_v2)) #so this is not what we would want


# In[6]:


#instead do this:
sorted_file.sort()
print(type(sorted_file))


# **Don't forget that functions can call other functions!**

# In[7]:


def count_word_occurence(file):
    sorted_file = sort_text(file) #function call to user-defined function "sort_text"
    word = input()
    return "The word '{}' occurs {} times in the text.".format(word,sorted_file.count(word)) 
    #note that we can use placeholders {} in the string, filled by the two objects named later

unsorted_file.seek(0) #reset file handle.

count_word_occurence(unsorted_file)


# ### More on loops
# 
# #### **Recap on *ranges***: 
# One of the most basic iterables is the range. The *range* function generates iterable sequences of numbers based on upto 3 input parameters: *range(i,n,k)* produces integers in the range from *i* to *n*-1, but only produces every *k*th integer in that sequence.
# 
# Ranges are **widespread and versatile for iterating over collections of elements** (lists, tuples, sets, dictionaries).

# In[8]:


for i in range(len(sorted_file)): #iterate over full length of list
    for j in range(17,20): #iterate over sequence of integers between 17 and 19
        if len(sorted_file[i])==j:
            print("The string '{}' has {} letters".format(sorted_file[i], j)) 


# **An issue for you to think of**: Try to understand the order of operations with nested loops. Why does the loop above not print output ordered by increasing string length, first printing all strings of length 17, then 18, 19,...? 

# #### **File handles are iterables**: 
# As you can see from the first code block in this session, loops can iterate over lines in a file. 
# 
# Note, though, that **file handles have *states***, that is, they **'remember where (in the file) they are'**. For this reason, you have to reset the state of the file handle if you want to loop over file handles multiple times, using ***file.seek(0)***.

# In[9]:


unsorted_file.seek(0)
print("The first 20 lines of the book are:\n")
for line in range(20):
    print(unsorted_file.readline())

#unsorted_file.seek(0) (use this command to reset the file handle)
print("\nBut if we loop over the file contents again, we continue where we left off:\n")
#this doesn't do what you think it might:
for line in range(20):
    print(unsorted_file.readline())


# ### Sorting, reverse sorting, sorting by key
# 
# Sorting elemens in a sequence or collection of objects is essential to many use-cases of programming. Luckily, the functionality of sorting functions in Python is much more versatile than we have seen thus far:
# 
# #### - *sort()* and *sorted()*
# As seen above, *sort()* modifies the original sequence it was passed. **To sort sequences or collections without disturbing the original sequence** of the object, use the ***sorted()*** function. *Sorted()* returns an ordered copy of the sequence passed as its argument:

# In[10]:


sorted_file_v3 = sorted(sorted_file, reverse = True) 
print(type(sorted_file_v3))


# #### - Sorting order
# The keyword ***reverse = True*** can be passed to both *sort()* and *sorted()* to reverse the sorting order from the **default sorting order**, which is **ascending** (numerically or alphabetically). 
# 
# Both *sort()* and *sorted()* can also be passed a ***key* parameter**, which can be used to specify alternative sorting orders. The key parameter **should be a function that takes a single argument** (the respective element of the to-be-sorted sequence) **and returns a key** (the value the function returns for the passed element) **to use for sorting purposes**. 
# 
# For instance, you may want to ignore capitalization when sorting list elements alphabetically:

# In[11]:


#case-insensitive string comparison
sorted_file_v3 = sorted(sorted_file, key = str.lower) #sorts all list elements as if they were lower-case versions of themselves
print(sorted_file_v3[1:500])


# #### - Sorting dictionaries by key or value
# **Dictionaries** are mappings between keys and values. As such, they are **not intrinsically ordered**. However, sometimes we may want to **sort dictionaries into a sequence of ordered elements**, e.g., when trying to read out the mapping between students' names and grades by order of their first/last name (A-Z) or grade (1-6 in the German system). 
# 
# By default, when applying the ***sorted()*** function, dictionaries are **sorted by their keys**. In fact, just feeding a dictionary straight to the *sorted()* function will simply return a sorted list of its keys.

# In[12]:


#initialize dictionary (see session04)
first_names = ["Arthur", "Ford", "Zaphod", "Marvin"]
last_names = ["Dent", "Prefect", "Beeblebrox", ""]
lifeform = ["Human", "Betelgeusian", "Betelgeusian", "Android"]
feature = ["Worried","Endlessly broad-minded","Two-headed","Paranoid"]

notebook = {"First name" : first_names, "Last name" : last_names, "Life form" : lifeform, "Distinct feature" : feature}


# In[13]:


print(sorted(notebook)) #just returns sorted list of keys


# **Option for sorting dictionary and returning a list sorted by key**: Using the dictionary method *items()*, we receive a dictionary view object, a list of tuples containing all key-value pairs (see also the methods *values()* and *keys()*, session 04). Calling *sorted()* on this object will return a list sorted by the dictionary's keys.

# In[14]:


print(sorted(notebook.items()))


# **Option for sorting dictionary and retuning a list sorted by value**: To sort a dictionary by value, we need to use a *key* parameter in the *sorted()* function that specifies which value of the dictionary elements to sort over.
# 
# - Remember that **the key parameter should be a function**. But there is no in-built function for getting dictionary values...
# 
# - Instead, a **lambda function** may be used to specify the sort key. Lambda functions are *anonymous* functions, that is, functions that are never defined with a name. They are useful when the function is only required for a short time/single application.
# 
# - Their syntax is:
#            
#            lambda arguments: expression
#     
# - This is akin to a function defined as:
#     
#         def function(arguments):
#             return expression
#     
# - Lambda functions can have **any number of arguments but only one expression**. That expression is **evaluated and returned**.

# In[15]:


#using a lambda function
print(sorted(notebook.items(), key = lambda x: x[1]))#sorts by value ==> here, alphabetical order of the lists containing our dictionary values (by their first element)


# - Alternatively, **the *operator* module** has convenience functions to fetch items from an operand, which can be any sequence or collection of elements:

# In[16]:


from operator import itemgetter

print(sorted(notebook.items(), key = itemgetter(1)))#sorts by value, same as the lambda function above


# ### ***While* loops, or "Anything you can do, *for* can do better"?**
# 
# We saw in an earlier session that *for* loops and *while* loops can be used to achieve the same outcome. So how should you decide which loop to choose in the first place?  
# 
# - *While* loops continue until a condition is False. *For* loops iterate over collections, iterable objects or generator functions.
# - As such, *for* loops are the natural choice for data structures that are already iterable.
# - *While* loops can be used on data structures that are not iterable. 
# - *While* loops may also be prefered if you do not know the number of required iterations beforehand.

# In[17]:


from random import randrange

playlist = ["Let It Be","Hey Jude","Here Comes The Sun","Something","Taxman","Eleanor Rigby","Yellow Submarine","Love You Do"]

command = "start"

print("Please choose an  option: \n 'repeat' -- repeat current song \n 'stop' -- stop playback \n other/no input -- continue playback\n")

while command !="stop":
    if command == "repeat":
        print("Repeating song:", current_song)
    else:
        current_song = playlist[randrange(7)] #on each execution, randrange picks a random integer from the specified range, here between 0 and 6
        print("Now playing: ", current_song ) 
    command = input()
print("Playback stopped.")   


# ### Notes on code efficiency and maintainability
# 
# #### Optimization
# For every **computable problem or task**, there are infinitely many programs which solve it; they will differ in **memory** and **time usage**. You may not care much about this for now, while working on toy examples with little computational demands. But if you **get used to writing reasonably efficient code** now, you will have a much easier time later!
# 
# **What does it mean for code to be efficient?** Some principles:
# 
# - **Avoid creating unnecessary objects**. *Do you really need that value stored in a variable?*
# - Conversely, **avoid computing the same thing twice** by storing the value in a variable. *Do you compute the same value on every execution of a loop? Why not save it in a variable?*
# - **Avoid running costly operations** (such as file I/O, search) multiple times. *Are you reading the same file at various places in your code? Why?*
# - **Use functions (and classes, see later sessions)** to generalize and modularize your code. Avoid declaring variables with global scope to prevent unnecessary clutter. *Will you really need that variable in your for loop again later on? Probably not...*
# 
# An extreme example:

# In[18]:


for i in range (2): #for i in range 0-1
    unsorted_file = open("hitchhikers_guide_full.txt", "r") #read in the file
    x = unsorted_file.readline().split() #read the first line, split into list of words
    global y #create global variable
    y = x[i] #save i-th word in list x in variable y
    print(y) #print variable


# The same thing, but more efficiently:

# In[19]:


for i in range (2): #for i in range 0-1
    unsorted_file.seek(0) #reset file handle
    print(unsorted_file.readline().split()[i]) #print i-th word in first line


# #### Maintainability
# 
# While **code efficiency** is about reducing **computational complexity**, **code maintainability** is about reducing **complexity for (human) programmers**. 
# 
# **Principles for code maintainability** include:
# - **Comment your code**, explain user-defined functions' behaviors, and use informative variable + function names to ensure your code is understandable to others
# - **Don't copy and paste** code, use functions and loops.
# - **Encapsulate elements** that are subject to change (e.g., user input, file I/O) and those that stay the same (e.g., functions, classes). This makes it easier to identify adaptable components.
# - **Minimize coupling** between different code components. This makes your code more *changeable*.
