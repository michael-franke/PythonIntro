#!/usr/bin/env python
# coding: utf-8

# ## Modules, file I/O (input/output) (December 06, 2022)
# 
# **So far, all of our Python programs were self-contained**, that is, they did not rely on external data files or pieces of code (except for in-built Python functions and methods). In most real-life situations, however, you will work off of existing files (e.g., for data analysis) or from pre-existing code (e.g., when adding new functionalities to an app or program). In this session, you will learn how to **import and use** external Python code as **modules** and how to **create, read from, and write to files**.
# 
# ### Modules
# 
# **Modules are Python files intended for use in other Python programs**. Any *.py* file can be loaded as a module. As such, modules allow us **(a) to distribute code across multiple files** (which is convenient for bigger coding projects) and **(b) to make use of collections of useful functions** provided by other programmers. Many modules come with Python as part of the default installation. One such example is the *Itertools* module we saw in the previous session. Others include the *math* module and the *random* module, which contain helpful functions for mathematical operations and for dealing with distributional data.
# 
# Modules are **loaded with an *import* statement** (more below). Upon importing them, **all statements in the imported module are executed**.  
# 
# In the following, we will focus on the *math* module:
# 
# #### Import modules
# 
# Modules can be imported in three ways:
# 
# - *import math*: makes all objects available as *math.object*
# - *from math import func*: makes *math.func* available as *func*
# - *from math import long_function_name as func*: makes *math.function_name_in_module* available as *func_name_in_my_code*

# In[1]:


from math import factorial  #imports the function factorial(x) from the math module, assigns it the name fc

print(factorial(4)) #prints 4!


# The names and functionalities of available modules can be looked up in Python's documentation: https://docs.python.org/3/py-modindex.html

# #### Example: Your homework as module
# 
# Our testing skripts import your homework as module. Your code gets loaded by *from ex_01 import \**. The star symbol indicates that the module should be imported with all functions and classes as elements in the current file's namespace(, even if that would replace existing names). Thus, your function definitions are assigned to the function names, and the unit tests will be executed on your definitions.  
# 
# The most basic element of our test code is the *assert* statement. Each such statement represents a basic fact which should hold of the program. For instance, *assertEquals(value, expression)* checks whether an expression correctly evaluates to a given value.   
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
# Now that you know how to use **modules**, we'd also like to know how to use **files**. Creating data by assigning values to variables worked fine so far, but more often than not data already exists and we want to work with it. Python allows you to **read in data** from external files such that you can **extract, analyse or modify** its contents and **save the results** to (another) file.  
# 
# **Files have two key properties**: 
# - a filename (including name + file type, e.g. *example.txt*) 
# - a path, which specifies its location on the computer (e.g. *C:\Users\jschwab\Documents\Teaching\Methods I\*)
# 
# #### Reading and writing to text files
# Plaintext files (*.txt*) contain only basic text characters and do not include font, size, or color information. They consist of lines of text with a newline symbol at the end of each line (in Python strings, a newline is represented by "\n"). Text files are one of the most elementary file types that we will deal with. Python can easily read them, treating their contents as string values. 
# 
# ##### Basic elements of file input:
# - The function *open()* creates and returns a file handle
# 
#     - obligatory argument: a file name (or a complete path)
#     - optional: a string representing the **mode** in which the file is opened
#     - optional: a string representing the **encoding** of the file (see below)
# - Example: *open("guide.txt", "r")*
# 
# 
# - The default mode if no other is specified: **"r" (“reading”** -- opens a file for reading only).   
#     Other options:   
#     **"w" ("writing"** -- opens a file for writing only. If the file does not exist, creates a new file for writing).   
#     **"a" ("appending"** -- opens a file for appending. New content is appended to the end of the file. If the file does not exist, creates a new file for writing).  
#     **"x" ("creating"** -- creates a file and opens it. Fails if a file by that name already exists).
# - Additional specifiers to the mode: **"+"** (*r+ = read and write, w+ = write and read, a+ = append and read*), **"b"** (*rb/wb/ab = read/write/append in binary format*)
# 
# 
# **A file handle in reading mode has a few core functionalities:**
# 
# - *file.read()* returns the whole document in a single string
# - *file.readline()* returns the next unprocessed line of the file
# - *file.readlines()* returns a list of strings, containing each line of the file as a string in the original order
# - *file.close()* cancels or finishes the processing of the file, ensuring that the file is closed correctly

