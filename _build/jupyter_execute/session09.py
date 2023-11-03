#!/usr/bin/env python
# coding: utf-8

# ## Recursion and trees 
# 
# ### Defining recursion
# It is time to turn everything on its head and introduce recursion into the game. **Recursion** occurs when we **define something in terms of itself or something else of its type**. For instance, we may define a file directory as a location on the computer that contains files *and (possibly) other directories*. 
# 
# Recursion is **useful for problems that can be represented as a series of subproblems of the same type**. To stay with the previous example, the problem of searching for a file, for instance, can be formulated recursively as follows (in pseudocode):
# 
#         def search(directory):
#             if file in directory:
#                 return(directory)
#             for subdirectory in directory:
#                     if search(subdirectory) != None:
#                         return search(subdirectory)
#             return None
# 
# Note that we are **calling the function *search()*** within the body of the *search()* function, and are **doing so on a smaller problem space** (i.e., a subdirectory of our main directory). 
# 
# ### Recursive functions 
# 
# **Successful recursion is recursion that terminates at some point**. It requires that we define both a **base case** and a **recursive case**. In the example above, the base case is such that either (a) we find the *file* in the current directory or (b) there is no further subdirectory to search and the file does not exist. If either (a) or (b) are the case, the function call terminates. The recursive case is entered with a *for*-loop over all subdirectories, which calls on the *search* function again and returns the subdirectory in which the file is located.
# 
# **Thus, keep the following in mind when defining recursive functions:**
# - if the function calls itself on every input, we get infinite recursion
# - in all useful recursive functions, each nested call differs in its arguments (e.g., by execution on subproblems)
# - for recursive functions to terminate, we need base cases!

# The following provides another example of a recursive function, this time in real Python code:

# In[1]:


#another example by the same principle as the file search algorithm in pseudocode above
#function that searches for the first sublist containing a specified element
def search(example, num):
    list_of_lists = [x for x in example if type(x)==list]
    if num in example:
        return example
    for i in list_of_lists:
        if search(i,num) != None:
            return search(i,num)
    return None
        
print(search([2,[2,3,[1,5],4],[4,2]], 1))


# ### Recursion in logic and mathematics
# 
# Recursive definitions are very common in logic and mathematics. **In particular, all inductive proofs are recursive**:
# 
# In induction, you prove that a theorem holds e.g. for *n = 0* (the base case), and that, under the assumption that the statement holds for any given case *n = k*, it also hold for the next case *n = k + 1* (recursive case). This proves that the theorem must hold for any natural number.
# 
# **Many definitions in logic are recursive. We have already seen an example within this class**. In a previous ression, **regular languages** were characterized as follows: 
# 
# **Given a finite alphabet Σ** (e.g., a collection of characters),...
# 
# - the empty language Ø is a regular language. **(base case)**
# - for each a ∈ Σ, the singleton language {a} is a regular language. **(base case)**
# - If A is a regular language, A&ast; (Kleene star, more below) is a regular language. That means the empty string language {ε} is also regular. **(recursive case)**
# - If A and B are regular languages, then A ∪ B (union)** and A • B (concatenation) are regular languages. **(recursive case)**
# - No other languages over Σ are regular.

# ### Recursion vs. iteration in programming
# 
# In principle, **recursion and iteration are equally powerful (meaning that one can be used to emulate the other)**. Some algorithms are **easier to write** iteratively, others are easier to write using recursion. In addition, recursive and iterative solutions to a problem can **differ in efficiency** (in terms of memory usage and completion time).
# 
# **Iteration --> Recursion**: Note that all loops can be implemented using recursion! In the following, we replace a *for*-loop with a recursive function.

# In[2]:


example2 = [2,[2,3,[1,5],4],[4,2]]

#iterative solution to print each element in list
for i in example2:
    print(i)


# In[3]:


#recursive solution to print each element in list
def recursive_print(example2,i):
    if i < len(example2):
        print(example2[i])
        recursive_print(example2,i+1)

recursive_print(example2,0)


# **Recursion --> Iteration**: At the same time, every recursive function can be implemented using iteration! Our search function from above could be rewritten as follows.

# In[4]:


