#!/usr/bin/env python
# coding: utf-8

# ## Advanced data types: lists, tuples, dictionaries, sets
# 
# So far, we have dealt with data types that encode a single value -- a number, a string, or a Boolean value. In this session, we will learn about **data types that can contain multiple values**, which is essential when you are handling large amounts of data. At the end of this session, you should know the distinctions between four such data types, namely *lists*, *tuples*, *dictionaries*, and *sets*, and you should be able to write simple programs in which you create and modify these data types.

# ### Lists
# 
# Lists are the most elementary of the above-mentioned data types. They contain an **ordered sequence of values of any data type**, and can even contain other lists, allowing for the representation of hierarchically structured data.  
# 
# - Lists begin and end with square brackets 
# - Values inside of a list are called *elements* or *items* and are comma-delimited
# - Lists can contain the same element multiple times (unlike for sets, see below)
# - Lists are *mutable*, meaning that their items can be changed in place (unlike for strings)

# In[1]:


list_of_mammals = ["dog","chimpanzee","whale","platypus"]

random_collection = ["string",1,True,3.15,list_of_mammals] #lists can contain any other data type

print(random_collection)


# #### Operating on lists
# Many **list operations** are already known from strings:
# 
# - *list[k]* retrieves the *k*th item in the list
# - *len(list)* returns the number of items in the list
# - *list + list* concatenates two lists
# - *list * int* replicates the list *n* times
# - *list[i:k]* returns the *i*th to *k*th element of the list (see slicing for strings)

# In[2]:


len(list_of_mammals[2:]) #returns the length of the list from index position 2 until the end of the list


# If your list contains other lists, you can retrieve its elements using **multiple indexes**:

# In[3]:


random_collection[4][3] #returns the 3rd item of the list that is the 4th item of random_collection


# As mentioned above, **lists are mutable**. This means that we can we can directly add, remove, or change the values of a list without creating a new list.

# In[4]:


random_collection[0] = "my value has changed" #replace item at index 0 with a new item
print(random_collection)


# This property allows us to use of a number of **new methods**:
# 
# | Method |Operation |Example | Evaluates to|
# |---|---|---|---|
# | *in* / *not in* | tests for list membership | "platypus" in list_of_mammals | True|
# |*list.append(obj)*| adds object to the end of the list|list_of_mammals.append("horse")|['dog', 'chimpanzee', 'whale', 'platypus', 'horse']|
# |*list.insert(k,obj)*| adds object in front of the *k*th element|list_of_mammals.insert(2,"horse")|['dog', 'chimpanzee', 'horse', 'whale', 'platypus', 'horse']|
# |*list.index(obj)*| returns the index of the first occurence of obj on the list|list_of_mammals.index("horse")| 2|
# |*list.pop()*| deletes rand returns the rightmost element|list_of_mammals.pop()| "horse"|
# |*list.pop(k)*| eletes rand returns the *k*th element|list_of_mammals.pop(2)| "horse"|
# |*list.remove(obj)*| removed the first instance of obj on the list|list_of_mammals.remove("dog")| ['chimpanzee', 'whale', 'platypus']|
# |*list.reverse()*| reverses the list in place|list_of_mammals.reverse()| ['platypus', 'whale','chimpanzee']|
# |*list.sort()*| sorts the list in place|list_of_mammals.sort()| ['chimpanzee','platypus', 'whale']|

# #### Creating lists
# 
# Lists can be created in a number of ways:
# 
# - direct assignment: *list = [a,b,c]*
# - starting from an empty list: *list = []*
# - the *split* method
# - list comprehensions
# 
# The latter two require some explaining:  
# 
# (1) **The *split* method** is a string method we have so far ignored. It allows us to split a string into a list of its part. By default, it splits the string at whitespaces. However, two optional arguments can be used to (a) specify other splitting criteria and (b) specify the number of splits to be executed:  

# In[5]:


long_string = "Orbiting this at a distance of roughly ninety-two million miles is an utterly insignificant little blue green planet whose ape-descended life forms are so amazingly primitive that they still think digital watches are a pretty neat idea."

string_list = long_string.split()
print(string_list)


# In[6]:


hyphen_split_string = long_string.split("-") #split at hyphens
print(hyphen_split_string)


# In[7]:


single_hyphen_split_string = long_string.split("-",1) #only split once
print(single_hyphen_split_string)


# **As an aside: The reverse of the *split* method is the *join* method, which creates a string from a list of string elements, joining them by the string provided as its first argument.**

# In[8]:


" ".join(string_list)


# (2) **List comprehensions** are short-form syntax for a *for* loop over list elements. 
# 
# General syntax: *new list = [expression for item in iterable (if condition == True)]*
# 
# Let's look at some examples:

# In[9]:


#Example 1: Square Numbers
squared_numbers = [x*x for x in range(1,10)] #for all x in range(1,10) add x*x to the new list squared_numbers
print(squared_numbers)


# In[10]:


#Example 2: Capitalize and return all words containing the vowels 'a' or 'e' from a longer list of words 
upper_a_or_e_words = [x.upper() for x in string_list if ('a' or 'e') in x]
print(upper_a_or_e_words)


# #### Processing lists
# **(1) Loops**  
# 
# What the example above already showed you is that lists are **iterable**, meaning that we can process them element by element using a *for* loop.
# 
# Let's do the same thing as in Example 2 above, only using a *for* loop:

# In[11]:


upper_a_or_e_words_2 = []
for x in string_list:
    if ('a' or 'e') in x:
        upper_a_or_e_words_2.append(x.upper())
        
print(upper_a_or_e_words_2)


# **(2) Aggregation functions**
# 
# There are some simple and frequently used functions that process list elements:
# 
# - *sum()* on a list of numbers returns their sum: *sum([2,15,67]) = 84 *
# - *min()* and *max()* on a list of numbers return the minimum and the maximum value, respectively
# - on a list of strings, *min()* and *max()* return the string that is first and last in alphabetical order, respectively. 

# **(3) Advanced functions**
# 
# Two extremely useful function for processing lists are *enumerate(list)* and *zip(list1,..., listn)*.  
# 
# - ***Enumerate(list)*** allows us to loop over the elements in the list and and have an automatic counter. The result of that function is an *enumerate* object, which can be transformed back to a list of numbered tuples (see below for more on the tuple data type) or whose elements (both the list element and the counter) can be employed in *for* loops (see below)
# 

# In[12]:


counter_list = list(enumerate(list_of_mammals)) #loop over the list elements and count them. Assign the result back to a list
print(counter_list)


# In[13]:


for i, animal in enumerate(list_of_mammals):
    if i == 3:
        print("The animal at list index ",i," is ",animal)
    elif animal == 'whale':
        print("The index of the list element 'whale' is ",i)


# - ***Zip(list1,...listn)*** allows us to iterate over multiple lists at once. Just as for *enumerate*, the result of that function is a *zip* object, which can be transformed back to a list of paired tuples or whose elements can be iterated over in *for* loops (see below). 

# In[14]:


list_of_birds = ["robin","duck","penguin","pidgeon"]

list_of_animals = list(zip(list_of_mammals,list_of_birds))
print(list_of_animals)


# In[15]:


for mammal , bird in zip(list_of_mammals ,list_of_birds):
    print("a " + mammal +" is a mammal, a "+ bird + " is a bird")


# ### <span style="color:red">End of lecture 4 (November 22, 2022).</span>
# 
# 
# ### Tuples
# 
# ### Dictionaries
# 
# ### Sets
