import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

def sample_normal_distribution(mu, var):
    # define variables
    std = var**0.5

    u1 = np.random.uniform()
    u2 = np.random.uniform()
    
    z = np.sqrt(-2*np.log(u1))*np.cos(2*np.pi*u2)

    y = z*std+mu


    return y
    
if __name__ == '__main__':
    y = []
    n = 10000
    mu = 100
    sigma = 15
    # plot the histogram of the data 
    # the histogram of the data
    
    for i in range(n):

        y.append(sample_normal_distribution(mu,sigma**2))

    count,bins,ignored = plt.hist(y,100,density=True)

    plt.show()
