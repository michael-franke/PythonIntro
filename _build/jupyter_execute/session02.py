#!/usr/bin/env python
# coding: utf-8

# # Data types and statements 
# 
# In this session, you will learn about the different **data types** Python can handle, about **storing data in variables** and modifying their contents through **assignment operators**, and about some of the essential basic **functions** in Python. At the end of this session, you should be able to write simple programs that assign, manipulate and return different types of data.  
# 
# ## Data types
# 
# When speaking of data types, we are refering to different **classes** that a value can belong to. Values always belong to exactly one data type, that is, if a value is of the *integer* type, for instance, it cannot simultaneously be of the *float* type. Integer values can be transformed into float values, however, as we will see below. 
# 
# ### Boolean
# 
# The Boolean data type only encodes the logical values *True* and *False*, encodable in bytes as 1 and 0, respectively. The Boolean data type is highly useful in programming. Many operators and functions return Boolean values to indicate whether a statement fulfills a certain condition (e.g., *is x bigger than y?*) 

# In[1]:


a = False
print(type(a))


# In[2]:


3 > 2 #the 'bigger than' operator is an example for an operator return a Boolean value


# **Question**: Why does the following not work? 

# In[3]:


false =1
a = false


# **Capitalization matters!** Just as natural languages have rules on capitalization (e.g. requiring capitalization of nouns in German), Python will only recognize *True* and *False*, with capital T/F as boolean values.   
# 
# Here, *false* is assumed to refer to a variable named *false*. However, as we haven't defined any such variable, Python returns a name error.

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

# In[4]:


b = 300

print(type(b))


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

# In[5]:


c = 15.5

print("c is of type",type(c))


# In[6]:


#Note that we can transform integer numbers into float numbers and the other way around.

#1. We can transform our int variable b into type float as follows:

d = float(b)
print("d equals",d)
print("d is of type",type(d))


# In[7]:


#2. We can transform our float variable c into an integer as follows:
e =int(c)
print("e equals",e)
print("CAREFUL! Note that tranforming floats into integers may change the value of your variable due to the loss of decimals. You will not receive a warning when this happens!")


# #### Complex
# As you may remember from maths classes, complex numbers employ the specific element *i*, called the imaginary unit, where i<sup>2</sup> = −1; every complex number can be expressed in the form *a + bi*, where a and b are real numbers.  
# 
# For some reason (feel free to go down the rabbithole on that one...), Python uses *j* instead of *i* to represent the imaginary unit. Complex numbers can thus be written as *x = a + bj*.

# In[8]:


f = 1 + 2j
print("f is of type",type(f))

print(f)


# What happens if we leave out either the real or imaginary part of the numbers? Let's try it out:

# In[9]:


g = 2j
print("g is of type",type(g))

print(g)


# In[10]:


h = 1 + 0j
print("h is of type",type(h))

print(h)


# #### Maths operators
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

# ### <span style="color:red">End of lecture 1 (October 25, 2022).</span>
# 
# ### Strings
# 
# String values are sequences of characters (length $\geq$ 0). Internally, they are stored as a sequence of letters, each of which has a specific bit encoding. Strings have to obey a number of rules:
# 
#  - must be surrounded by single ( 'string' ) or double quotes ( "string" )
# - only the other type of quotes is allowed inside a string:
#     - 'I am a "string"' is a string
#     - "I am a ’string’" is also a string
#     - "I am a "string"" is not a valid string
# - the backslash has special significance as an escape character, "some\time\ago" will look different from what you think
# - to produce an actual backslash, you need to have it twice: "some\\\time\\\ago"
# - Other common escape characters are:
#     - *\b* - Backspace         
#     - *\r* - Carriage Return                      
#     - *\n* - New Line                 
#     - *\’* - Single Quote    
#     - *\t* - Tab   

# In[11]:


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

# In[12]:


j = "\nWhere\nare\nyou?"

print(i+j)


# In[13]:


print(j*2)


# There are, however, a number of functions with specific functionalities for string operations.
# 
# 1. *len()* : returns the length of a string in number of characters. *len()* is an example of a **built-in function** which can also be applied to other objects representing sequences

# In[14]:


len(i)


# 2. *startswith()* and *endswith()*: tests whether a string starts/ends with a specific string. 
#     - Note that these are **methods** specific to string objects. They are therefore called on the object itself, typed as *str.startswith("x")*.
#     - They are sensitive to capitalization.
#     - You can feed a string of arbitrary length into startswith()/endswith(), even the full string whose contents you are testing.

# In[15]:


print(i.startswith("He"))


# In[16]:


print(i.startswith("he"))


# In[17]:


print(j.endswith("!"))


# In[18]:


print(j.endswith(j))


# 3. *in* and *index*: *in* is an operator that asks whether an object is contained in a sequence, whereas *index()* is a method that returns the position of that object in a sequence
#     - *in* will only return True or False, but will not tell you how many times an object is contained within the sequence
#     - *index()* starts counting at 0

# In[19]:


print("mäh" in "Rasenmäher")


# In[20]:


print("Rasenmäher".index("mäh"))


# 4. *lower()* and *upper()*: methods than return lower- or uppercase copies of the strings they operate on

# In[21]:


print(i.lower())


# In[22]:


print(j.upper())


# 5. *replace()*: method that replaces all instances of the first type with instances of the second
#    - an optional third argument can limit how many instances of the first type should be replaced

# In[23]:


k = "Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun."

print(k)


# In[24]:


print(k.replace(" ","_"))


# In[25]:


print(k.replace("a","AAA",2))


