#!/usr/bin/env python
# coding: utf-8

# # Applications (Part II): Programming in experimental research (February 07, 2023)
# 
# **Experimental research in linguistics has grown in importance over the last few decades**. Two key research areas that depend on the experimental validation of hypotheses regarding, among others, language processing, production, and acquisition, are **psycho- and neurolinguistics**. Yet, even researchers that are primarily concerned with formal aspects of language (e.g. in syntax, semantics, or language typology) have turned to experimental research to address their research questions.
# 
# Linguistic experiments can be incredibly simple, for instance, when presenting participants with a sentence and asking for an **acceptability judgment**. Or they can be very complex, e.g., when simultaneously recording **eye-tracking** and **EEG** data while participants read sentence material.
# 
# Regardless of experiment complexity, **we can use Python to implement such experiments and to statistically analyze the recorded data**. Today, we will look at a simple example of implementing a behavioral (button-press) experiment.

# **An example for a single experimental trial in a grammaticality judgment task:**
# 
# <p style="text-align: center; font-style: italic"> Please read the following sentence: </p>
#     
# <p style="text-align: center"> Which man did Jane say that the parent who scolded him forgave the babysitter’s mistake?</p>
#  
# <p style="text-align: center; font-weight: bold"> Is this sentence acceptable? </p>
#  
# <div style="text-align: center">
#       <input type="radio" id="contactChoice1" name="contact" value="Yes" />
#       <label for="contactChoice1">Yes</label>
#       <input type="radio" id="contactChoice2" name="contact" value="No" />
#       <label for="contactChoice2">No</label>
#                                  </div>

# ## Implementing an experiment
# 
# For today's purpose, we will be concerned with experiments conducted by Lassiter (2016) and Yastushiro et al. (2022) on epistemic modal adjectives and adverbs like *possible/possibly* and *certain/certainly*.
# 
# 
# **Background**
# 
# Epistemic modal expressions provide an estimation of the likelihood that the state of affairs expressed in the clause applies to the world, according to either the speaker or some other epistemic authority (Nuyts, 2016). As such, epistemic modality can arguably be “subjective” or “objective” (Lyons, 1977), in that "the former refers to the personal opinion of the speaker, whereas the latter refers to some factual chance that is of an interpersonal nature" (Yatsushiro et al., 2022).
# 
# In English, it has been suggested that subjective and objective epistemic modality are (preferably) expressed by different linguistic forms. Specifically, epistemic modal adverbs like in (2) might be interpreted subjectively, whereas epistemic adjectives like (3) might be interpreted objectively (Hengeveld 1988; Nuyts 1992; 1993).
# 
#         (2) Abdul certainly / probably / possibly is at school.
# 
#         (3) It is certain / probable / possible that Abdul is at school.
# 
# This distinction is further supported by distributional differences regarding their appearance under negation and in questions (for details, see Yatsushiro et al., 2022):
# 
#     (4) a.  Abdul is *uncertainly at school.
#         b. It is not certain that Abdul is at school.
#     
#     (5) a. Is Abdul *certainly at school?
#         b. Is it certain that Abdul is at school?
#     
# **The research question**
# 
# "Do these two types of epistemic operators [really] have different interpretations? That is, given a certain situation that leads to a certain estimation of likelihood for a proposition, would speakers apply an epistemic adjective differently from its corresponding epistemic adverb?" (Yatsushiro et al., 2022) 
# 
# **Method** (Lassiter, 2016; Yatsushiro et al., 2022 Experiment 2)
# 
# Participants read a context scenario that provides a measureable likelihood for a certain event (6). In a subsequent critical sentence (6a-d), they are confronted with an epistemic modal adjective or adverb. They must provide a judgment of **whether they agree with the assertion**. The hypothesis is that participants "would be less strict in their use of subjective *possibly* and *certainly*, on the ground that a privately held certainty, or denial of possibility, may be felt to be less subject to public scrutiny and approbation if it turns out to be incorrect." (Lassiter, 2016: 132)
# 
# 
#         (6)  (Low likelihood of win)
#              Yesterday, Bill bought a single ticket in a raffle with 1000 total tickets. 
#              There were also 999 other people who bought one ticket each. 
#              The drawing was held last night, and the winner will be announced this evening.
# 
#             a. It is possible that Bill won the raffle. 
#             b. Bill possibly won the raffle.       
#             c. It is certain that Bill did not win the raffle.     
#             d. Bill certainly did not win the raffle.
# 
#         (7) (High likelihood of win)
#             999 tickets to a raffle were purchased by Jay, a wealthy local businessperson. 
#             1 ticket was purchased by a member of the community. 
#             The drawing was held last night, and the winner will be announced this evening.
#                   
#             a. It is certain that Jay won the raffle.     
#             b. Jay certainly won the raffle.
#             
# Thus, these are the predictions:
# 
# - in (6), *possibly* should be less assertable / dispreferred to *possible* (because although objectively possible, the  agent may privately assume / **commit themselves to** (Krifka, to appear) the fact that it is *not* likely that Bill would win the raffle)
# - in (6), *certainly* should be more assertable / preferred over *certain* (because although not objectively certain, the  agent may privately assume / commit themselves to the fact that it is quite certain that Bill would not win the raffle)
# - in (7), *certainly* should be more assertable / preferred over *certain* (reasoning analogous to the previous examples)