#iterative solution to searching a sublist with a specified element
def iterative_search(ex, num):
    for i in ex:
        if i == num:
            print(ex)
            break
        elif type(i) == list:
             for j in i:
                if j == num:
                    print(i)
                    break
                elif type(j) == list:
                    for k in j:
                        if k == num:
                            print(j)
                            break

print(iterative_search([2,[2,3,[1,5],4],[4,2]],1))


# Recursive definitions are often easier to write for processing data structures which contain substructures of varying size (i.e. data that is not tabular in shape). 
# 
# **Examples**:
# - processing syntax trees for programming languages (in a compiler) and natural languages (in a parser)
# - processing more general graph structures like networks
# - sorting and searching in structures that are more complex than lists or dictionaries (e.g., 3-D models)

# ### In-class exercise: Fibonacci numbers
# 
# The following is the Fibonacci sequence, a sequence of numbers starting at *F<sub>0</sub> = 0* and *F<sub>1</sub> = 1*, in which each number is the sum of the previous two numbers.
# 
#     0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
#     
# To determine the *n*-th Fibonacci number in the sequence, we can write a simple recursive program:

# In[5]:


#in-class exercise
def fib(n):
    pass

print(fib(15))


# ### Visualizing recursion with the *Turtle* module 
# 
# A useful **tool to train your recursive thinking is to use a graphical interface** on which you can draw recursive structures. Just googling for *recursive fractals* should give you some inspiration.
# 
# In the following, we will **draw a tree structure in which every branch splits up into two smaller branches (recursion) unless it has leaves at its end (base case)**. We use the *Turtle* module (https://docs.python.org/3/library/turtle.html) to draw this figure, a module that provides a basic graphical interface in which we control the movements of a "turtle" (the cursor). The module has methods like *left(angle)*, *right(angle)*, *forward(length)*, *backward(length)* determining the movement of the turtle, and methods like *color(color_string)* or *pensize(int)* determining its visual properties.

# In[6]:


import turtle #import turtle module, a graphical interface to draw shapes; opens in separate window

turtle.speed(1000) #set speed of animation
turtle.setheading(90) #set initial orientation of the turtle as looking straight up

def draw_branch(len): #recursive function to draw a tree
    if (len > 5):
        turtle.color("brown") #draw branches in brown
        turtle.forward(len)
        turtle.right(25)
        draw_branch(len - 5) #recursive function call
        turtle.left(50)
        draw_branch(len - 5) #recursive function call
        turtle.right(25)
        turtle.backward(len)
    else:
        turtle.color("green") #draw leaves in green
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.color("brown") #reset color to brown
        
draw_branch(35)


# In[17]:


turtle.bye() #close Turtle window


# **The output looks like this:**
# 
# ![](https://www.dropbox.com/s/rq7gdv0w4w1alhp/turtle_tree.png?raw=1)
# 

# ### Trees + tree traversal
# 
# Speaking of trees, trees are not only ubiquitous in linguistics, they are also one of the most important data structures in computer science.
# 
# |**Trees in linguistics**|**Tree structures in computer science**|
# |---|---|
# | syllable structure trees |directory structure on file systems|
# | word structure trees | "call trees" during program execution|
# | phrase structure trees | dependencies between software packages|
# | dependency trees | |
# | derivation trees ||
# | formula structure trees ||
# 
# Trees are a useful way to maintain sorted records and **allow for efficient data retrieval and insertion**. We will see that they can be searched ("traversed") and expanded quite easily. 
# 
# #### Implementing a tree structure
# 
# The tree isn't a built-in data type in Python, but we can easily define our own data type, the Tree, as a user-defined class. We would like our Tree to have *nodes* and *leaves*, such that nodes are branching points with labels and leaves are endpoints (i.e., nodes that do not have any children). 
# 
# **For all trees, it holds that:**
# - nodes have a label, which we will store as instance variable
# - nodes have children which we will store as instance variable containing a list of (sub)trees (in which order matters!)
# - leaves do not have children. We will model this as an empty list of children []
# - every node can thus be thought of as root node of its (sub)tree
# 
# ![](https://www.dropbox.com/s/4a6s9i6etks8ryt/tree_example.png?raw=1)

# In[16]:


