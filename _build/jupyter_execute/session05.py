#!/usr/bin/env python
# coding: utf-8

# ## Modules, file I/O (input/output)
# 
# **So far, all of our Python programs were self-contained**, that is, they did not rely on external data files or pieces of code (except for in-built Python functions and methods). In most real-life situations, however, you will work off of existing files (e.g., for data analysis) or from pre-existing code (e.g., when adding new functionalities to an app or program). In this session, you will learn how to **import and use** external Python code as **modules** and how to **create, read from, and write to files**.
# 
# ### Modules
# 
# **Modules are python files intended for use in other Python programs**. Any *.py* file can be loaded as a module. As such, modules allow us **(a)** to **distribute code across multiple files** (which is convenient for bigger coding projects), and **(b)** to make use of **collections of useful functions** provided by other programmers. Many modules come with Python as part of the default installation. One such example is the *Itertools* module we saw in the previous session. Others include the *math* module and the *random* module, which contain helpful functions for mathematical operations and for probabilistic data.
# 
# Modules are **loaded with an *import* statement** (more below). Upon importing them, **all statements in the imported module are executed**.  
# 
# In the following, we will focus on the *math* module:
# 
# #### Import modules
# 
# Modules can be imported in three ways:
# 
# - *import math*: makes all objects available as math.object
# - *from math import func*: makes math.func available as func
# - *from example import long_function_name as func*: makes math.function_name_in_module available as func_name_in_my_code

# In[1]:


from math import factorial as fc #imports the function factorial(x) from the math module, assigns it the name fc

print(fc(4)) #prints 4!


# The names and functionalities of available modules can be looked up in Python's documentation: https://docs.python.org/3/py-modindex.html

# #### Example: Your homework as module
# 
# Our testing skripts import your homework as module. Your code gets loaded by *import ex_01*, which causes your function definitions to be assigned to the function names, and the unit tests will be executed on your definitions.  
# 
# The most basic element of our test code is the *assert* statement. Each such statement represents a basic fact which should hold if the program. For instance, *assertEquals(value, expression)* checks whether an expression correctly evaluates to a given value.   
# 
# The code below also uses an object constructor (a *class*) and the *self* attribute. You'll learn more about those in later sessions.

#     import unittest  
#     from ex_01 import *
# 
#     class TestTask1(unittest.TestCase):
# 
#         def test_br_to_am_1(self):
#             self.assertEqual("color", br_to_am("colour")) #checks whether the expression br_to_am("colour") 
#             self.assertEqual("honor", br_to_am("honour")) #evaluates to "color". If so, you get points!

# ### File I/O
# 
# #### Reading and writing to text files
# 
# #### File formats
# 
# #### FIle encodings
