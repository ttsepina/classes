# A432432 #PID
#Taymor Tsepina

# import all modules here if you need any

import numpy as np
import matplotlib.pyplot as plt
# your file should always start from definition of functions 


def computeGridSukharev(n): 
    """ descriptions here """

    k = int(np.sqrt(n))

    X = []
    Y = []

    for i in range(2*k):
        if i%2 == 0:
        
            for j in range(2*k):
                if j%2 == 0:
                    X.append((i+1)/(2*k))
                    Y.append((j+1)/(2*k))

    return X, Y
        
    
    

def computeGridRandom(n):
    np.random.seed(1)
    """ descriptions here """
    k = int(np.sqrt(n))

    X = []
    Y = []
    

    for i in range(k):
            for j in range(k):
                    X.append(np.random.rand())
                    Y.append(np.random.rand())    
    
    return X, Y
    
    
def computeGridHalton(n, b1, b2):
    """ descriptions here """

    # define some variables etc.
    
    X = []
    Y = []
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
    
    plt.scatter(X, Y, color='r', marker='o')
    plt.title("Sukharev Grid")
    plt.xlim((0,1))
    plt.ylim((0,1))
    plt.show()



    n = 4
    X, Y = computeGridRandom(4)
    #You can put the visualization codes here
    
    plt.scatter(X, Y, color='r', marker='o')
    plt.title("Random Grid")
    plt.xlim((0,1))
    plt.ylim((0,1))
    plt.show()

    n = 4
    b1 = 2
    b2 = 3
    
    X, Y = computeGridHalton(n, b1, b2)
    #You can put the visualization codes here







