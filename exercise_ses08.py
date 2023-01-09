# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 11:58:43 2023

@author: Juliane
"""

a = [1, "Arthur", True, [False], 2.75, "boxes"];

b =  sorted(a, key = lambda x: str(x).lower()); 

#always include lower!
#note what happens with the list! (is treated as string starting with special character)

#our tools as hints:
    
#sort()
#sorted()
#lambda
#key
#lower


#Qs:

#1. what you often see is something like "functions.py" and "program.py" with import functions
#- what are the advantages? (sharability, user can modify parameters in main program, easy to adapt!) 
#2. what is transliteration? Does somebody here speak Arabic and can confirm the accuracy?
#3. somebody know what a regular language is?
# 4. let's write an FSA for the following:
    #  ((aa)* | (b|c)+ ) d
    
    #Start-b,c->Z1
    #Start-d-> End
    #Z1->b,c->Z1
    #Z1-d->End
    #Start-a-> Z2
    #Z2 -a-> Z3
    #Z3-a-> Z2
    #Z3-d->End
    
#Let's think again of some areas of application, specifically in linguistics. Where do you think such search patterns could come in handy?
#1. e.g., looking for a word form in all its inflections: walk(ing|s|ed)*
#2. e.g., combined with annotated corpus data, looking for all patterns of word forms like "N + Prep + V + N"...
#3. and so on...