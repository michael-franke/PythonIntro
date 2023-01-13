#!/usr/bin/env python
# coding: utf-8

# ## Classes (January 17, 2023) 
# 
# 
# In previous sessions, we learned about various different data types (e.g., integers, strings, lists, tuples, dictionaries...) along with their methods (e.g., *str.split()*, *list.sort()*,...), **but what if we could define our own?**
# 
# With **classes**, you can write user-defined data types. This is a form of what's called **object-oriented programming**. Instead of writing procedures / algorithms to solve a task, we are now writing code to define objects (of course these may subsequently be used in *procedural programming tasks*). 
# 
# ### The basics
# 
# - **A class specifies** the **format** of instances of that class (in terms of data structure) and what **procedures** are available for them (in terms of user-defined methods). 
# - Instances of a class are called objects (just like there are integer objects, list objects, etc.)
# 
# **You may think of the definition of a class as the definition of a concept**. As in real life, **concepts/classes are defined by their essential properties, specified in terms of more basis concepts**: 
# 
# - e.g., a *rectangle* may be defined as a quadrilateral with right angles, *angles* may be defined as the figure formed by two rays sharing a common endpoint, *rays* may be defined as [...], and so forth). 
# - **In Python**, that means that you can **use any of the in-built basic data types to define objects of your own class**, or may even define several classes (e.g., Rectangle and Angle), one of which inherits properties of the other (e.g. Rectangle inheriting properties of the Angle class).
# 
# **Methods of a class can be thought of as definitions of the way in which instances of that concept / class interact with the world**:
# - e.g., a rectangle can be enlarged or shrunk by adding / removing the same amount of length to its opposing sides, two rectangles may be conjoined if they align on one of their dimensions, etc.
# - **In Python, methods of a class are specified in terms of functions that take an instance of that class as argument**.

# ### Defining a class in Python
# 
# - Class names start with a capital letter.
# - Classes usually start with an \_\_init\_\_ constructor (more on this below).
# - The *self* parameter is automatically set to refer to an object of the data type you are defining. In the code below, it is a variable refering to an instance of *YourClass* and functions like any other variable inside the class definition.

# In[1]:


class YourClass:
    def __init__(self):
        self.variable1 = 1
        self.variable2 = 2
           
    def method1(self):
        #some method
        pass
           
    def method2(self):
        #some other method
        pass


# #### The initialization method
# 
# The *\_\_init\_\_(self)* method (also called the *class constructor*) is automatically called whenever you create an instance of the class. **In it, you should specify the basic properties of all instances of that class.** For instance, in the code above, it initializes all objects of the *YourClass* class as having two properties, *variable1* and *variable2*, which have the values *1* and *2*, respectively. 

# In[2]:


example = YourClass() #create an instance of the YourClass class  
print(example) #printing an object of that class just prints information about the type of object it is


# In[3]:


print(example.variable1) #after initialization, this object has the properties we specified above
print(example.variable2)


# We may not always want to initialize objects with the same values for *variable1* and *variable2*, though. **To make the initialization method more general, we can add extra parameters in its definition**, as in the following example. The way this works is that it sets *value1* and *value2* to *1* and *2*, respectively, as long as no other values are provided in your call to create an instance of that class.

# In[4]:


class YourClass:
    def __init__(self, value1 = 1, value2 = 2):
        self.variable1 = value1
        self.variable2 = value2
           
    def method1(self):
        #some method
        pass
           
    def method2(self):
        #some other method
        pass


# We can still create objects like before:

# In[5]:


example2 = YourClass()
print(example2.variable1)


# But we can also specify their values for *value1* and / or *value2*:

# In[6]:


example3 = YourClass(2,3)
print(example3.variable1)


# In[7]:


example4 = YourClass(value2=3)
print(example4.variable2)


# Note that if you do not provide default values as in *def \_\_init\_\_(self, value1 = 1, value2 = 2)*, you will always have to provide such values upon creating an object of that class.

# ### A simple Language class
# 
# The following is **not a complete representation of specific language families**. It only serves for illustration:

# In[8]:


class Language:
    #if no information about family, branch, or number of speakers is provided by the user, set to unknown
    def __init__(self, name, family="unknown", branch="unknown", num_of_speakers="unknown"): #initializes the language class
        self.name = name
        self.family = family
        self.branch = branch
        self.num_of_speakers = num_of_speakers

    #function to infer language family from language branch
    def branch_to_family(self):
        if self.family == "unknown" and self.branch != "unknown":
            if self.branch == ("Balto-Slavic" or "Germanic" or "Hellenic" or "Indo-Iranian" or "Romance"):
                self.family = "Indo-European"
            elif self.branch == ("Sinitic" or "Tibeto-Burman"):
                self.family = "Sino-Tibetan"
            


# In[9]:


de = Language("German", "Indo-European", "Germanic", 100000000)
lat = Language("Latvian", branch = "Balto-Slavic",num_of_speakers = 2200000)

ra_ha = Language("Ramarih Hatohobei", "Austronesian", "Micronesian")

print(de) #de is now a Language object


# #### Calling class methods
# 
# We can call on a class method just as we called methods for other data types before (e.g., *str.split()*):

# In[10]:


lat.branch_to_family()
print(lat.family) #family information has now been added


