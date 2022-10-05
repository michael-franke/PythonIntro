#!/usr/bin/env python
# coding: utf-8

# # Functions and conditional execution
# 
# In this session, you will learn about **functions** and **flow control statements**. These are essential concepts to any programming language and will allow you to write more complex programs that execute blocks of statements based on variables types of input and output values. 
# 
# ## Preliminaries: Code structure
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
    z = 3
    global y 
    y = 4
    string_percentage("a",z)
    string_percentage("a",y)

outer_function()


# Note that variables that are only defined inside of a function body are **local variables** of that function. They do not exist once you exit the function.   
# You can create **global variables** inside a function by using the global keyword (see code block above).

# In[8]:


print(z)


# In[9]:


print(y)


# ### Return statements
# 
# A **return statement immediately terminates the function call**, causing program flow to revert to the
# place where function was called.
# 
# Return statements can have arguments which define the object that the function call will evaluate to. These arguments can be assigned to a variable like any other object. Return statements thus often serve to get information back from the inside of the function (without use of global variables). You can return expressions (see code block [10]) or variables (see code block [11]).  
# 
# **Python also supports the use of multiple return values**, separated by commas. The result of the function call needs to be assigned to the same number of variables, also separated by commas

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
# Conditional execution is an extremely important concept in any programming language. So far, most of our little programs were just lists of instructions that are executed in serial order. One of the strengths of programming, however, is that we can specify the conditions under which certain statements are to be executed, repeated, skipped, and so on.  
# 
# Like most programming languages, Python offers a range of such **flow control statements**.
# 
# 
# ### if
# The most basic flow control statement is the *if*-clause. It will execute the code block in its body *iff* (if and only if) the statement's condition is *True*. Its execution is skipped whenever the condition is *False*. We have seen an *if* statement before:

# In[3]:


x = 'Forest runs'

if 'runs' in x: #if variable x contains the string 'runs'
    y = x.replace('runs','walks',1) #replace its first instance with the string 'walks'
print(y) #then print the new variable


# #### if...else
# *If* statements can be optionally followed by *else* statements, which are executed *iff* the statement's condition is *False*.

# In[4]:


if 'runs' in y: #if variable x contains the string 'runs'
    z = y.replace('runs','walks',1) #replace its first instance with the string 'walks'
else:
    z = y.replace('Forest','Natasha')
print(z) #then print the new variable


# #### elif
# *If...else* statements will only execute one of two possible clauses. In cases with (many) more possible options, however, we can use the *elif* ("else if") statement instead. This statement has to follow another *if* or *elif* statement and provides a condition that is checked *iff* the conditions of the previous statements were *False*.  
# 
# *If* + *elif* statements can be (almost) arbitrarily long. Note, though, that **if multiple *elif* statements are provided, only the first one that evaluates to *True* will be executed.**  
# 
# Thus, given that z = *Natasha walks*, what will be the output of the following statement?

# In[5]:


if 'runs' in z: #if variable x contains the string 'runs'
    z = z.replace('runs','walks',1) #replace its first instance with the string 'walks'
elif 'walks' in z: #otherwise, if z contains 'walks'...
    z = z.replace('walks','runs') #...and so on
elif 'Forest' in z:
    z = z.replace('Forest','Natasha')
elif 'Natasha' in z:
    z = z.replace('Natasha', 'Forest')
else:
    print("String does not contain any of these words.")
    
print(z) #then print the variable


# With an *else* statement at the end of an *if...elif* expression you can make sure that something is returned if all conditions evaluate to *False* (see code block [20]). 
# 
# Finally, **flow control statements can be nested**:

# In[6]:


if 'runs' in z: #if variable z contains the string 'runs'
    if 'Natasha' in z: #and contains the string 'Natasha'
        z = z.replace('Natasha runs', 'Forest walks')
    elif 'Forest' in z: 
        z = z.replace('Forest runs', 'Natasha walks')
else:
    print("String does not contain 'runs'.")
    
print(z) #then print the variable


# ### Intermezzo: Complex Boolean Expressions
# 
# All of the conditions for *if* statements specified so far used a single Boolean operator: **in**. We can also specify more complex conditions for conditional execution by:
# 
# - using the **comparison operators** introduced in Session 02 (*==*, *!=*, *</>*, *<=/>=*, *is*)
# - and combining them with **Boolean operators** (*and*, *or*, *not*)
# 
# Boolean operators follow the rules known from logic:
# 
# - *A and B* is true *iff* A is true and B is true
# - *A or B* is true *iff* A is true or B is true or both A and B are true
# - *not A* is true *iff* A is false

