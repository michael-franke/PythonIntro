#!/usr/bin/env python
# coding: utf-8

# # Data types and statements
# 
# In this session, you will learn about the different **data types** Python can handle, about **storing data in variables** and modifying their contents through **assignment operators**, and about some of the essential basic **functions** in Python. At the end of this session, you should be able to write simple programs that assign, manipulate and return different types of data.  
# 
# ## Data types
# 
# When speaking of data types, we are refering to different **categories** that a value can belong to. Values always belong to exactly one data type, that is, an if a value is of the *integer* type, for instance, it cannot simultaneously be of the *float* type. Integer values can be transformed into float values, however, as we will see below. 
# 
# ### Boolean
# 
# The Boolean data type only encodes the logical values *True* and *False*, encodable in bytes as 1 and 0, respectively. The Boolean data type is highly useful in programming. Many operators and functions return Boolean values to indicate whether a statement fulfills a certain condition (e.g., *is x bigger than y?*) 

# In[1]:


a = False
print(type(a))


# In[2]:


3 > 2 #the 'bigger than' operator is an example for an operator return a Boolean value


# ### Numbers 
# 
# Values that are numbers can belong to three distinct categories: *integers*, *floating-point numbers*, or *complex* numbers.
# 
# #### Integer
# 
# Integer values are **whole numbers**, e.g. -300, 0, 300.  
# 
# Integer values can be stored in bits. In a 32-bit encoding, integers up to the size of 2.147.483.648 can be respresented.  
# 
# Binary encoding uses 2's complement. Let's take a look at binary encodings of integers in a 16-bit system:
# 
# | decimal | 16-bit binary| | | | | | | | | | | | | | | |    
# | ------ | ------ | ------ |  ------ |------ |------ |------ |------ |------ |------ |------ |------ |------ |------ |------ |------ |------ |  
# | | 32768 | 16384 | 8192 | 4096 | 2048 | 1024 | 512 | 256 | 128 | 64 | 32 | 16 | $2^3$ = 8 | $2^2$ = 4 | $2^1$ = 2 | $2^0$ = 1|
# | 0 | 0|0|0|0| 0|0|0|0| 0|0|0|0| 0|0|0|0|  
# | 10 | 0|0|0|0 |0|0|0|0 |0|0|0|0 |1|0|1|0 |  
# | 150 | 0|0|0|0| 0|0|0|0| 1|0|0|1| 0|1|1|0| 
# | 32000 | 0|1|1|1| 1|1|0|1| 0|0|0|0| 0|0|0|0| 

# In[3]:


b = 300

print(type(b))


# **Question**: Can we represent negative numbers in this system? It will be part of your homework to figure this out.

# #### Float
# 
# Positive and negative numbers with a decimal point are called *floating-point numbers*. Floating-point numbers are expressed by their **sign** (positive/negative), their **mantissa**, and their **exponent to the power of two**.  
# 
# 15.5 = +1.9375 $\times$ $2^3$  
# 
# This type of representation allows for efficient encoding and representations of very large numbers in binary form. Let's see how this is achieved:  
# 
# In a 16-bit encoding, 1 bit is allocated to the sign (0 = positive, 1 = negative), 6 are allocated to the exponent (in binary encoding using 2's complement), and 9 are allocated to the mantissa (in binary encoding using 2's complement with negative exponent).   
# 
# Since there may be multiple matching mantissa and exponents for representing a number like 15.5, we assume a **normalized mantissa** that always carries a 1 before its decimal point, i.e. *1 $\leq$ mantissa < 2*. Since it is redundant to encode the 1 and decimal point, they are left out of the encoded form, but can always be understood to be present at the left of the mantissa (see below).  
# 
# Given *x* = 15.5  
# 
# 1. Determine the sign: positive sign = 0  
# 2. Determine the exponent: find the largest 2<sup>e</sup> $\leq$ x 
# 3. Determine the mantissa: *m* = x / 2<sup>e</sup> with *e* according to step 2.
# 4. Transform to binary encoding:
# 
# | sign | (pre-decimal) | reduced mantissa | | | | | | | | | exponent | | | | | |
# | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
# | pos. | (1.) | 2<sup>-1</sup> =  $\frac{1}{2}$ | 2<sup>-2</sup> = $\frac{1}{4}$ | 2<sup>-3</sup> | 2<sup>-4</sup> | 2<sup>-5</sup> | 2<sup>-6</sup> | 2<sup>-7</sup> | 2<sup>-8</sup> | 2<sup>-9</sup> | 32 | 16 | 8 | 4 | 2 | 1 |
# | 0 | | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  

# In[4]:


c = 15.5

print("c is of type",type(c))


# In[5]:


#Note that we can transform integer numbers into float numbers and the other way around.

#1. We can transform our int variable b into type float as follows:

d = float(b)
print("d equals",d)
print("d is of type",type(d))


# In[6]:


#2. We can transform our float variable c into an integer as follows:
e =int(c)
print("e equals",e)
print("CAREFUL! Note that tranforming floats into integers may change the value of your variable due to the loss of decimals. You will not receive a warning when this happens!")


# #### Complex
# As you may remember from maths classes, complex numbers employ the specific element *i*, called the imaginary unit, where i<sup>2</sup> = −1; every complex number can be expressed in the form *a + bi*, where a and b are real numbers.  
# 
# For some reason (feel free to go down the rabbithole on that one...), Python uses *j* instead of *i* to represent the imaginary unit. Complex numbers can thus be written as *x = a + bj*.