# ### Experimental setup using *pygame*
# 
# *Pygame* is a Python package primarily designed for writing video games. Experiments, in many respects, are just like video games, thus the module has become popular for the implementation of (behavioural) experiments.
# 
# Like in video games, we need to:
# 
# - **control frame-by-frame visual displays**, including the appearance of images, text, and other elements.
# - in some cases, this includes **synchronized audiovisual signals**
# - **record and save** reaction times, button presses and other user-provided input
# - **conditionally execute parts of the code** based on button presses or other user input
# 
# **Pygame offers a range of methods to do this.** With respect to **visual displays**, the *display* module offers a range of methods that allow you to control the contents displayed on screen. Pygame has a single display Surface that is either contained in a window or runs full screen. You must first initialize this surface, e.g., as fullscreen display or window of specified dimensions:
# 
#     screen = pygame.display.set_mode((1280, 480), pg.SCALED)
#    
# Then you can modify the contents of that surface, e.g., by changing its color or adding text / images at varying positions. Changes are not immediately visible on the real screen; you must use the "flipping" function *flip()* to update the actual display.
#     
#     bgColor = (0,0,80) # darkblue
#     screen.fill(bgColor)
#     pygame.display.flip() 
#     
# With respect to **recording (and reacting to) user input**, Pygame continually records all user input as "events" in an event queue. Events can have different types, such as key presses, mouse clicks, or movements of a joystick. The *get()* method gets all events from the current queue and removes them from it. By calling this method repeatedly, on every single frame, until a specified event occurs, we can control the execution of the experiment. 
# 
#      #function that waits for any key press
#         def waitForAnyKey():
#             while True:
#                 for event in pygame.event.get():
#                     if event.type == pygame.KEYDOWN:
#                         return event.key  #returns key numbers
#                     elif event.type == pygame.QUIT:
#                         pygame.quit()
#                         
#                         
# **Let's look at an implementation of the experiment that is introduced above:**

# In[1]:


# -*- coding: utf-8 -*-
# these are texts, that are used in different places during the experiment

#########################Instruction texts######################################################
starting_instructions = """Dear participant,

thank you for deciding to take part in out study. By participating, you confirm that you are an English native speaker and at least 18 years old.

This study is about language comprehension in English. It consists of a single trial in which you will read a short story and will answer a question about it.

This study should take no more than 2-3 minutes. Please take your time to read each sentence that appears on screen and press the space bar to proceed to the next one.

The question at the end of the story can be answered by pressing the number keys 1 or 2, as will be indicated on the screen.

Your data will be treated anonymously. You can abort the experiment at any time without negative consequences. To exit, press the Escape key.

Department of Linguistics
University of Tübingen 2022
"""

###############################################################################
leertasten_hinweis = """To start, please press the space bar."""

after_practice_instructions = """The experiment will start now.
"""
###############################################################################
end_trial = "Continue by pressing the space bar."
###############################################################################
end_experiment = """Thank you for participating!

We would like to cordially thank you for your participation. Your data has been saved anonymously.
You can close this window now.

Deptartment of Linguistics
University of Tübingen 2022
"""
###############################################################################
preparing_data_string = "Preparing the data. Please wait..."
###############################################################################
press_any_key = "Press any key to continue."
###############################################################################
enter_subnr_text = "Please enter a subject number and confirm with Enter:"    
error_subnr_already_taken = "This number is already taken. Please choose a different one."
enter_age_text = "What is your age (in number of years)? Confirm with Enter."
enter_gender_text = "Please indicate your gender:"     
dialect_text = "Do you speak any dialect?"        
dialect_text_2 = "Which one? Enter as text and confirm with Enter" 


