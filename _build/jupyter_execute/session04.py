#!/usr/bin/env python
# coding: utf-8

# ## Advanced data types: lists, tuples, sets, dictionaries (November 22 and 29, 2022)
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
# Three extremely useful functions for processing lists are *enumerate(list)*, *zip(list1,..., listn)*, and *map(function, list)*.  
# 
# - ***enumerate(list)*** allows us to loop over the elements in the list and and have an automatic counter. The result of that function is an *enumerate* object, which can be transformed back to a list of numbered tuples (see below for more on the tuple data type) or whose elements (both the list element and the counter) can be employed in *for* loops (see below)
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


# - ***zip(list1,...listn)*** allows us to iterate over multiple lists at once. Just as for *enumerate*, the result of that function is a *zip* object, which can be transformed back to a list of paired tuples or whose elements can be iterated over in *for* loops (see below). 

# In[14]:


list_of_birds = ["robin","duck","penguin","pidgeon"]

list_of_animals = list(zip(list_of_mammals,list_of_birds))
print(list_of_animals)


# In[15]:


for mammal , bird in zip(list_of_mammals ,list_of_birds):
    print("a " + mammal +" is a mammal, a "+ bird + " is a bird")


# - ***map(function, list)*** applies a function (in its first argument) to all elements of a sequence (in its second argument). The function returns a *map* object, which can be assigned back to a list or tuple.

# In[16]:


word_lengths = list(map(len , list_of_mammals)) #applies the function len to each element on the list and returns the length of the animal names in a new list
word_lengths


# ### <span style="color:red">End of lecture 4 (November 22, 2022).</span>
# 
# 
# ### Tuples
# Tuples are the little cousins of lists. They are best explained by how the two differ:
# 
# - tuples are typed with parentheses () instead of square brackets []
# - tuples are immutable, that is, their values cannot be modified, appended, or removed without creating a new variable. For that reason, you can **use them for sequences of values that are meant to stay fixed**. 
# 
# Tuples have many uses, such as returning multiple values from a function or assigning objects to multiple variables (see session03). We have also already seen that **tuples and lists sometimes interact**, e.g., when using the *zip()* or *enumerate()* functions. Just as for integer and floating-point numbers, **lists can be converted to tuples and the other way around**.

# In[17]:


reptiles = "crocodile", "lizard", "iguana"
print(reptiles)

list_of_reptiles = list(reptiles)
print(list_of_reptiles)


# #### Itertools
# 
# So far, we've used *for* loops to iterate over all elements of an iterable or over multiple iterables (as with *zip*). Some more complex iterators are predefined in the *itertools* module, which you can use after importing it to Python (more on modules in the next session).  
# 
# **Itertools provides a range of predefined iterators to make your life easier**, see here: https://docs.python.org/3/library/itertools.html .
# 
# For instance, *product(iterable1,....iterable n)* returns the Cartesian product of its arguments, which is equivalent to building a nested *for* loop.  
# 
# Have a look at the documentation linked above for further helpful functions (**this may or may not be relevant to homeworks in the future...**).

# In[18]:


import itertools

for entry in itertools.product(list_of_mammals,list_of_birds): #for each of the cartesian products
    print(entry) #print the tuple

print("\nThis is equivalent to:\n")

for entry1 in list_of_mammals:
    for entry2 in list_of_birds:
        entry = entry1, entry2 #create tuple of animals
        print(entry) #print


# ### Sets
# A final basic data type for collections of elements is the *set*. Unlike list and tuples, sets are **unordered** and **every element can only occur once**. Sets begin and end with curly brackets {}.

# In[19]:


lays_eggs = {"platypus","crocodile","iguana","lizard"}
produces_milk = {"dog","platypus","horse","chimpanzee","whale"}


# **Set methods**:
# 
# | Method |Operation |Example | Evaluates to|
# |---|---|---|---|
# | *in* / *not in* | tests for set membership | "platypus" in lays_eggs | True|
# | *add(obj)* | adds a single element to the set| produces_milk.add("goat")| produces_milk == {"dog","platypus","horse","chimpanzee","whale","goat"}
# |*update(obj)* | adds multiple elements to the set|lays_eggs.update(("robin","penguin"))| lays_eggs == {"platypus","crocodile","iguana","lizard","robin","penguin"}|
# |*remove(obj)*| deletes an element from the set| lays_eggs.remove("penguin") | lays_eggs == {"platypus","crocodile","iguana","lizard","robin"} |
# |*discard(obj)*| works like *remove()*, but does not throw exception if the object wasn't part of the set in the first place|lays_eggs.remove("dodo") | lays_eggs == {"platypus","crocodile","iguana","lizard","robin"} |
# |*len(set)*| returns the number of elements in the set| len(produces_milk) | 6 |

# You can perform also perform a variety of **set operations** known from logics: 
# 
# - The **intersection** of two sets is written as *A & B*
# - The **union** of two sets if written as *A | B*
# - The **difference** between two sets if written as *A - B*
# 
# See your logics classes for further set operations...

# In[20]:


print(lays_eggs & produces_milk)


