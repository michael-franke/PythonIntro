#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# In this course, you will learn the basics of programming. Our language of choice will be **Python**, a *high-level, dynamically-typed* programming language. You will learn what that means later on. No prior knowledge in programming is required. At the end of this course, you should have acquired general-purpose knowledge relevant for *any* higher-level programming language, you should have learned how to write and interpret basic programs in Python, and you should be able to break down complex (data analysis) problems into algorithms aimed to solve the task at hand.  
# 
# ## Why programming?
# Some of you may be wondering why you should have to learn about *computer science* if you are studying *linguistics*. Answers to this question are manifold, but typically fall into two broad categories: 
# 
# 1. It's a necessary, or at least highly useful, **practical skill**: programming is essential to study implementation + data analysis, corpus data processing + analysis, natural language processing (NLP), computational modeling of language   
# 2. It trains your **logical, mathematical thinking** about structure and meaning in (natural and formal) languages: programming languages are formal languages with a strictly defined syntax and lexicon, but no pragmatics. They metaphorically allow you to "talk to" the computer. Computers act as naive, logical machines, requiring you to do the same when writing code: syntax errors, spelling mistakes, leaps in logical thinking, and ambiguity in the program will be punshed by errors or otherwise faulty output.
# 
# ## Higher- and lower-level programming languages
# Computers (more precisely, CPUs) work off binary code (also called machine code), a string of 1's and 0's that form machine commands such as "load", "store", ... . These are used to operate on units of data in the computer's register or memory.  
# 
# Binary code is a **low-level programming language**. It works directly on the machine's hardware components. Since each CPU or family of CPUs has its own specific machine language, binary code is hardware-specific. This is because each processor (or family of processors) has its own set of instructions, telling it to perform simple tasks, encoded as series of bits. 
# 
# For example, some CPUs may only use 32-bit instructions, in which the first 6 bits represent the operation to be performed, while the second 26 bits represent the operand (= the data to perform the operation on). That means that each instruction will be a series of 32 1's and 0's.  
# 
# **An example of a type of binary machine code**
# 
# | op | target address|
# | ------ | ------ |
# | jump | (to) address 1024 |
# | 000010 | 00000 00000 00000 10000 000000 |
# 
# Low-level programs are fast and memory-efficient, but writing programs directly in binary would be cumbersome. **High-level programming languages** are more user-friendly because they allow us to write instructions in a language that is easier (for us) to understand and because they are hardware-independent. Behind the surface, translators transform programs written in high-level languages into machine code that is readable for the computer. This is done by **"compilers"** or **"interpreters"**.  
# 
# For the rest of the course, we will be concerned with high-level programming languages only.
# 
# 
# ## Algorithms
# ### Definitions  
# In computer science, an algorithm refers to any finitely long instruction, consisting of a sequence of sub-commands. Algorithms are performed deterministically, not at random. Algorithms are usually employed to solve specific problems or perform tasks. In contrasts to heuristics, algorithms are fully specified task instructions.  
# 
# Some commonplace tasks can be thought of algorithmically:  
# 
# **Baking recipes**: Take 200g of flour, add 1 tsp of baking powder, mix. Add 1 egg...
# 
# **Navigation**: Go left in 200ms, then go straight ahead for 1km...  
# 
# Algorithms start from an **input** state (e.g., the set of raw ingredients in the recipe example, or your start position in the navigation example) and perform a set of operations to produce desired **output** (e.g., a chocolate cake, arriving at your goal position).  
# 
# ### Types of instructions
# 
# Some instructions operate directly on the element at hand:
# 
# **Examples:**  
# *divide x by 2*  
# *add 1 to y*
# 
# Other instructions are *conditional*:
# 
# **Example:**  

# In[1]:


get_ipython().run_cell_magic('capture', '', '"""\nIF you are using dark chocolate,\n    THEN add 100g of sugar,\nELSE IF you are using milk chocolate,\n    THEN add 50g of sugar.\nWHILE your dough is chunky,\n    keep whisking.\n"""   ')


# The above are examples of algorithms written in *pseudo-code*. These are not executable pieces of code, but a natural-language representation approximating the structure of a computer algorithm. 
# 
# Here is another example of an algorithm in pseudo-code. **Can you figure out what problem it solves?** (see the solution at the end of this page).

# In[2]:


get_ipython().run_cell_magic('capture', '', '"""\nDEFINE a function that takes a finite list of numbers L:\n    set x to the first number in L;\n    set y to the first number in L;\n    \n    for each element i in L:\n        if that element is BIGGER THAN x:\n            x = i\n        if that element is SMALLER THAN y:\n            y = i\n    return x and y\n"""')


# ## Python
# *Python* is a high-level programming language, just like *Java, Javascript, or C++*. It is also a *dynamically typed* programming language, meaning that some of its behaviours are evaluated at runtime, not during compilation (contrary to *statically typed* programming languages like *Java*). Statically typed programming languages require you to fully specify the relevant data types the code is operating on:  
# 
# **Example of static typing systems**:  
# 
# *int x = 2*  
# *int y = 1*  
# 
# *int z = x + y*
#   
#   
# By contrast, in dynamic typing systems the interpreter resolves the data type at run time. This can be advantageous because you have to expend less time on fixing all data types beforehand, particularly in cases where you might deal with a diverse set of data. On the other hand, it can be error-prone because type incompatibilites can sneak by until very late in development.
# 
# **Example of dynamic typing systems (our first piece of Python code)**:

# In[3]:


x = 2
y = 1
a = "duck"
b = 0.1

print(type(x))


# In[4]:


print(type(y))


# In[5]:


print(type(a))


# In[6]:


print(type(b))


# In[7]:


z = x + y

print(z)


# In[8]:


print(type(z))


# In[9]:


b = x + a


# As you see above, the data types are of *x* and *y* are interpreted as integers (=whole numbers), whereas *a* is interpreted as string variable (=series of letters). *b* is a float variable, that is, a number that contains a floating decimal point. We will learn more about different variable types in next week's session.  
# 
# For now, note that this assignment (correctly) results in a type error when we try to add "duck" to the integer 2. After all "duck" is not a number.  
# 
# But what happens if we want to add an integer and a float variable?

# In[8]:


c = x + b

print(c)


# In[9]:


print(type(c))


# The resulting variable *c* is of type float! In a statically typed language, we would have had to know beforehand whether we want *c* to be the sum of integers or float variables. In Python, we can let the interpreter work its magic for us.

# ### Setting up your Python environment
# To write your own code in Python, you first need to install Python. For this course, I am asking you to install *miniconda*, which includes *Python*, conda (a package management and installation system), and some additional useful packages we will need.  
# 
# * go to https://docs.conda.io/en/latest/miniconda.html
# * download the installer for Python 3.9 and your operating system 
# * execute the installer and follow the instructions
# 
# 
# Additionally, you will want to install *Spyder*, a scientific environment built to simplify code editing, debugging, and analysis. Only do the next steps *after* you have installed miniconda. 
# 
# * open a conda shell (Windows: Start menu > Anaconda > Anaconda PowerShell Prompt; Linux: Open shell > type "conda activate")
# * type: conda install spyder=5.2.2
# 
# Alternatively, if you already have older versions of the software installed, you can update to the latest versions of conda and Spyder by typing the following from your conda shell:
# 
# * conda update conda
# * conda update spyder

# ### Familiarization with the programming environment
# To open Spyder, first open a conda shell (see above). Then type "spyder". Spyder will open. The window will look something like this:
# 
# ![](https://www.dropbox.com/s/e30o864f4cnv6ws/spyder_layout.png?raw=1)
# 
# On the bottom right, you can see the **interactive console**. Here, your entered commands are evaluated immediately. We input (In \[1\]) *2+2* and immediately get *4* as output.  This is useful to execute or test small pieces of code.
# 
# On the left-hand side, you can see the **script window**. Here you can write code as Python *scripts*. Python script files are text files ending in ".py". Scripts have the advantage that they can be saved to disk, shared, printed, and so on. 
# 
# Python scripts can be **executed via the "Run" command** in Spyder. It is often useful during debugging to run scripts line by line or to only run selected lines. These options are available in Spyder too.  
# 
# Any variables created during the execution of scripts will appear in the **Variable Explorer** on the top right. For debuggigng purposes, it if often useful to check whether the variables appearing there behave as expected (correct data type?, correct data value?).

# (Finally, to answer the question about out piece of pseudo-code above: The pseudo-code algorithm found and returned the smallest and the biggest natural number in the list L.)