# In[2]:


import pygame

#############################################################################
############     Functions that regulate display of text on screen ##########
############################################################################
CENTER = 0
NEWLINECENTER = 1
ERRORPOS = 2
BOTTOM = 3
OPTIONS = 5
TOP = 6

#we show different texts at different positions. This function simply makes that more clear.
def get_position(screen, text_surface, where):
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    width = screen.get_width()
    height = screen.get_height()
    if where == CENTER:
        return width/2-text_width/2, height/2-text_height/2
    elif where == NEWLINECENTER:
        return width/2-text_width/2, 5.0/8*height
    elif where == ERRORPOS:
        return width/2-text_width/2, 3.0/8*height
    elif where == BOTTOM:
        return width/2-text_width/2, height-1.5*text_height
    elif where == OPTIONS:
        return width/2-text_width/2, 3.0/4*height
    elif where == TOP:
        return width/2-text_width/2, 1.0/10*height

#this shows all the one-line-texts
def showText(screen, text, where, fontsize, textColor, bgColor, eraseAll=False): 
    if eraseAll: #if specified to be true, clear the screen of all contents
        screen.fill(bgColor) 
    font = pygame.font.SysFont("verdana",fontsize) 
    text_surface = font.render(text, True, textColor, bgColor)
    posx, posy = get_position(screen, text_surface, where)
    screen.blit(text_surface, (posx, posy)) #copies the text to positions x, y
    pygame.display.flip() #flips the contents to the designated screen
 
    
    
# this function takes one line of text and displays it at the screen center
def showTextCenter(screen, text, fontsize, textColor, bgColor, eraseAll = True): 
    showText(screen, text, CENTER, fontsize, textColor, bgColor, eraseAll)
    

# to display a new line of text without erasing the first
def showTextNewLine(screen, text, fontsize, textColor, bgColor):
    showText(screen, text, NEWLINECENTER, fontsize, textColor, bgColor)


# error messages
def showErrorText(screen, text, fontsize, textColor, bgColor): 
    showText(screen, text, ERRORPOS, fontsize, textColor, bgColor, eraseAll = True)
    
# show answer options for multiple choice questions
def showOptions(screen, options, fontsize, textColor, bgColor):  
    showText(screen, options, OPTIONS, fontsize, textColor, bgColor)  
    

