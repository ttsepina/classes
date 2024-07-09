import numpy as np
import scipy.stats

def landmark_sensor_model(z, x, l):
    # z is your range and bearing, x robot pose, l is the landmark
    # position you can make use of a built in python in python to
    # compute your noise samples

    # define variables


    # compute your likelhood

    #z = [r,theta]    x = [x,y,theta]
    var_r = 0.25
    var_theta = 0.01


    #epsilon_r = np.random.normal(0,var_r**0.5)
    #epsilon_theta = np.random.normal(0,var_theta**0.5)

    z_r = np.sqrt((l[0]-x[0])**2+(l[1]-x[1])**2)
    z_theta = np.arctan2(l[1]-x[1],l[0]-x[0]) - z[1]


    prob_zr = scipy.stats.norm.pdf(z[0],z_r,var_r**0.5)
    prob_ztheta = scipy.stats.norm.pdf(z[1],x[2],var_theta**0.5)


    likelihood = prob_zr*prob_ztheta
    
    return likelihood