# Let's presume we have a text file (*guide.txt*) that contains the following content:
# 
# > DOUGLAS ADAMS: The Hitchhiker's Guide to the Galaxy   
# > Preface 
# >
# > Far out in the uncharted backwaters of the unfashionable end of 
# the western spiral arm of the Galaxy lies a small unregarded yellow 
# sun. 
# >
# > Orbiting this at a distance of roughly ninety-two million miles is an 
# utterly insignificant little blue green planet whose ape-descended life 
# forms are so amazingly primitive that they still think digital watches 
# are a pretty neat idea. 
# >
# > This planet has - or rather had - a problem, which was this: most 
# of the people on it were unhappy for pretty much of the time. Many 
# solutions were suggested for this problem, but most of these were 
# largely concerned with the movements of small green pieces of paper, 
# which is odd because on the whole it wasn't the small green pieces of 
# paper that were unhappy. 
# 
# 
#     fr = open("guide.txt", "r")
#     title = fr.readline () #assigns the contents of the first line to a variable called title
#     chapter = fr.readline() #assigns the contents of the next line to a variable called chapter
#     contents = fr.read() #stores the full file contents in a variable called contents
#     fr.close () #closes the file

# ##### Basic elements of file output:
# 
# - To create or overwrite a file and write new contents into it, use *open(file_name,"w")*.
# - *file.write()* writes a string to the file, and returns the number of characters written
# - *file.writelines()* takes a list of strings, and writes each of them into a new line of the file
# - *file.flush()* forces the buffer to be flushed 
#     - Note that file contents are not changed immediately. The operating system buffers changes in order to make file operations more efficient.
#     - To force that the buffer is cleared, use *flush()*. The buffer is also cleared upon using *close()* or when closing a Python session. 
#     - This method can be useful if you want to ensure that file contents are securely saved in case the program might crash.
# - *file.close()* finishes the creation of the file, and ensures that the file is closed correctly
# 
# Note that the *write* (**"w"**) and *append* (**"a"**) modes functions very similarly, except that the latter allows you to add new contents to the end of an existing file, whereas the former will overwrite all previous file contents.

# Let's presume we want to write a new file called *"example.txt"*.
# 
#     fp = open("example.txt", "w")
#     while True:
#         text = input("Enter a line to write to the file , or press ENTER to quit!") #accepts new text input
#         if text == "": #until the user enters nothing (just presses ENTER)
#              break 
#         fp.write(text) #writes the new input to the file
#     fp.close () #closes the file