class Tree(object):
    def __init__(self , name='root ', children=None):
        self.name = name
        self.children = []
        self.parent = None
        if children is not None:
            for child in children:
                self.add_child(child)
                child.parent = self

    def add_child(self , node):
        assert isinstance(node , Tree)
        self.children.append(node)


# In[17]:


#this creates a tree like the one shown above
first_tree = Tree("A", children = [Tree("B"), Tree("C", children = [Tree("D", children = [Tree("F"), Tree("G"), Tree("H")]),Tree("E")])])


# In[18]:


#We can easily add new nodes to the tree:
first_tree.children[1].children[1].add_child(Tree("I"))

#We can retrieve that node again like so:
first_tree.children[1].children[1].children[0].name


# #### Traversing trees
# 
# Trees are useful data structures, in part, because they can be "traversed" in multiple ways. **Tree traversal** (also known as **tree search**) refers to the process of looking up elements in a tree by visiting (e.g. retrieving, updating, deleting) each node in a tree exactly once.
# 
# We previously looked at data structures like lists or tuples, which must always be searched / traversed in linear order. Tree structures, in comparison, can be traversed in various ways, called *depth-first* or *breadth-first* orders. Various hybrid traversal schemes are also possible. Depending one one's application, tree traversal can be substantially more efficient than linear searches. For linguistic applications, it can also be more representative of the underlying structural relations that we would like to process.
# 
# **Depth-first** traversal orders deepen the current subtree as much as possible before moving to the next sibling. **Breadth-first** traversal orders broaden the current level as much as possible before moving to deeper nodes.
# 
# There are three common ways to traverse trees in depth-first order: **in-order**, **pre-order** and **post-order**:
# - **in-order traversal**: left child first, parent, then other children
# - **pre-order traversal**: parent first, then children from left to right
# - **post-order traversal**: children from left to right, then parent
# 
# All of them are easily implemented using recursion (*in-order* here, *pre-* and *post-order* in your homework).
# 
# 1. **In-order traversal**
# 
# **Question: In which order do we visit the nodes in in-order traversal (left child first, parent, then other children)?**
# (solution at the bottom)
# ![](https://www.dropbox.com/s/4a6s9i6etks8ryt/tree_example.png?raw=1)

# In[21]:


class SearchTree(object):
    def __init__(self , name='root ', children=None):
        self.name = name
        self.children = []
        self.parent = None
        if children is not None:
            for child in children:
                self.add_child(child)
                child.parent = self

    def add_child(self , node):
        assert isinstance(node , SearchTree)
        self.children.append(node)
        
    def inorder(self):
        """In -order traversal:
        First recurse into left child , then visit the node itself ,
        then recurse into other children in order.
        :return: A list of tree nodes in in-order."""
        result = []
        if len(self.children) > 0:
            result += self.children[0].inorder ()
        result.append(self)
        for i in range(1,len(self.children)):
            result += self.children[i].inorder ()
        return result


# In[22]:


#this creates a tree like the one shown above, now using our new class of traversable trees
second_tree = SearchTree("A", children = [SearchTree("B"), SearchTree("C", children = [SearchTree("D", children = [SearchTree("F"), SearchTree("G"), SearchTree("H")]),SearchTree("E")])])

inorder_tree = second_tree.inorder()
for i in inorder_tree:
    print(i.name)


# 1. **Pre-order traversal**
# 
# **Question: In which order do we visit the nodes in pre-order traversal (parent first, then children from left to right)?**
# (solution at the bottom)
# ![](https://www.dropbox.com/s/4a6s9i6etks8ryt/tree_example.png?raw=1)

# 1. **Post-order traversal**
# 
# **Question: In which order do we visit the nodes in post-order traversal (children from left to right, then parent)?**
# (solution at the bottom)
# ![](https://www.dropbox.com/s/4a6s9i6etks8ryt/tree_example.png?raw=1)

# <br>
# <br>
# <br>
# <br>
# <br>
# 
# 
# 
# **Solution to in-order traversal: B, A, F, D, G, H, C, E**
# 
# **Solution to pre-order traversal: A, B, C, D, F, G, H, E**
# 
# **Solution to post-order traversal: B, F, G, H, D, E, C, A**
