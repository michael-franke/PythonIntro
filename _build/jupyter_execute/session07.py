#!/usr/bin/env python
# coding: utf-8

# ## For efficiency's sake: structured programs, packages, regular expressions  (December 20, 2022) 
# 
# Efficiency is key. Therefore, in this session, you will learn more about advanced aspects of efficient programming. We have already discussed how to improve code efficiency and maintainability in small programs. Sooner or later, however, additional questions may emerge: How should you **distribute code over a main program and importable modules**? Where can time and effort be saved by **relying on already available modules and **packages**? Can **repeating patterns** in the task at hand be detected and exploited for further automization? 
# 

# ### Structured programs
# Python code (in .py files) can be used in two ways:
# - as a standalone program (e.g., the code file that you run from within Spyder)
# - as a module that is imported and used from inside another program
# 
# **Recap**: Any .py file can be loaded as a module. As such, modules allow us (a) to distribute code across multiple files (which is convenient for bigger coding projects). Modules are loaded with an *import* statement. 
# 
# **Larger projects should make use of the distinction between standalone programs and modules.**
# - package the main functionality in different Python files
# - import these files as modules from a main file where the execution code resides
# - this main code should only be executed when the code is run as a standalone program
# 
# #### Introducing the *main* block
# 
# Upon importing a module, **all statements in the imported module are executed**. This may be fine if the module is explicitly design with a singular intended function as module imported to other programs. But **sometimes you may want to be able to use a script as both a module and an executable standalone program in and of itself**. This is where the *main* block comes in handy.
# 
# Why would you want this functionality?
# - Your code's **main function may be for use as module**, but you still want to include a script mode where it runs some **unit tests or a demo**.
# - Your code's **main function may be for use as standalone program**, but you still want to **make some of its functionalities available to other programs**, without needing to create a new .py file.
# - Finally, your code may be for **use as standalone program (by you)**, but may have some unit tests and the **testing framework (by your teachers)** works by importing .py files like your script and running special test functions. This is the case for your homework exercises.

# In[1]:


#Example from homework exercise 01
def pig_latin_name(name):
    """
    Transform a name to the Pig Latin variant (paying attention to capital letters).
    """
    pass


# paste your test code here (will not be tested)
if __name__ == '__main__':
    pass


# In your homework exercises, **you can test your own code in the main block of your script**. This part of the code is **only exectued when the file runs as standalone program**. If it is instead imported as module (e.g., to our testing scripts), execution of the module's main block is skipped. 

# **But how does this work, exactly?**
# 
# Upon initializing a script, the Python interpreter will...
# 1. read the source files and **assign certain special variable names**
# 2. execute all code
# 
# Special variables are preceded and followed by \_\_ . Here, we care in particular about the **\_\_name\__** variable. 
# 
# If you are **running a source file as the main program**, the interpreter will assign the hard-coded string "\_\_main\_\_" to the \_\_name\_\_ variable. It's as if the interpreter inserts this at the top of your code (you don't actually have to add this to your code):
# 
#     __name__ = "__main__" 
#     
# If you want to convince yourself of this, try and print out the variable's value on your next homework exercise:

# In[2]:


print (__name__)


# If you are **importing a source file as module to another program**, the interpreter will search for the respective .py file and will assign the name from the import statement as value of its \_\_name\_\_ variable.
# 
# For instance, if we are importing the module *math*, it's as if the interpreter inserts this at the top of the *math.py* file:
# 
#     __name__ = "math"
#     
# Note that the name of your main program remains \_\_main\_\_:

# In[3]:


import math
print("the live script's name remains: ",__name__)
print("the imported module's name is:",math.__name__)


# Coming back to the question as to **how this is useful**, note that we can **conditionalize the execution of certain statements on whether the file is executed as main file or as module**. Code that is embedded under the *if* statement will only be executed if the \_\_name\_\_ variable is assigned the "\_\_main\_\_" value at runtime:

# In[4]:


if __name__ == '__main__':
    print("This is now running as standalone program!")
    
if __name__ == '__math__':
    print("We never get here from the main program.")


# #### Using the main block to separate functionality from function
# 
# It is efficient, and good practice, in programming to **separate code functionality (the function definitions) from code function (the executable program code)**. You are already using this pattern in your homeworks!
# 
# The following program provides an **example of well-packaged code** that could readily be imported as module to other programs, which would provide them with the specified functions' functionalities:

# In[5]:


def sum_lists(list1 , list2):    #functionalities are defined for generalized usability and can be imported into other files
    return sum(list1) + sum(list2)