# In[9]:


if 'walks' in z and len(z) < 20:
    z = z + ' for a long time'
elif 'walks' in z and (z.startswith('Forest') or z.startswith('Natasha')):
    z = z + '. What is Ming doing now?'
print(z)


# ### <span style="color:red">End of lecture 3 (November 15, 2022).</span>
# 
# ### *while* loops
# Loops introduce a central feature of programming language, iterating over the same sequence of statements multiple times. While an *if* statement just executes once if its condition is met, loops keep executing for as long as their condition holds. Loops **reduce the need for code duplication** and are **quite flexible at runtime** (e.g., when the number of times we'll have to run a sequence of statements depends on varying parameter values such as the length of a string).  
# 
# Note, however, that **loops may continue forever** unless a terminating criterion is reached.  
# 
# We have already seen one example for a loop, the **while** loop. This loop repeats executing the code in its body as long as its condition is met.

# In[10]:


x = 'Forest runs'

while ('and runs and runs' not in x): #while this is the case
    x += ' and runs' #do this
#terminates as soon as the string includes 'and runs and runs'    
x+='.'
print(x)


# Non-terminating loops often happen out of carelessness. To avoid them:
# 
# - be very careful to cover boundary cases
# - define additional exit points using *break* statements (see below)
# - ensure that the test condition changes in each iteration (as in code block [10], but not always possible)

# In[14]:


#Example of a non-terminating loop
reply = ""
while (reply != "Who's there?"):
    print("Knock knock")
    reply = "Yes?"
    print(reply)
    #reply = input() #allowing user input would enable changing the value of reply on every iteration
print("Stop asking questions and let me in.")


# #### Exiting the loop with 'break' or 'continue'
# *Break* causes the loop to stop at the point at which it appears, without completing the current iteration. This is useful to ensure termination for certain cases.  
# 
# *Continue* statements end the current iteration of the loop and cause it to repeat from the top. This is useful if there are cases you'd like to skip or ignore.

# In[34]:


reply = ""
while (reply != "Who's there?"):
    print("Knock knock")
    reply = input() #user can input their reply
    if reply == "Yes?":
        break #exits loop immediately
    elif reply == "Who's there?":
        continue #causes the loop to end and starts again from the top by evaluation whether reply != "Who's there".
    else:
        print("Try again:") 
        reply = input() #otherwise, allow user to enter new reply
print("Stop asking questions and let me in.")


# ### *for* loops
# *While* loops execute a statement for as long as their condition is true, but often we only want to **execute the code block in the loop's body a certain number of times or for a certain range of variable values**. The *for* loop does just that: it executes the code in its body **for all x in y**, where **x is a variable** and **y is an iterable**. The variable x need not have a value assigned to it before entering the loop. It will automatically iterate over all elements of y.
# 
# **Iterables** can have various types:
# 
# - *strings*: variable is assigned each character of the string in turn
# - *ranges*: variable is assigned to iterable sequence of numbers, see details below
# - *lists*,*tuples*,*sets*,*dictionairies*: next week

# In[49]:


#for loop on strings
char_num = 1
example_string = "Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun."
for i in example_string: #for each character in the example string
    print("The letter at position",char_num,"is",i) #print this
    char_num += 1 #then iterate the character number by 1
#terminates at the end of the string


# #### Ranges
# 
# The *range* function generates iterable sequences of numbers based on upto 3 input parameters:
# 
# - *range(n)* generates a sequence of integers from 0 to n-1. For instance, *range(10)* generates 0,1,2,3,4,5,6,7,8,9
# - *range(i,n)* generates a sequence of integers from i to n-1. For instance *range(10,20)* generates 10,11,12,13,14,15,16,17,18,19
# - *range(i,n,k)* generates sequences of integers from i to n-1, but only generates every *k*th integer in that sequence. For instance *range(1,20,5)* generates 1,6,11,16

# In[48]:


#for loop on numbers
example_string = "Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun."
for i in range(1,20,5): #for each character in the example string
    print("The letter at position",i,"is",example_string[i-1]) #print this
#terminates at the end of the string

