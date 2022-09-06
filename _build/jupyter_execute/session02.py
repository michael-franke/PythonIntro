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
# The Boolean data type only encodes the logical values *True* and *False*, encodable in bytes as 1 and 0, respectively. The Boolean data type is highly useful in programming. Many operators and functions return Boolean values to indicate whether a statement fulfills a certain condition (e.g., is x bigger than y?) 

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
# Let's take a look at binary encodings of integers in a 16-bit system:
# 
# | decimal | 16-bit binary| | | | | | | | | | | | | | | |    
# | ------ | ------ | ------ |  ------ |------ |------ |------ |------ |------ |------ |------ |------ |------ |------ |------ |------ |------ |  
# | | 32768 | 16384 | 8192 | 4096 | 2048 | 1024 | 512 | 256 | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1|
# | 0 | 0|0|0|0| 0|0|0|0| 0|0|0|0| 0|0|0|0|  
# | 10 | 0|0|0|0 |0|0|0|0 |0|0|0|0 |1|0|1|0 |  
# | 150 | 0|0|0|0| 0|0|0|0| 1|0|0|1| 0|1|1|0| 
# | 32000 | 0|1|1|1| 1|1|0|1| 0|0|0|0| 0|0|0|0| 

# In[3]:


b = 300

print(type(b))


# #### Float
# 
# Floating-point numbers 
# 
# #### Complex
# 
# 
# Summary table
# 
# ### Strings
# 
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

# In[4]:


#Why does the following not work? 
a = false

#What will be the type of this variable?
a = "false"


# ## Variables and assignments
# 
# ### Operations
#  Homework: find out which operations work on which data types and to what results (e.g. using modulo on a boolean and so on....)
# 
# ## Comments
# 
# ## Simple functions