# #### FIle encodings
# As mentioned above, you can read and write files in various encodings. Technically, an encoding specifies the **mapping between characters and the bit sequences that they are encoded as**. Every text files encodes characters according to some encoding, the most relevant ones (for now) being **ASCII** (7-bit, English alphabet only), **ISO 8859** (8-bit, variable encodings depending on region/language, alphabetical writing systems only), and **UTF-8** unicode (variable length of 1-4 bytes (fyi, 1 byte = 1 8-bit sequence), all writing systems). The default encoding in Python is **UTF-8**.  
# 
# **Examples:**  
# 
# There's **no difference in the encoding** of characters compatible with the **English alphabet**:  
# - UTF-8 binary encoding of "A" = 01000001  
# - ASCII binary encoding of "A" = 01000001  
# - ISO 8859-1 binary encoding of "A" = 01000001  
# 
# But it **matters for many other languages** (most obviously all languages with writing systems that do not use the Latin alphabet). Even for languages using the Latin alphabet, subtle differences mean that some encodings cannot capture their full character set.  
# 
# 
# The following German sentence can only be encoded in UTF-8: 
# 
# *Frank sagt: &bdquo;Es könnte dieses Jahr weiße Weihnachten geben.&ldquo;* (Frank says: "We might get a white Christmas this year"). 
# 
# The problems for other encodings are:
# - ASCII: No umlauts (*ä,ö,ü*), no *ß*, no German quotation marks (*&bdquo;...&ldquo;*)
# - ISO 8859-1: No German quotation marks (*&bdquo;...&ldquo;*)
# 
# ##### More on different encodings
# 
# **ASCII** (American Standard Code for Information Interchange)
# - first introduced in the **1960s**
# - wide range of control characters
# - limited to lower- and uppercase English alphabet
# - 7-bit encoding with a leading 0 --> 128 characters, all encoded in a single byte (0 0000 000 to 0 1111 111)
# - limited for non-US usage: no umlauts, accents or other diacritics, no currency symbols other than dollar
# - modifications were introduced in various countries, replacing ASCII characters with those of higher local significance, e.g., *ISCII* (Indian scripts), *VSCII* (Vietnamese)
# 
# **ISO 8859** 
# - introduced by ISO (International Organization for Standardization) in **1987** to extend ASCII
# - same encoding as ASCII for all ASCII characters
# - upper range of 128 additional characters for localized symbols
# - different ISO 8859 standards for different regions (e.g. *ISO 8859-1* for Western Europeean languages, *ISO 8859-6* for Arabic, and so on...)  
# 
# **Unicode** (using Unicode Transformation Format (UTF) for binary encoding)
# - first released in **1991** as attempt to provide a **universal encoding for all languages**, contemporary and historic, including relevant non-linguistic symbols (currencies, ...)
# - virtually universal coverage (139 scripts) with a single standard
# - multi-byte encoding with enough room for all current and many future symbols (1 114 111, of which 136 690 are currently used)
# - unicode can be encoded as **UTF-8, UTF-16, or UTF-32**, where each character will be represented as a sequence of one to four 8-bit bytes, one or two 16-bit code units, or a single 32-bit code unit, respectively.
# - UTF-8 is most common on the web. UTF-16 is used by Java and Windows. Both UTF-8 and UTF-32 are used by Linux and various Unix systems. **Conversions between all of them are algorithmically based, fast and lossless.**
# 
# ##### Reading and writing to different encodings
# 
# You can specify the file encoding when reading or writing files in Python. Python internally represents strings in UTF-8, so non-unicode encodings will be converted by Python:
# 
#     ascii_file = open(file_name , encoding="ascii", "r") #reads file in ASCII format
#     latin1_file = open(file_name , encoding="latin-1", "w") #writes file in ISO 8859-1 format

