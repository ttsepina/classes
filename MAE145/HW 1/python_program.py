#A16479821

'''
print('Test 1')
p1 = [1,1]
p2 = [2,2]
q = [3,4]
'''

'''
print('Test 2')
p1 = [0,2]
p2 = [2,2]
q = [1,2]
'''

#'''
print('Test 3')
p1 = [2,0]
p2 = [2,2]
q = [5,2]
#'''

def computeLineThroughTwoPoints(p1,p2):
    
    if type(p1) and type(p2) is list:
        a = p2[1] - p1[1]
        b = -(p2[0] - p1[0])
        c = p1[1]*(-b) + (-a)*p1[0]
        return([a,b,c])                     # Computes and returns constants required to generate standard form for equation of a line from 2 points
    else:
        print('Point arguments must be lists with x-y coordinates as entries')

def computeDistancePointToLine(q,p1,p2):
    if type(q) and type(p1) and type(p2) is list:
        l = computeLineThroughTwoPoints(p1,p2)
        distance = abs(l[0]*q[0]+l[1]*q[1]+l[2])/((l[0]**2 + l[1]**2)**0.5) #
        return distance
    else:
        print('Point arguments must be lists with x-y coordinates as entries')

def computeDistancePointToSegment(q,p1,p2):
    if type(q) and type(p1) and type(p2) is list:
        l = computeLineThroughTwoPoints(p1,p2)
        
        distance = computeDistancePointToLine(q,p1,p2)
        
        qp1 = [q[0]-p1[0],q[1]-p1[1]]
        p2p1 =  [p2[0]-p1[0],p2[1]-p1[1]]
        mag2_p2p1 = (p2p1[0]**2 + p2p1[1]**2)

        u = (qp1[0]*p2p1[0]+qp1[1]*p2p1[1])/(mag2_p2p1)  #Defines ratio of projection of line p1_q with the length of the segment p1_p2

        if u > 1:                                        # q is closer to p1 if the dot product is negative, and closer to p2 when the dot product is longer than the original segment
            w = 2
        elif u < 0:
            w = 1
        else:
            w = 0
        return [distance,w]
    else:
        print('Point arguments must be lists with x-y coordinates as entries')

print('Line Through Two Points:')
print(computeLineThroughTwoPoints(p1,p2))

print('Distance from point to line:')
print(computeDistancePointToLine(q,p1,p2))

print('Distance from point to segment:')
print(computeDistancePointToSegment(q,p1,p2))