# #### Using class objects as arguments or parameters
# We can use instances of our class as arguments or parameters in functions. For instance, we could write a function that outputs all information about a particular language:

# In[11]:


def print_language_info(lang):
    print(lang.name, "is an instance of a", lang.branch, "language in the", lang.family, "language family. It has", lang.num_of_speakers, "native speakers")
    
print_language_info(de)


# **Importantly, for general-purpose functions like this, it is preferred to add them as new methods of the class, rather than as functions operating outside of the class**. One of the reasons for that is that your code stays more portable and comprehensible if all important functions / methods are contained within the class definition. 
# 
# So let's add a print method to our class. **Crucially, if we call it *\_\_str\_\_(self)*, it will function as the default output of the *print()* function called on objects of that class!**

# In[12]:


class Language:
    def __init__(self, name, family="unknown", branch="unknown", num_of_speakers="unknown"):
        self.name = name
        self.family = family
        self.branch = branch
        self.num_of_speakers = num_of_speakers

    def branch_to_family(self):
        if self.family == "unknown" and self.branch != "unknown":
            if self.branch == ("Balto-Slavic" or "Germanic" or "Hellenic" or "Indo-Iranian" or "Romance"):
                self.family = "Indo-European"
            elif self.branch == ("Sinitic" or "Tibeto-Burman"):
                self.family = "Sino-Tibetan"
    
    def __str__(self):
        return ("{0} is an instance of a {1} language in the {2} language family. It has {3} native speakers.".format(self.name, self.branch, self.family, self.num_of_speakers))
    


# In[13]:


#create the objects again with the new Class definition:
de = Language("German", "Indo-European", "Germanic", 100000000)
lat = Language("Latvian", branch = "Balto-Slavic",num_of_speakers = 2200000)

ra_ha = Language("Ramarih Hatohobei", "Austronesian", "Micronesian")

print(de)


# #### Using several instances of a class
# 
# We can also **define methods that operate on several instances of the class we are in**. For example, we could specify a class method that checks whether two languages are part of the same language family. This method takes *self* and another Language object as arguments.
# 
# Note also that **we can call other class methods from within a class method** (here, we call *branch_to_family*), just like we saw nested function calls in previous sessions.

# In[14]:


class Language:
    def __init__(self, name, family="unknown", branch="unknown", num_of_speakers="unknown"):
        self.name = name
        self.family = family
        self.branch = branch
        self.num_of_speakers = num_of_speakers

    def branch_to_family(self):
        if self.family == "unknown" and self.branch != "unknown":
            if self.branch == ("Balto-Slavic" or "Germanic" or "Hellenic" or "Indo-Iranian" or "Romance"):
                self.family = "Indo-European"
            elif self.branch == ("Sinitic" or "Tibeto-Burman"):
                self.family = "Sino-Tibetan"
    
    def family_check(self, comparison):
        if self.family == "unknown":
            self.branch_to_family()
        if comparison.family == "unknown":
            comparison.branch_to_family()
        if self.family == "unknown" or comparison.family == "unknown":
            print("At least one of the languages does not have a known language family.")
        elif self.family == comparison.family:
            print("Same language family.")
        else:
            print("Not the same language family.")
    
    def __str__(self):
        return ("{0} is an instance of a {1} language in the {2} language family. It has {3} native speakers.".format(self.name, self.branch, self.family, self.num_of_speakers))
    


# In[15]:


#create the objects again with the new Class definition:
de = Language("German", "Indo-European", "Germanic", 100000000)
lat = Language("Latvian", branch = "Balto-Slavic",num_of_speakers = 2200000)

ra_ha = Language("Ramarih Hatohobei", "Austronesian", "Micronesian")

de.family_check(lat)
ra_ha.family_check(de)


# ### Class inheritance
# We can declare classes as subtypes of another class. For instance, below, we define a class *IndoEuropean* as a subtype of the *Language* class.
# 
# **All functionalities of the superclass (class variables, methods) are inherited by the subclass**, but can be overridden by redefinition or reassignment.

# In[16]:


class IndoEuropean(Language):
    pass

en = IndoEuropean("English")
print(en.family)


# Below, we redefine the initialization method for the *IndoEuropean* class. Note that all other methods from the *Language* class will still be available in the *IndoEuropean* subclass.

# In[17]:


class IndoEuropean(Language):
    def __init__(self, name, branch="unknown", num_of_speakers="unknown"):
        self.name = name
        self.family = "Indo-European"
        self.branch = branch
        self.num_of_speakers = num_of_speakers
        
en = IndoEuropean("English")
print(en.family)


# ### Objects are mutable
# 
# You know *mutability* from list objects. It means that we can we can directly add, remove, or change the values of the object without creating a new object. **Note that Class objects are mutable!** Specifically, we can change any of the instantiated object's values, delete properties of the object, or delete the object altogether:

# In[18]:


#change value of num_of_speakers
en.num_of_speakers = 370000000
print(en.num_of_speakers)


# In[19]:


#delete num_of_speakers property
del en.num_of_speakers
print(en.num_of_speakers) #results in error


# In[20]:


#delete object
del en

#to remind you of the try block...
try:
    print(en)
except NameError:
    print("The object no longer exists.")

