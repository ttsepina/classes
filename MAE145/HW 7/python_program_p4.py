import numpy as np

def predict_next_pos(x, y, theta, vel_l, vel_r, t, l, R):
    # implement the exact differential drive motion model here
    # from the initial pose x,y ,theta, obtain the next pose x_1, y_1, \theta_1
   
    v = R*(vel_r+vel_l)/2
    w = R*(vel_r-vel_l)/l

    

    if w != 0:
        x_1 = x + (-v/w)*np.sin(theta) + (v/w)*(np.sin(theta+w*t))
        y_1 = y + (v/w)*np.cos(theta) + (-v/w)*(np.cos(theta+w*t))
        theta_1 = theta + w*t

        xc = x - (v/w)*np.sin(theta)
        yc = y + (v/w)*np.cos(theta)
        r = np.sqrt((x-xc)**2+(y-yc)**2)

        print('Rotational Velocity is ',w,)
        print('Curvature Radius is ',r)
        print('ICC is ',(xc,yc))

        return x_1, y_1 , theta_1
    else:
        x_1 = x +(v*t)*(np.cos(theta))
        y_1 = y + (v*t)*(np.sin(theta))
        theta_1 = theta

        print('Rotational Velocity is 0')
        print('There is no curvature radius')
        print('There is no ICC')


        return x_1, y_1 , theta_1

#print(predict_next_pos(1.5,2,(np.pi)/2,0.3,0.3,3,0.5,0.15))

if __name__ == '__main__':

    c = [0.1, 0.2, 3]
    print('c = ',c)
    print('Next position is', predict_next_pos(1.5,2,(np.pi)/2,c[0],c[1],c[2],0.5,0.15))