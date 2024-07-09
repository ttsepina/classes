import numpy as np
import matplotlib.pyplot as plt

def box_muller(mu, var):
    # this function should give you a sample according to N(mu,sigma^2=var)

    std = var**0.5

    u1 = np.random.uniform()
    u2 = np.random.uniform()
    
    z = np.sqrt(-2*np.log(u1))*np.cos(2*np.pi*u2)

    y = z*std+mu

    return y

def predict(x_t, u_t_plus_1, alpha):
    
    u_t_plus_1_err = []
    
    u_t_plus_1_err.append(u_t_plus_1[0] - box_muller(0,alpha[0]*(u_t_plus_1[0])**2+alpha[1]*(u_t_plus_1[1])**2))
    u_t_plus_1_err.append(u_t_plus_1[1] - box_muller(0,alpha[0]*(u_t_plus_1[0])**2+alpha[1]*(u_t_plus_1[1])**2))
    u_t_plus_1_err.append(u_t_plus_1[2] - box_muller(0,alpha[3]*(u_t_plus_1[0])**2+alpha[3]*(u_t_plus_1[1])**2)+alpha[2]*(u_t_plus_1[2])**2)
    # Add noise odometry reading
    
    # Compute new pose
    x_t_plus_1 = []

    x_t_plus_1.append(x_t[0] + u_t_plus_1_err[2]*np.cos(x_t[2]+u_t_plus_1_err[0]))
    x_t_plus_1.append(x_t[1] + u_t_plus_1_err[2]*np.sin(x_t[2]+u_t_plus_1_err[0]))
    x_t_plus_1.append(x_t[2] + u_t_plus_1_err[0]+u_t_plus_1_err[1])
    

    

    return x_t_plus_1

if __name__ == '__main__':
    # plot scatter plot with 5000 positions
    n = 5000
    x = []
    y = []
    for i in range(n):

        pos = predict([2,4,0],[np.pi/2,0,1],[0.1,0.1,0.01,0.01])
        x.append(pos[0])
        y.append(pos[1])

    ax = plt.scatter(x,y)

    plt.show()
