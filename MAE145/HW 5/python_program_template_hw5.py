#!/usr/bin/env python3
"""
Guidelines for program submission: 
    
A) To ensure readability by the grader, 
    please make sure the following submission format:

    1-- Please change the file name to python_program.py 
        ---(The file name is case sensitive, make sure it's identical)---
               
    2-- The *.py file should be compressed to the root of the *.zip file
        e.g., when you submit your homework.zip, 
                Please compress the python files directly 
        ---(Do Not compress the directory!)---
                    aka, if you unzip your *.zip, *.py files should appear
                        in the directory of *.zip file. 
                        
    ---FAIL TO FOLLOW INSTRUCTION A) MAY COST YOU SOME POINTS--- 


B) Your homework should follow the similar structure as this template

C) Keep in mind some minor points:
    
    1-- Your code should not have any debug error before submission!!!

    2-- The order of the function arguments should be the same as that in HW 

    2a-- The data type of the argument should be the same as that in template
                      
    3-- make sure your function return the value which the HW requested
    
    4-- make sure the order of the output arguments the same as those in template
    
    5-- Do not round up your output values
    
    6-- Do not use input function in your function
        
    7-- if you need uncommon modules, contact TA before submission or post it on Piazza

    8-- Please do not add any variable clearing command in the file, as this may terminate grader
    


If you had any question about the guideline, 
    contact TAs or post questions on piazza for response.
        
@author: Dan Li (lidan@ucsd.edu) & Yunhai Han (y8han@eng.ucsd.edu) at UCSD
@date: Jan 2021
"""


"""
The template starts from here
"""

# A432432 #PID

# import all modules here if you need any

# import numpy as np
# import matplotlib.pyplot as plt
# your file should always start from definition of functions 


def computeGridSukharev(n): 
    """ descriptions here """

    # define some variables etc.
    X = 
    Y = 
    ##########
    #### Your main code here ####
    ##########
    return X, Y
        
    
    

def computeGridRandom(n):
    np.random.seed(1)
    """ descriptions here """

    # define some variables etc.
    
    X = 
    Y = 
    ##########
    #### Your main code here ####
    ##########
    
    
    return X, Y
     
    
def computeGridHalton(n, b1, b2):
    """ descriptions here """

    # define some variables etc.
    
    X = 
    Y = 
    ##########
    #### Your main code here ####
    ##########
    
    
    return X, Y
    
if __name__ == '__main__':
    """ 
    This is the place where you can test your function. 
    You can define variables, feed them into your function and check the output   
    """
    
    n = 4
    X, Y = computeGridSukharev(n)
    #X = [0.25, 0.75, 0.25, 0.75]
    #Y = [0.25, 0.25, 0.75, 0.75]
    #The order of points could be different, but it should be the same point set.
    
    #The points are (X[i], Y [i]) : (0.25, 0.25),(0.75, 0.25),(0.25, 0.75),(0.75, 0.75)
    #You can put the visualization codes here
    
    n = 4
    X, Y = computeGridRandom(4)
    #You can put the visualization codes here
    
    n = 4
    b1 = 2
    b2 = 3
    
    X, Y = computeGridHalton(n, b1, b2)
    #You can put the visualization codes here