# 6. Slicing: To return just part of a string, you can indicate *which* part by way of its numerical indices
#     - *str[start : end]* will return a copy of the string starting with the character at *start* and ending with the character at *end*, where *start* and *end* are integer indices, respectively
#     - *str[start : ]* will return a copy of the string starting with the character at *start* 
#     - *str[ : end]* will return a copy of the string ending with the character at *end*  
#     - a position *-x* will be interpreted as *len(string)-s*
#     - providing a third number *k* will return every *k*th letter: *str[start : end : k]*

# In[26]:


print(k[0:7]) #returns letters 0-7


# In[27]:


print(k[:7]) #returns letters 0-7


# In[28]:


print(k[45:]) #returns all letters from the 45th letter to the end of the string


# In[29]:


print(k[::5]) #returns every 5th letter


# In[30]:


print(k[+20:-20:5]) #returns every 5th letter, starting 20 letters after the start of the string and ending 20 letters before its end


# #### Summary table
# 
# |Operator |Operation |Example |
# |---|---|---|
# |+| Append|"a "+ "ball" = "a ball"|
# |\*|Replication|"a" * 3 = "aaa" |
# | len(str) | Length |len("ball") = 4 | 
# |str.startswith(str)/str.endswith(str)|Checking start and end of string|"ball".startswith("b") = True |
# | str in str|Checking containment in string|"a" in "ball" = True |
# |str.index(str)|Checking position of string in string|"ball".index("a") = 1 |
# |str.upper()/str.lower()|Return lower- or uppercase copy of string|"ball".upper() = "BALL"|
# |str.replace(str,str,int)|Replace number of instances of the first string with instances of the second| "ball".replace("l","i",1) = "bail"|

# ## Data types that we will cover in later sessions
# 
# ### Sequences
# List, Tuple, Range
# 
# ### Mappings
# Dictionary, Set

# ## Variables and assignment
# Creating and modifying variables is one of the essential aspects to programming. **Variables** are names that **refer to values**. Variables are created upon their first assignment through an **assignment operator** (*=*). Attempting to evaluate a variable that has not yet been assigned will result in an error.  
# 
# Rules and conventions:
# - Important variables should get meaningful names (e.g., city = "Tübingen").
# - Throwaway/Temporary variables get single-letter names (e.g., a, b, i, j, ...). 
# - Variable names must start with a letter and can contain only letters, numbers, and underscores. Although they can start with an uppercase letter, it is convention to use lowercase variable names.

# In[31]:


l = "a"
m = 2
n = False

print(o)


# #### Variable assignment
# 
# Note that the assignment operator (*=*) is not the same as the equality operator known from maths! The **assignment statement binds a name**, on the left-hand side of the operator, **to a value**, on the right-hand side. To evaluate whether two sides of an equation, or alternatively two variables, are identical in their expressed value, use the *==* operator.  
# 
# The following example illustrates:

# In[32]:


o = 17


# In[33]:


17 = o


# In[34]:


17 == o


# Once you assign a new value to a variable, you lose (access to) its previous value. It is **often wise to create temporary copies of important variables**, which you can modify without losing knowledge of the original variable's value.

# In[35]:


o = o + 1

print(o)


# **Shorthand notation** for changing variable values:
# 
# - *a += b* increases the value of a by the value of b
# - analogously, *a -= b*, *a *= b*,*a /= b*
# - remember that + and * also have functionality for strings!

# In[36]:


o += 1

print(o)


# In[37]:


study_program = "Linguistics"
city = "Tübingen"
study_program += " in " + city

print(study_program)


# Some variable names are **illegal**. This is because Python uses a set of **keywords** with special functionality (you have already seen some of them earlier:*True*, *False*, *in*). These keywords define that language's syntax and structure; therefore they can't be used as variable names.
# 
# |Examples |of | keywords | |||
# |---|---|---|---|---|---|
# |and |	as |	assert |	break| 	class| 	continue|
# |def |	del |	elif |	else |	except |	exec|
# |finally | 	for| 	from  |	global |	if | 	import|
# |in |	is 	|lambda |	nonlocal | 	not |	or|
# |pass |	raise |	return |	try 	| while | 	with|
# |yield |	True |	False |	None|||

# ### Expressions vs. statements
# 
# A basic distinction to be aware of when programming is whether you are working on an **(evaluating) expression** or a **statement**.  
# 
# **Expressions** are pieces of code that **evaluate to an object** and do nothing else but to perform this evaluation. They can be (any combination of) values, variables, operators, and calls to functions. Typing expressions into the command prompt will cause Python to evaluate it and return its result.

# In[38]:


(20 + o) * 3


# While expressions ARE something, statements DO something. **Statements are instructions** for Python to execute. Examples that we have already encountered include variable assignments and the *print()* function. We will see other examples in later sessions. Typing statements into the command prompt will cause Python to execute that statement. This will not result in the display of results.

# In[39]:


p = "I am a statement" #no output from executing this line


# ### Comparison operators
# As we've seen, equality can be checked with the built-in *==* operator. This is not the only **comparison operator**:
# 
# |Operator |Operation |Example |
# |---|---|---|
# |==| equality| 3 == 2 + 1 (**True**)|
# |!=|inequality|3 != 1 (**True**)|
# | < / > | strictly smaller/bigger than | 1 < 2 (**True**) | 
# | <= / >= | smaller/bigger than or equal to |1 <= 1 (**True**) | 
# | is | identity (in terms of memory location)| a = 3; b = 3; a **is** b (**True**) | 
# 
# 
# **Question for practice**: How do you think these operators will behave if we use them to compare string or boolean variables? What if we compare two variables of different data types? Try it out!
# 
# 
