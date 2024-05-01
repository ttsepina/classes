# A16479821 #PID

# import all modules here if you need any

import numpy as np
import random

# your file should always start from definition of functions 



def computeBFStree(AdjTable, start): 
    """ descriptions here """
    
    ##########
    #### Your code goes here ####
    ##########
    
    # keep track of all visited nodes
    visited = []
    # keep track of nodes to be checked
    queue = [start]
    # visits all the nodes of a AdjTable (connected component) using BFS
    parentDict = {}

    for vertex in AdjTable:
        if vertex == start:
                parentDict[vertex] = start
        else:
              parentDict[vertex] = ''
    
    #print(parentDict)              

    while queue != []:
        #print(queue)
        
        vertex = queue.pop(0)
        visited.append(vertex)
        for node in AdjTable[vertex]:
              #print(node)
              if parentDict[node] == '':
                    parentDict[node] = vertex
                    queue.append(node)
                    
                    #print(parentDict)

         
    #print(parentDict)
    #print(visited)
    

    # keep looping until there are nodes still to be checked
    # there should be three different types of results to return:  
    if type(AdjTable) != dict:
        return 'AdjTable is invalid'
    
    if start not in AdjTable:  
        return 'No start node in the graph'
    # or a vector of pointers parents describing the BFS tree rooted at start
    # equivalently, a list of nodes in visited order, start from the 'start node' 
    return visited # list of visited node e.g. [ 'A', 'B', 'C', 'D']
    


def computeBFSpath(AdjTable, start, goal):
    """ descriptions here """

    # define some variables etc.
    
    
    ##########
    #### Your code goes here ####
    ##########
    
    # there should be four different types of results to return:  
    if type(AdjTable) != dict:
        return 'AdjTable is invalid'
 
    if start not in AdjTable:  
        return 'No start node in the graph'

    if goal not in AdjTable:  
        return 'No start node in the graph'

    
    
    # keep track of visited nodes
    visited = []
    # keep track of all the paths to be checked
    queue = [start]
    # return path if start is goal
    parentDict = {}

    for vertex in AdjTable:
        if vertex == start:
                parentDict[vertex] = start
        else:
              parentDict[vertex] = ''
    #Condition 1
    
    while queue != []:
        #print(queue)
        
        vertex = queue.pop(0)
        visited.append(vertex)
        for node in AdjTable[vertex]:
              #print(node)
              if parentDict[node] == '':
                    parentDict[node] = vertex
                    queue.append(node)
                    
                    #print(parentDict)


    #print(parentDict)

    p = [goal]
    i = 0
    while parentDict[p[0]] != p[0]:
        p.insert(0,parentDict[p[0]])
        i+=1
        if i > len(AdjTable):
            break
    if p[0] == start:
        return p
    else:
        return "No path" # Condition 2 
                # mark node as visited
                #visited.append(node)
    # in case there's no path between the 2 nodes
    
     
    
    
    
if __name__ == '__main__':
    """ 
    This is the place where you can test your function. 
    You can define variables, feed them into your function and check the output   
    """
    
    # AdjTable defined as a dictionary 
    
    #Testing with input of AdjTable
    AdjTable = {'A': ['B', 'D'],
                'B': ['A'],
                'C': ['D'],
                'D': ['A', 'F', 'C'],
                'E': ['F'],
                'F': ['D', 'E']}
    
      
    start='A'
    goal='C'
    
    myBFSTree=computeBFStree(AdjTable, start)
    print(myBFSTree)
    # output should be a list: 
    # ['A', 'B', 'D', 'F', 'C', 'E']

    myBFSPath=computeBFSpath(AdjTable, start, goal)
    print(myBFSPath)
    # output should be a list: 
    # ['A', 'D', 'C']
    
    
    #Writing maze graph in E2.8 as the AdjTable1 and testing based on the nodes marked 
    AdjTable1 = {1: [2,3],2: [1,4,17],3: [1,4,5],4: [2,4,6],5: [3,6,7],6: [4,5,8],7:[5,8,9],
                 8: [6,7,10],9: [7,10],10: [8,9,11],11: [10,12],12: [11,13],13:[12,14],
             14: [13,15],15: [14,26,16],16: [15,32],17: [2,18],18: [17,19], 
             19:[18,20,21],20: [19,22], 21: [19,22,23],22: [20,21,24],23: [21,24,27],
             24:[22,23,25],25: [24,26],26: [25,15],27: [23,28],28: [27,29],29: [28,30],
             30:[29,31],31: [30,32],32: [16,31]}
    start, goal = 1, 32
    myBFSTree=computeBFStree(AdjTable1, start)
    print(myBFSTree)
    # solution should be a list: 
    #[1, 2, 3, 4, 17, 5, 6, 18, 7, 8, 19, 9, 10, 20, 21, 11, 22, 23, 12, 24, 
    #27, 13,25, 28, 14, 26, 29, 15, 30, 16, 31, 32]
     
    myBFSPath=computeBFSpath(AdjTable1, start,goal)
    print(myBFSPath)
    # [1, 2, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16, 32]