def read_floats_from_file(filename):
    with open(filename , "r") as in_file:
         lines = in_file.readlines ()
    float_list = []
    for line in lines:
        float_list.append(float(line.strip ()))
    return float_list

if __name__ == "__main__": #input is read in only here, that is, when executing the source file as standalone program.
    l1 = read_floats_from_file("test.txt")
    l2 = read_floats_from_file("test2.txt")
    print("Sum of both lists: " + str(sum_lists(l1 ,l2)))


# ### Packages
# 
# Some functionality is needed by many different programs, but isn't part of the core language (like built in string methods) or the built-in modules/libraries (like *math* or *itertools*).
# 
# **Linguistic examples:**
# - visualization of objects likes trees and graphs
# - efficient natural language parsing
# - multilingual text processing and conversion between alphabets
# 
# You don't need to reinvent the wheel. Focus on the novel functionality of your program while relying on stable code used (and tested) by other programmers for common tasks.
# 
# **Python packages** are shared by programmers via package management systems, from which they can be installed via automated tools.
# 
# #### How to find and install a package:
# 
# - Google for packages that might provide the functionality you want.
# - If you are using the configuration that was recommended at the outset of this course, try installing it via *conda* first:
# 
#         conda install the-package   (the-package is our dummy name, replace it by the package's real name)
# - If it says *package not found*, access the Python Package Index (PyPI) via pip:
#                         
#        pip install the-package
#       
# - For the latter option, you might need to install pip first:
# 
#         conda install pip
#         
# #### How to use an installed package:
# 
# **Installed packages are available as importable modules.** Take a look at the examples on the package’s website to figure out what modules can be imported. Try out some of the code provided on the package's website to test that everything works as expected.
# 
# Not sure about what one of the functions or variables in the module’s namespace does? **Many packages provide good documentation online!**
# 
# ##### Many packages define their own classes (data types):
# - Class names are conventionally written with an uppercase letter (example: Text)
# - Classes are similar to the built-in complex datatypes like lists and dictionaries: they define the behavior of objects of their type (e.g., what properties should Text objects have)
# - creating an instance of a class (an object of its type) works by calling its constructor, like you used dict() to create a new dictionary:
# 
#         my_text = Text(str)
# 
# - Classes provide methods, i.e. functions which take an instance of the class as their first argument, and calls to which are written instance.method(additional arguments)
# 
#         my_text.words
#         
# - You will learn how to create your own classes in a later session.
# 
# #### Example: The *polyglot* package
# 
# The *polyglot* package is a natural language processing toolbox specialized on multilingual language applications. It offers tools for tokenization, language detection, morphological analysis and more in 150+ languages.

# In[7]:


import polyglot #import the polyglot package
from polyglot.text import Detector, Text, Word #imports the Text and Word classes

text_en = Text("Enjoy the Christmas break and have a happy new year!")
text_ar = Text("عيد ميلاد مجيد وكل عام وانتم بخير")
print(text_en.words)
print("\nLanguage Detected: Name={}".format(text_en.language.name))
print("\nLanguage Detected: Name={}".format(text_ar.language.name))


# In[5]:


from polyglot.transliteration import Transliterator

#english-arabic transliteration
for x in text_en.transliterate("ar"):
  print(x)