#displays a longer text. Splits the longer text up into several lines if it doesn't fit on to the screen.
def showInstructions(screen, text, fontsize, textColor, bgColor, overwriteBg = True, startAtLine = 0, continueText=""):
    if continueText == "": 
        continueText = press_any_key
    if overwriteBg:
        screen.fill(bgColor)
    font = pygame.font.SysFont("verdana",fontsize) 
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    width = screen.get_width()
    height = screen.get_height()
    pos = width//10, height//10
    x, y = pos
    y += startAtLine*font.render(" ", 0, textColor).get_size()[1]
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, textColor)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= (width//10)*9: #if word does not fit onto current line anymore
                x = pos[0]  # Reset the x position.
                y += word_height  # Start on new row.
            screen.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # after each line, reset the x position
        y += word_height  # and start on new row.
            
    showText(screen, continueText, BOTTOM, fontsize, textColor, bgColor)
    pygame.display.flip()
    

# to enter the subject id or age of subjects
def enterNumber(screen, text1, fontsize, textcolor, bgColor, EnterKey, EscapeKey=pygame.K_ESCAPE, errortext=""):  
    showTextCenter(screen, text1, fontsize, textcolor, bgColor)   
    if errortext != "":
            showErrorText(screen, errortext, fontsize, textcolor, bgColor)   
    nr = ""
    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.KEYDOWN:
                if evt.unicode.isnumeric():
                    nr += evt.unicode
                elif evt.key == pygame.K_BACKSPACE:
                    nr = nr[:-1]
                    eraseText(screen, fontsize, OPTIONS, bgColor)
                    pygame.display.flip() 
                elif evt.key == EnterKey[1]:
                    if len(nr) > 0:
                        return int(nr)
                elif evt.key == EscapeKey:
                    return
            elif evt.type == pygame.QUIT:
                return
        showText(screen, nr, OPTIONS, fontsize, textcolor, bgColor)
        


# to enter the gender of the subject
def enterGender(screen, text, fontsize, textcolor, bgColor):   
    showTextCenter(screen, text, fontsize, textcolor, bgColor)        
    choicetext = 'a. %s     b. %s     c. %s     d. %s' %('male','female','non-binary','prefer not to answer')
    showOptions(screen, choicetext, fontsize, textcolor, bgColor)
    while True:
        key = waitForAnyKey()
        if key == pygame.QUIT or key == pygame.K_ESCAPE:
            return
        if key == pygame.K_a:
            return "m"
        elif key == pygame.K_b:
            return "f"
        elif key == pygame.K_c:
            return "nb"
        elif key == pygame.K_d:
            return "na"
            
    

# does subject speak a dialect?
def enterDialect(screen, text, text2, fontsize, textcolor, bgColor):
    showTextCenter(screen, text, fontsize, textcolor, bgColor)        
    choicetext = 'a. %s     b. %s' %('yes','no')
    showOptions(screen, choicetext, fontsize, textcolor, bgColor)
    while True:
        key = waitForAnyKey()
        if key == pygame.QUIT or key == pygame.K_ESCAPE:
            return
        elif key == pygame.K_a:
            return [1, enterDialectRegion(screen, text2, fontsize, textcolor, bgColor)]
        if key == pygame.K_b:
            return [0, '']
        

    
# if subject speaks a dialog, which one?          
def enterDialectRegion(screen, text2, fontsize, textcolor, bgColor):
    showTextCenter(screen, text2, fontsize, textcolor, bgColor)
    dialect = ""
    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.KEYDOWN:
                if evt.unicode.isalpha():
                    dialect += evt.unicode
                elif evt.key == pygame.K_BACKSPACE:
                    dialect = dialect[:-1]
                    pygame.display.flip()
                elif evt.key == pygame.K_RETURN:
                    return dialect
                elif evt.key == pygame.K_ESCAPE:
                    return
            elif evt.type == pygame.QUIT:
                return
        showOptions(screen, dialect, fontsize, textcolor, bgColor)


#wait for any key press
def waitForAnyKey():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return event.key  #returns key numbers
            elif event.type == pygame.QUIT:
                return

#wait for specific key press
def waitForKey(which):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == which:
                    return True
            elif event.type == pygame.QUIT:
                return  


# In[3]:


# -*- coding: utf-8 -*-
"""
@author: Juliane Schwab, Scientific Programming 2022/2023
"""

import pygame
import random
from pygame import time as ptime
import os
import csv
import numpy as np
import sys
import threading
import time

#correspondence between columns in csv stimulus file and variables defined here
EXPTYPE = 0
ITEM = 1
IS_PRACT = 2
COND = 3 
S1 = 4 
S2 = 5 
S3 = 6 
S4 = 7 
ANSWER1 = 8 
INDEX = 9
LISTNUM = 10

NUMSENTS = 6

CSV_ENCODING = "ISO-8859-1"


###############################################################################
#these are variables that may be changed depending on the experiment we use the code for.
###############################################################################

# amount of lists. If you have eg two lists, every even subject will use list 2, etc.
CONDITIONS = [1, 2, 3, 4, 5, 6]
             
datafolder = "data/"
csvfolder = "results/"
if not os.path.exists(csvfolder):
    os.mkdir(csvfolder)



###############################################################################
#settings for the look of the experiment
###############################################################################


WaitForKey2 = ["Enter", pygame.K_RETURN] 
WaitForKey1 = ["Space", pygame.K_SPACE]     

#for yes/no questions
responses1 = [["Yes", "1", pygame.K_1], ["No", "2", pygame.K_2]]

escape = pygame.K_ESCAPE

fontsize = 24 
instructions_fontsize = 20 
textColor = (255,255,255) # white
bgColor = (0,0,80) # darkblue
bgColor2 = (0,0,80) # darkblue



###############################################################################
################### functions working on the csv-files ########################
###############################################################################


def find_sub_files(sub, folder):
    """
    Figures out the location of the respective subject data files, and returns a catchable error if they already exist.
    If the error occurs in the main loop, the subject can simply enter another number.
    """
    outfile_long = "%ssub_%s_long.csv" %(folder, sub)
    if os.path.isfile(outfile_long):
        raise FileExistsError("There is already a file for that participant!") 
    return outfile_long


def create_sub_files(sub, folder):
    """
    writes the header of the sub-file.
     fields that are saved are:
     subject_id, list, trial, experiment, item, condition, sen_num, rt, answer, fits_pred
    """

    outfile_long = find_sub_files(sub, folder)
    header = ["subject_id",  "StimulIndex", "trialnum", "which_experiment", "itemnr", "condition", "sentence_num", "reading/responseTime", "answer1", "answer1AsPredicted"]
    
    with open(str(outfile_long[0]), "w", newline="") as file:
            csv.writer(file, delimiter=';').writerow(header)
    
    return outfile_long



def append_to_CSVs(fields, longfile, sentence_num):
    """
    We created the csv already, so with every new question, we simply add a row to that csv.
    This function gets called called after every sentence of a trial.
    """ 
    with open(str(longfile[0]), 'a', newline='') as f:
        csv.writer(f, delimiter=';').writerow(fields)              



def appendto_subInfo_file(folder, sub, age, gender, d1, d2, condition, comment):
    """We also have one file "subsToInfo.csv", in which we externally store the demographic  information
       (age, gender, dialect)
       together with the corresponding subject-number
    """
    filestring = folder+"subsToInfo.csv"
    if os.path.isfile(filestring):
        mode = "a"
    else:
        mode = "w"
    with open(filestring, mode, newline='') as f:
        if mode == "w":
            csv.writer(f, delimiter=";").writerow(["Subject_Number", "Age", "Gender", "Speaks_Dialect", "What_Dialect", "Does_Condition", "Comments"])
        csv.writer(f, delimiter=';').writerow([sub, age, gender, d1, d2, condition, comment])
            

###############################################################################
############## functions to read and filter the data files ####################
###############################################################################

def read_data(folder):
    """ Reads all experiment-data from the "together.csv"-file in the folder folder. If that is non-existent, it creates the file first, using the 4 subfiles """
    if os.path.isfile(folder+"Stimuli.csv"):
        exp1 = read_file(folder+"Stimuli.csv")
    else:
        raise FileNotFoundError("Filename must be 'Stimuli.csv'!")
    return exp1



def read_file(file_name):
    """ Reads a file (csv), fields must be seperated by ';', and seperates it linewise and by field.
        Returns a list of lists: [[line1_entry1, line1_entry2, ...], [line2_entry1, line2_entry2, ...], ...] 
        Leaves out the first row, which contrains the header. Also leaves out empty rows."""
    assert os.path.exists(file_name), "File %s missing!" %file_name
    with open(file_name, mode='rt', encoding=CSV_ENCODING) as f: 
        reader = csv.reader(f, delimiter=';', quotechar='|')
        datafields = [line for line in reader if (line != "" and not ("exp" in line[0].lower()))]
    return datafields


###############################################################################
###############################################################################
###############################################################################


def enter_proband_info(screen, fontsize):
    """ In the beginning of the experiment, we ask for demographics (sub-nr, age, gender, dialect).
        This function will get called right at the beginning of the main loop."""
    sub = enterNumber(screen, enter_subnr_text, fontsize, textColor, bgColor2, WaitForKey2)
        
    dobreak = False    
    while not dobreak: #this loop will ask the subject to enter a new sub-number as long as the entered one is already taken.
        dobreak = True
        #tries to generate a new sub file, unless one by that name already exists
        try: 
            _ = find_sub_files(sub, csvfolder)
        except FileExistsError:
            dobreak = False
            sub = enterNumber(screen, enter_subnr_text, fontsize, textColor, bgColor2, WaitForKey2, errortext=error_subnr_already_taken)
        if dobreak:
            break
    
    age = enterNumber(screen, enter_age_text, fontsize, textColor, bgColor2, WaitForKey2)
    gender = enterGender(screen, enter_gender_text, fontsize, textColor, bgColor2)
    dialect = enterDialect(screen, dialect_text, dialect_text_2, fontsize, textColor, bgColor2)
    d1 = dialect[0] #IF the subject speaks a dialect
    d2 = dialect[1] #WHICH dialect they speak
    return sub, age, gender, d1, d2



def run_all_trials_from_list(curr_list, screen, sub, yourcond, file_long):
    """
    This function takes as input the entire list of trials for the subject, loops through this list, and executes
    the trial-function for every single one.
    This allows us to have more than one trial.
    """
    ind = 0
    for line in curr_list: 
        ind += 1  
        presentences = [S1, S2, S3, S4]
        sentences = []
        for currsent in presentences:
            if line[currsent] != "":
                sentences.append(currsent)
            
        trial(ind, line, sentences, screen, sub, yourcond, file_long) 


def trial(trial, line, sentences, screen, sub, yourcond, file_long):
    """ function to run one trial
    displays the context sentences and the critical sentence
    registers which answer option was chosen and saves it along with their reaction time
    parameters:
        trial - trial number, for saving the data
        line - one line from the data-file
        file_long: the path of the csv-files in which to store the result
    """
    
    sentence_num = 0
    itemnr = int(line[ITEM])
    condition = int(line[COND] )
    sents = [line[i] for i in sentences]
    answer1 = line[ANSWER1]
    index = line[INDEX]
                   
    # going through the sentences and displaying one at a time   
    for currsent in sents:
        sentence_num += 1
        
        currsentence = currsent.encode(CSV_ENCODING)
        
        showTextCenter(screen, currsentence, fontsize, textColor, bgColor) 
        t1 = ptime.get_ticks() # rounds to the 100ths of a second
        
        
        if (currsent == sents[-1]): #If its the last sentence, 
            #you don't wait for the space bar input (in the else-loop), but for the reaction of  the user (after the else-loop)
            break
        
        else:                       
            answered = False
            while not answered:
                key = waitForAnyKey()
                if key == escape or key == None: #user either pressed escape-key or the X at the top right
                    endProgram()
                    return 
                elif key == WaitForKey1[1]: #spacebar
                    answered = True
                    t2 = ptime.get_ticks() #calculate the reading time of the sentence and save it in the long csv-file
                    rt = t2-t1
                    append_to_CSVs([sub, index, trial, "modal", itemnr, condition, sentence_num, rt, ""], file_long, sentence_num)
    

    response1 = janein(screen) 
    fits1 = response1 == answer1 
    t2 = ptime.get_ticks()
    rt = t2-t1 # calculate the reaction time
    
    to_save = [sub, index, trial, "modal", itemnr, condition, sentence_num, rt, fits1]
    
    append_to_CSVs(to_save, file_long, sentence_num)
    
    showTextCenter(screen, end_trial, fontsize, textColor, bgColor)
    if waitForKey(WaitForKey1[1]) == None: #if the user presses the X, you end the program
        endProgram()
    
    

def janein(screen): 
    """function to display 2 choices, enter answer with one of two keys
    returns which choice was made
    parameter choices: given choices
    parameter exp_type: to know from which list of distractors to choose a word (if there are only 2 choices given)
    """
  
    choicetext = '%s) %s                   %s) %s'%(responses1[0][1],responses1[0][0],responses1[1][1],responses1[1][0]) 
    showOptions(screen, choicetext, fontsize, textColor, bgColor)
    while True:
        key = waitForAnyKey()
        if (key == responses1[0][2]): #yes
            return responses1[0][0]
        elif (key == responses1[1][2]): #no
            return responses1[1][0]
        elif (key == escape) or (key == None):
            endProgram() 
            return


###############################################################################
###############################################################################
###############################################################################


def endProgram():
    pygame.quit()
    sys.exit()


def main():
    #initiating the experiment....
    pygame.init()
    
    modes = pygame.display.list_modes(0, pygame.FULLSCREEN)
    screen=pygame.display.set_mode(modes[0], pygame.FULLSCREEN)
    
    
    #showing the starting instructions.....
    if starting_instructions != "":
        showInstructions(screen, starting_instructions, instructions_fontsize, textColor, bgColor2)
        waitForAnyKey();
                     
    
    #collect demographic data by calling the enter_proband_info function
    sub, age, gender, dialect1, dialect2 = enter_proband_info(screen, fontsize)
     
    
    # read in the data file and assign an experimental condition to the subject based on their sub nr.
    exp_list = read_data(datafolder)
    yourcond = CONDITIONS[(sub-1) % len(CONDITIONS)]
    exp_list = [line for line in exp_list if line[LISTNUM] == str(yourcond)] #only keep the trial that will be shown to the participant

    
    #prepare the CSVs to save the results into
    file_long = create_sub_files(sub, csvfolder)
     
        
    #now for the real experiment...
    showInstructions(screen, after_practice_instructions, fontsize, textColor, bgColor)
    waitForAnyKey()
    
    run_all_trials_from_list(exp_list, screen, sub, yourcond, file_long)
    
    
    #show the finishing instructions and we're done!
    showInstructions(screen, end_experiment, fontsize, textColor, bgColor)
    time.sleep(0.5)
    waitForAnyKey()
    
    endProgram()



if __name__ == '__main__':    
    main()


# **Here is what our stimulus file looked like:**
# ![](https://www.dropbox.com/s/wy4qcj32crpn3xk/stimuli.png?raw=1)
# 
# 
# **And here's what the recorded results file looks like:**
# ![](https://www.dropbox.com/s/xcvs0q4nialu53v/result.png?raw=1)
# 

# ### Descriptive data exploration
# 
# to be added...