# ### Dictionaries
# 
# Dictionaries in Python function much like dictionaries in real life: they are used to organize data by key terms (capitals of countries, regions of Germany, English-German translations, ...) . Like lists, **dictionaries are mutable collections of many values**. Unlike lists, which are organized by their numerical index, however, **dictionaries can be organized (or indexed) by many different data types**. We call these indices *keys* and the association between a key and its values a *key-value pair*.  
# 
# Dictionaries are...
# 
# - **used for storing objects under keys and looking them up again** (hence the name)
# - a **universal data structure that can be used to represent any mapping**. Any immutable type can be a key (strings, numbers, tuples, but not lists or sets) and any object can be a value (even lists or sets)
# 
# #### Basic features of dictionaries
# 
# Like sets, dictionaries begin and end with curly brackets. Inside, they contain mappings between key and value, indicated as objects on the left-hand and ride-hand side of a colon, respectively.

# In[21]:


some_capital_cities_of_africa = {"Algeria" : "Algiers",
                                 "Botswana": "Gaborone",
                                 "Chad" : "N'Djamena",
                                 "Egypt" : "Cairo",
                                "Kenya" : "Abc"}
print("The capital of Egypt is ",
      some_capital_cities_of_africa["Egypt"]) #retrieve dictionary entries by their key

#adding new dictionary entries is easy....
some_capital_cities_of_africa["Kenya"] = "Nairobi"


# #### Dictionary construction
# 
# There are many more elegant ways of dictionary construction than hand-typing out all key-value pairs as in the example above.
# 
# - Using **list comprehension** to create a list of pairs:

# In[22]:


to_upper_dict = dict([(l.lower(),l) for l in 
                      "ABCDEFGHIJKLMNOPQRSTUVWXYZ "])
print(to_upper_dict)


# - Using two zipped sequences:

# In[23]:


lower = ["a","b","c","d","e","f","g","h"]
upper = ["A","B","C","D","E","F","G","H"]

to_lower_dict = dict(zip(upper,lower))
print(to_lower_dict)


# Remember that dictionaries can contain *any* object as values, even lists. Thus, they can be used to store large amounts of data at once.
# 
# Let's imagine you want to keep score of important information about your friends. A dictionary easily allows you to represent the relevant information:

# In[24]:


first_names = ["Mohamed", "Alina", "Tracy", "Sophia"]
last_names = ["bin Hamad", "Schultz", "Sanchez", "Loren"]
ages = [33, 28, 41, 38]
phone_numbers = ["0176123456", "0176123456", "0176123456", "0176123456"]

notebook = {"First name" : first_names, 
            "Last name" : last_names, 
            "Age" : ages, "Phone number" : phone_numbers}

for i in notebook:
    print("I have the following information: ", 
          i ,":", notebook[i][0]) #for each key, returns the list element with index 0


# #### Modifying a dictionary
# 
# - *len()* on a dictionary evaluates to the number of key-value pairs
# - *in* checks for the presence of a key
# - *dict.keys()* returns a list of all keys in the dictionary
# - *dict.values()* returns a list of all values in the dictionary
# - *dict.items()* returns a list of all key-value pairs 
# - *del* deletes a key-value pair, e.g., *del notebook["Phone_number"]*
# - *dict.clear()* empties the dictionary
# 
# #### Processing a dictionary
# 
# Since dictionaries have both keys and values, we can use loops to iterate over either. Using the *values()* and *keys()* methods is essential here:

# In[25]:


#Adding a new friend to our notebook:
key_list = list(notebook.keys())
i = 0

#a loop over dictionary values
for entry in notebook.values(): 
    print("Please add a new", key_list[i])
    new_entry = input()
    entry.append(new_entry)
    i += 1
print(notebook)


# In this particular case, the same result may also be achieved by looping over dictionary keys. Whether you should loop over keys or values will always depend on your application.

# In[26]:


#a loop over dictionary keys
for i in notebook.keys():
    print("Please add a new", i)
    new_entry= input()
    notebook[i].append(new_entry)

print(notebook)


# Note, crucially, that **we can't access dictionary entries by using a numeric index**, as we would for lists. The following command raises a *key error*:

# In[27]:


print(notebook[1])


# This is because **although it looks like a numeric index, it is not**. As specified earlier, any immutable type can be a dictionary key, including integer numbers. Therefore, *notebook[1]* is understood as command to look up the values paired with the key *1* (and we never defined such a key in this dictionary).
# 
# **Dictionaries are not inherently ordered, therefore accessing its items always relies on referring to their keys and/or values.** Although Python does guarantee that the order of items in a dictionary is preserved when displayed or iterated over, this is only the case since very recently. It has been added as a part of the Python language specification in version 3.7 (released in 2018).

# ### Hierarchical structure
# 
# Remember that all data types that encode collections of elements (lists, tuples, sets, dictionaries) can be nested! A more elegant way of representing our little notebook of friends uses **nested dictionaries**:

# In[28]:


revised_notebook = dict()

for i in range(1,len(first_names)):
    revised_notebook["Friend "+ str(i)] = {"First name" : first_names[i-1], 
     "Last name" : last_names[i-1], 
     "Age" : ages[i-1], 
     "Phone number" : phone_numbers[i-1]}

print("\n",revised_notebook["Friend 1"])


# Similarly, lists can be nested into arbitrarily complex hierarchical list structures. **It is very common to represent matrices as nested lists**, for instance: 

# In[34]:


#initializing a matrix with m rows and n columns:
matrix = [[1,2,3,4], [5,6,7,8]]

#modifying the values in row 1 and 2, columns 3 and 4 respectively:
matrix[0][2] = 0.3; matrix[1][3] = 0.1
print(matrix)

#summing up the rows
print("The sum of the rows is:",list(map(sum , matrix)))

#Question: How would you sum up the columns?
print("The sum of the columns is:", list(map(sum,zip(matrix[0],matrix[1]))) )


# In[ ]:




