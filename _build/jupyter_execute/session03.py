#!/usr/bin/env python
# coding: utf-8

# ## Code structure
# 
# Proper **formatting** of your code is essential to ensure that it runs in the intended order and is understandable to others (as well as your future self). Code readability is also improved by documentation in the form of **comments/annotations**, which, in addition, are a useful tool in debugging (cf. **rubber duck debugging**: https://en.wikipedia.org/wiki/Rubber_duck_debugging). 
# 
# 
# ### Indentation
# 
# For advanced constructs, **lines of code are organised in blocks**. Blocks specify sequences of statements that are always executed together in the same order. Blocks are organised through levels of code indentation. There are three rules for blocks.  
# 
# - Blocks begin when the indentation increases.
# - Blocks can contain other blocks.
# - Blocks end when the indentation decreases to zero or to a containing block’s indentation.  
# 
# This will be easier to understand by way of example:

# In[1]:


x = 'Forest runs'

while ('and runs and runs' not in x):
    x += ' and runs'
x+='.'
print(x)
    


# Note that the period is only added once we have exited the inner block (or *loop*). We will lean more about loops later.

# ### Commenting
# Comments are parts of the code that are ignored by the interpreter. Typical uses for comments include:
# 
# - explaining in natural language what a segment of code does 
# - describing what can be done with a user-defined function
# - adding authorship and version information to the beginning of a file
# - temporarily “de-activating” lines to test other parts of the code
# 
# Single-line comments are preceded by a hash character (#). Multi-line comments start and end with three (single or double) quotation marks.

# In[2]:


if 'runs' in x: #if variable x contains the string 'runs'
    y = x.replace('runs','walks',1) #replace its first instance with the string 'walks'
print(y) #then print the new variable    


# In[3]:


"""
You will often find multi-line comments like this providing authorship information at the beginning of code files.
You may also place them before a new block of code in order to explain its functionality.

Author: Juliane Schwab, 2022
version: Python 3
"""


# ### Naming variables and functions
# 
# Lastly, using meaningful labels for important variables and functions makes it easier for others to understand their purpuse. To reiterate from session 2:
# 
# - Important variables should get meaningful names (e.g., city = "Tübingen").
# - Throwaway/Temporary variables get single-letter names (e.g., a, b, i, j, ...).

# ## Functions
# Functions are **reusable blocks of code that perform an action, like computing a value, on the basis of potentially changing parameters**. We have seen examples of (in-built) functions before: *print()* prints its argument to the standard output device, *float()* transforms its argument to a floating-point number.
# 
# Functions are invaluable to programming for several reasons:
# 
# - **generalization**: functions avoid code duplication due to controlled execution through parameters
# - **reusability**: functions can be transfered between programs without loss of functionality
# - **manageability**: functions split code into easy-to-read chunks/blocks
# - **encapsulation**: functions can be used by other programmers without requiring knowledge of the implementation
# 
# Functions are defined by a **def statement**, which specifies the name and arguments of the function. The indented code inside of the function block is the **body of the function**. Functions are executed by calling them; **function calls** use the function's name followed by parentheses, possibly containing a number of arguments within the parentheses. Note that functions can only be called *after* they have been defined.
# 
# Upon calling a function, executing of the code jumps into the function and returns to the line from which the function was called only after the execution of the function has ended.

# In[4]:


print("Start")

def course_information(year): #def(inition) statement
    print("Programming in Python. University of Tübingen. Winter term", year)#function body
    #the function ends here

print("Nothing has printed yet! Only now we're calling the function:")
course_information(2022) #function call with parameter "2022"
print("Stop")


# ### Code optimisation through functions
# 
# Suboptimal code contains unnecessary duplications that could be avoided by specifying a function to do the job. In general, this type of code if difficult to read and to de-bug because you'll have to remember to change the code everywhere you copied it.
# 
# #### Example of suboptimal code:

# In[5]:


word1 = "we"
word2 = "are"
word3 = "programming"

combined_length = len(word1) +len(word2) + len(word3)

w1_percentage = len(word1) / combined_length
w2_percentage = len(word2) / combined_length
w3_percentage = len(word3) / combined_length

print(w1_percentage)
print(w2_percentage)
print(w3_percentage)


# #### Example of optimized code

# In[6]:


def string_percentage(word,length):
    print(len(word)/length)

#flexible use of function with varying input:    
string_percentage(word1,combined_length)
string_percentage(word1, 20)
string_percentage("love",20)


# ### Nested function calls
# 
# Functions can be called within functions. Be wary of the order in which code blocks are executed, particularly for more complex programs with many nested function calls.

# In[7]:


def outer_function():
    x = 3
    global y 
    y = 4
    string_percentage("a",x)
    string_percentage("a",y)

outer_function()


# Note that variables that are only defined inside of a function body are **local variables** of that function. They do not exist once you exit the function.   
# You can create **global variables** inside a function by using the global keyword (see code block above).

# In[8]:


print(x)


# In[9]:


print(y)


# ### Return statements
# 
# A **return statement immediately terminates the function call**, causing program flow to revert to the
# place where function was called.
# 
# Return statements can have arguments which define the object that the function call will evaluate to. These arguments can be assigned to a variable like any other object. Return statements thus often serve to get information back from the inside of the function (without use of global variables).  
# 
# Python also supports the use of multiple return values, separated by commas. The result of the function call needs to be assigned to the same number of variables, also separated by commas

# In[10]:


def string_percentage(word,length):
    return(len(word)/length)

x = string_percentage("return",20)
print(x)


# In[11]:


def get_word_statistics(word , length):
    word_percentage = (len(word)/length)
    return word , len(word), word_percentage

w, wlen , wperc = get_word_statistics("return" ,20)
print(w + " (length:" + str(wlen) + ", percentage: " + str(wperc) + ")")


# **What happens if nothing is returned?**  
# 
# Python has a *None* value, which represents the absence of a value. None must be typed with a capital N.
# 
# Internally, Python adds *return None* to the end of any function body with no return statement. If you assign the result of a function call without return value to a variable, that variable will also have the *None* value (see code block below).

# In[12]:


def string_percentage(word,length):
    return #function execution ends here!
    return(len(word)/length) #never reached

x = string_percentage("return",20)
print(x)


# ## Conditional execution
# 
# ### for-loop
# ### while-loop
# ### if-loop
# - if else
# ....
# 
# 
# ## Functions(session 4 only???)
# 
# - defining functions
# - return values
# - calling functions
# 
# 
# ## Modules(?)
# - importing modules
# - ....