# In[7]:


f = 1 + 2j
print("f is of type",type(f))

print(f)


# What happens if we leave out either the real or imaginary part of the numbers? Let's try it out:

# In[8]:


g = 2j
print("g is of type",type(g))

print(g)


# In[9]:


h = 1 + 0j
print("h is of type",type(h))

print(h)


# ### Maths operators
# 
# We can perform a range of simple mathematical operations on numerical data types, such as subtraction, addition, multiplication, and so on...
# 
# |Operator |Operation |Example |Evaluates to |
# |---|---|---|---|
# | - | Subtraction |5 - 2 | 3 |
# |+| Addition|2 + 2|4|
# |\*|Multiplication|2 \* 2|4|
# |/|Division|5 / 2|2.5|
# |\*\*|Exponent|2 ** 3|8|
# |%|Modulus/remainder|22 % 8|6|
# |//|Integer division/floored quotient|22 // 8|2|

# ### Strings
# 
# String values are a sequence of characters. The have to obey a number of rules:
# 
#  - must be surrounded by single ( 'string' ) or double quotes ( "string" )
# - only the other type of quotes is allowed inside a string:
#     - 'I am a "string"' is a string
#     - "I am a ’string’" is also a string
#     - "I am a "string"" is not a valid string
# - the backslash has special significance as an escape character, "some\time\ago" will look different from what you think
# - to produce an actual backslash, you need to have it twice: "some\\time\\ago"
# - Other common escape characters are:
#     - *\b* - Backspace         
#     - *\r* - Carriage Return                      
#     - *\n* - New Line                 
#     - *\’* - Single Quote    
#     - *\t* - Tab   

# In[10]:


i = "Hello world!"

print(i)
print(type(i))


# #### Simple string operations
# 
# You cannot perform mathematical operations on strings, with two exceptions:
# 
# 1. The *+* operator represents concatenation of strings, not addition. Concatenation means joining two strings by their ends.
# 2. Strings can be replicated by mutiplication with an integer number.
# 

# In[11]:


j = "\nWhere\nare\nyou?"

print(i+j)


# In[12]:


print(j*2)


# There are, however, a number of functions with specific functionalities for string operations.
# 
# 1. *len()* : returns the length of a string in number of characters. *len()* is an example of a **built-in function** which can also be applied to other objects representing sequences

# In[13]:


len(i)


# 2. *startswith()* and *endswith()*: tests whether a string starts/ends with a specific string. 
#     - Note that these are **methods** specific to string objects. They are therefore called on the object itself, typed as *str.startswith("x")*.
#     - They are sensitive to capitalization.
#     - You can feed a string of arbitrary length into startswith()/endswith(), even the full string whose contents you are testing.

# In[14]:


print(i.startswith("He"))


# In[15]:


print(i.startswith("he"))


# In[16]:


print(j.endswith("!"))


# In[17]:


print(j.endswith(j))


# 3. *in* and *index*: *in* is an operator that asks whether an object is contained in a sequence, whereas *index()* is a method that returns the position of that object in a sequence
#     - *in* will only return True or False, but will not tell you how many times an object is contained within the sequence
#     - *index()* starts counting at 0

# In[18]:


print("mäh" in "Rasenmäher")


# In[19]:


print("Rasenmäher".index("mäh"))


# 4. *lower()* and *upper()*: methods than return lower- or uppercase copies of the strings they operate on

# In[20]:


print(i.lower())


# In[21]:


print(j.upper())


# 5. *replace()*: method that replaces all instances of the first type with instances of the second
#    - an optional third argument can limit how many instances of the first type should be replaced

# In[22]:


k = "Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun."

print(k)


# In[23]:


print(k.replace(" ","_"))


# In[24]:


print(k.replace("a","AAA",2))


# 6. Slicing: To return just part of a string, you can indicate *which* part by way of its numerical indices
#     - *str[start : end]* will return a copy of the string starting with the character at *start* and ending with the character at *end*, where *start* and *end* are integer indices, respectively
#     - *str[start : ]* will return a copy of the string starting with the character at *start* 
#     - *str[ : end]* will return a copy of the string ending with the character at *end*  
#     - a position *-x* will be interpreted as *len(string)-s*
#     - providing a third number *k* will return every *k*th letter: *str[start : end : k]*

# In[25]:


print(k[0:7]) #returns letters 0-7


# In[26]:


print(k[:7]) #returns letters 0-7


# In[27]:


print(k[45:]) #returns all letters from the 45th letter to the end of the string


# In[28]:


print(k[::5]) #returns every 5th letter


# In[29]:


print(k[+20:-20:5]) #returns every 5th letter, starting 20 letters after the start of the string and ending 20 letters before its end


# ### Sequences
# 
# #### List
# 
# #### Tuple
# 
# #### Range
# 
# ### Mappings
# 
# #### Dictionary
# 
# #### Set
# 
# There are other data types...

# In[30]:


#Why does the following not work? 
a = false

#What will be the type of this variable?
a = "false"


# ## Variables and assignments
# 
# ### Comparisons and logical operators
#  Homework: find out which operations work on which data types and to what results (e.g. using modulo on a boolean and so on....)
# 
# ## Comments
# 
# ## Simple functions
