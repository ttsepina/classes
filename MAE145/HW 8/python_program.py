import numpy as np
from scipy.stats import norm

def landmark_sensor_model(z,x,l):

    #z = [r,theta]    x = [x,y,theta]
    var_r = 0.25
    var_theta = 0.01


    #epsilon_r = np.random.normal(0,var_r**0.5)
    #epsilon_theta = np.random.normal(0,var_theta**0.5)

    z_r = np.sqrt((l[0]-x[0])**2+(l[1]-x[1])**2)
    z_theta = np.arctan2(l[1]-x[1],l[0]-x[0]) - z[1]


    prob_zr = norm.pdf(z[0],z_r,var_r**0.5)
    prob_ztheta = norm.pdf(z[1],x[2],var_theta**0.5)


    return prob_ztheta*prob_zr

if __name__ == '__main__':
    
    #z = [5,np.pi/4]
    #z = [5,0.6]
    #z = [4.5, np.pi/4]
    z = [5.5,0.9]
    x = [2,3,(np.pi)/4]
    l = [2,8]
    
    print('prob(z) = ')
    print(landmark_sensor_model(z,x,l))