# ### Pattern detection via regular expressions
# 
# In many applications, we need to **find strings matching a pattern**:
# - find all documents containing a given name
# - find example sentences for the usage of some word in a corpus
# - find the places in your code where you used some variable
# 
# Also, we often need to **extract parts of a string matching a pattern**:
# - extract everything that is formatted like a name
# - extract the words which can occur as arguments to a specific verb from a corpus
# 
# **Regular expressions** are sequences of strings and special operators that define a regular language (in the Chomskian sense). They allow you to specify search patterns for text data.
# 
# #### Regular expressions as regular language
# 
# Regular languages, in general, are characterized as follows: 
# 
# **Given a finite alphabet Σ** (e.g., a collection of characters),...
# 
# - the **empty language Ø** is a regular language.
# - for each a ∈ Σ, the **singleton language {a}** is a regular language.
# - If A is a regular language, **A&ast; (Kleene star, more below)** is a regular language. That means the empty string language {ε} is also regular.
# - If A and B are regular languages, then **A ∪ B (union)** and **A • B (concatenation)** are regular languages.
# - **No other languages over Σ are regular.**
# - In particular, that means that A<sup>n</sup>B<sup>n</sup> does not describe a regular language (because there is no memory for the value of *n*)
# 
# All regular languages are describable by regular expressions. Let's assume a language with alphabet Σ = {a, b, c}. Regular expressions over this alphabet can use any of its constants (characters) as well as the three basic operations admittable by the definition of regular languages:
# 
# - **Concatenation**: in linear order, combine two elements of the alphabet: *ab, aab, aaabb, aacbbb, ...* 
# - **Alternation**: free choice of either the (potentially multi-character) expressions on the left or right of the pipe symbol: *a|b, (ab)|(bc), (accc)|b,...*
# - **Kleene star**: denotes the smallest superset of the set described by the expression it is applied to that contains ε and is closed under string concatenation: *a&ast; = {ε, a, aa, aaa, aaaa,...}*, *(ab)&ast; = {ε, ab, abab, ababab,...}*
# 
# #### Finite state automata
# 
# Regular languages (and thus regular expressions) can also be represented visually in (deterministic or nondeterministic) *finite state automata* (FSA). These consist of:
# 
# - a finite number of states Z = {Z<sub>1</sub>, Z<sub>2</sub>, ..., Z<sub>k</sub>}
# - a starting state Z<sub>start</sub> ∈ Z
# - one (or possibly several) final states Z<sub>end</sub> ⊆ Z
# - a transition function to move from Z<sub>i</sub> to Z<sub>j</sub> depending on an input symbol from the alphabet Σ. δ : Z × Σ → Z 
# 
# Determinisitic FSA need to specify exactly one possible transition per input symbol on each state. Nondeterministic FSA can have multiple transition options for an input symbol (e.g., for a on Z<sub>1</sub> below).
# 
# <img src="https://www.dropbox.com/s/sbye5rzzqoxa0lw/automata_regex.png?raw=1" width="500" height="500" />
# 
# 
# 

# #### So what's the use of this again?
# 
# Using just the set of operations defined above, we can significantly improve pattern detection for various types of text input.
# 
# **Regular expressions can be used in Google**: "(parties|concerts) in Tübingen on (Friday|Saturday)".
# 
# #### The *re* module
# Using the **Python module *re***, we can find and extract text patterns by matching them against specified regular expressions. Note that the package's syntax is a bit differnt from the notation introduced above and introduces a few extra operators:
# 
# |Operator|Meaning|Example|
# |---|---|---|
# | &ast; | zero or more repetitions | *b&ast;t* matches *t, bt, bbt, ...* |
# | + | at least one repetition | *b+t* matches *bt, bbt, ...*|
# | ? | optional items (zero or one repetition) | *b?t* matches *t* and *bt*|
# | [] | alternation between single characters | *b[aeiou]t* matches *bat, bet, bit, bot, but*, but not *beet*|
# | [^...] | the hat symbol inside square brackets serves to negate the characters therein | *b[^aeiou]t* matches bbt, bct, ...*, but not *bat, bet, bit, bot, but*|
# | {min, max} | more general quantification | *a{4,6}* matches *aaaa, aaaaa*, and *aaaaaa*|
# | . (dot) | wildcard symbol that matches any character except the new-line character | *b.t* matches *bat, bbt, bct, bdt, bet,...*|
# | () | grouping metacharacter as above | *(ab)+* matches *ab, abab, ababab,...*|
# | \| | alternation as above | *apple\|banana* matches *apple, banana*|
# 
# Further useful shorthand notations:
# 
# - [A-Z] matches any uppercase letter of the alphabet
# - [0-9] matches any digit
# - \d stands for digits (= [0-9])
# - \w stands for word characters (= [a-z A-Z 0-9])
# - \s stands for whitespaces (= [\t\r\n])
# 
# **Re** requires you to specify an expression against which to match the designated string. You can set this using *re.compile(regex)*. **Simple pattern matching operations on that basis include**:
# 
# - *regex.match(str)*: matches the regex pattern **for its appearance at the beginning of the string**.
# - *regex.search(str)*: matches the regex pattern **for its appearance anywhere in the string**. Only returns the first match.
# - *regex.findall(str)*: matches the regex pattern **for its appearance anywhere in the string** and returns all matches.
# - *regex.split(str)*: matches the regex pattern **for its appearance anywhere in the string** and splits the string into a list of substrings.

# In[1]:


import re

sentence = "The quick brown fox jumps over the lazy dog."

matcher = re.compile("(\s[d|f]o[^aeiou])")

print(matcher.findall(sentence)) #find all instances matching the regex
print(matcher.split(sentence)) #split string around all instances matching the regex


# The first two of these methods return a *match* object, which can be further processed using methods within the *Re* module (e.g., *start()* and *end()*, but check out the online documentation for more).

# In[10]:


match = matcher.search(sentence)
print(match)

match.start(), match.end()


# You can replace matching substrings using the *sub(replacement, string)*:

# In[12]:


matcher.sub(" cat", sentence)

