# -*- coding: utf-8 -*-
"""
Created on Sun Jan  15 11:58:43 2023

@author: Juliane
"""

#two files, one as module for the other

#first, module file:
def count_words(*strings):
    j = []
    for i in strings:
        j.append(i.split())
    return(list(map(len, j)))
        

if __name__ == "__main__" :
    def file_get_line(file, line):
        with open(file, 'r') as file:
            return(file.readlines()[line])
    
    line1 = file_get_line("hitchhikers_guide_full.txt", 50)
    line2 = file_get_line("hitchhikers_guide_full.txt", 75)  


    print(count_words(line1, line2))
#######################################
# second, stand-alone file:

#import first-file

print(count_words("Why","are you","this way?")) #works

print(file_get_line("hitchhikers_guide_full.txt",30)) #does not work if module is imported