# #### File formats
# 
# Above, we dealt with text files organised as sequences in the form of lines of text (*.txt* files). However, text-based data can be formatted in various ways for information exchange:
# 
# - Tab-Separated Values **(TSV)** or Comma-Separated Values **(CSV)** for **tabular data** (i.e. for datapoints consisting of values for predefined fields -- think of *Excel* spreadsheets, but without colour, size, or font information)
# - Extensible Markup Language **(XML)** for **hierarchically structured data** where format checking is necessary (think of dictionaries, for instance)
# - JavaScript Object Notation **(JSON)** for uncomplicated **data exchange between programs** 
# - various **binary formats** (database files, matrices) for memory-efficient storage and transfer
# 
# ##### CSV and TSV
# 
# - standard table format
# - first line ("header"): field names
# - one entry per line
# - field values are separated by one designated delimiter, common choices:
#     - the tab character (TSV format, ending .tsv)
#     - the comma (CSV format, ending .csv)
# - if the delimiter occurs inside a field value, the value needs to be surrounded by double quotes; tools automatically handle this
# - parsing can be done via *split()*, but more safely via the *csv* module
# 
# **Example table:**  
# 
# |Name|Age|Gender|
# |---|----|----|
# |Saurabh|25|male|
# |Taylor|41|non-binary|
# |Stephanie|30|female|
# 
# **in CSV file format:**
# <center>
# Name,Age,Gender<br>  
# Saurabh,25,male  <br>
# Taylor,41,non-binary <br> 
# Stephanie,30,female 
#     </center>
#     
# **Example usage of csv module:**
# 
#     import csv
#     csvfile = open('eggs.csv', newline='')
#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
#     
# ##### Extensible Markup Language (XML)
# 
# - data is structured by user-defined tags like \<country>
# - textual data is stored in elements: \<tag>text\</tag>
# - elements can have attributes: \<country id="AF">
# - elements can contain other elements (nested structure)
# - XML processing is very complex, do not try this on your own! Use *xml.dom* and *xml.sax* modules for representing and processing XML documents
# 
# **Example of XML document:**
# 
#     \<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
#     \<countryDatabase>
#         \<country id="AF">
#             \<name>Afghanistan</name>
#             \<province id="BDS">
#                 \<name>Badakhshan</name>
#                 \<capital>Fayzabad</capital>
#             \</province>
#             \<province id="BDG">
#                 \<name>Badghis</name>
#                 \<capital>Qala i Naw</capital>
#             \</province>
#             ...
#         \</country>
#     ...
#     \</countryDatabase>
#     
# #### JavaScript Object Notation (JSON):
# 
# - structured data represented using arrays and key-value pairs
# - syntax is mostly identical to Python literals!
# - However, when processing JSON files, some subtle differences between Python and JSON notation mean that not every Python literal can directly be interpreted as JSON, and vice versa (e.g. tuples don't exist in JSON, lists and tuples both correspond to arrays)
# - *json* module can dump any nested data structure to a JSON file, and load any JSON structure from a file
# 
# **Example of a JSON document:**
# 
# 
#     [{"ID": "AF",  
#       "Name": "Afghanistan",
#       "Provinces":
#        [{"ID": "BDS", "Name": "Badakshan", "Capital": "Fayzabad"}, 
#        {"ID": "BDG", "Name": "Badghis", "Capital": "Qala i Naw"},...
#        ]
#      },
#      {"ID": "AL",
#        "Name": "Albania",
#         ...
#      },
#     ...
#     ]
#     
# **Example usage of *json* module:**
# 
#     import json
# 
#     jsonfile = open('filename.json')
#     data = json.load(jsonfile) #read JSON file
#      
#     dictionary = {
#         "ID": "AF",
#         "Name": "Afghanistan",
#         "Provinces": [{"ID": "BDS", "Name": "Badakshan", "Capital": "Fayzabad"}, 
#                      {"ID": "BDG", "Name": "Badghis", "Capital": "Qala i Naw"},...
#                      ]
#         }
#  
#     outfile = open("countries.json", "w")
#     json.dump(dictionary, outfile) #save dictionary to countries.json
#     

# #### Wrapping up lose ends: exception handling
# 
# Python will **throw errors and end code execution** if you try to read or write to files that:
# - do not exist (FileNotFoundError)
# - you do not have the correct permissions for (PermissionError)
# - the storage device does not have enough space for (IOError)
# 
# A more elegant solution for **handling exceptions** is to **pre-define how potential errors should be handled at runtime**:
# 
# - The *try* construct comprises a **try** block, an **except** block, and a **finally** block, which specify the statements that could raise exceptions, what should happen if exceptions occur, and what statements should be executed in any case, regardless of whether the *try* block was successfully executed or not.

# In[2]:


try:
    file = open("test.txt")
    text = file.read()
except FileNotFoundError:
    print("ERROR: file not found!")
finally:
    file.close()


# - The ***with* construct opens files and performs common cleanup tasks**, such as closing the file, regardless of whether exceptions are raised within the code block

# In[3]:


# without with
file = open('test.txt', 'w')
try:
    file.write('hello world')
finally:
    file.close()

# using with
with open('test.txt', 'w') as file:
    file.write('hello world !')


# Notice that there is **no need to call *file.close()***. The *with* statement itself ensures proper acquisition and release of resources, regardless of whether the *file.write* method throws exceptions.
