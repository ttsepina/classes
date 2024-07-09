import shapely
from workspace import Workspace
from coord_handling import initialize_wksp_obs,XY_To_LonLat,LonLat_To_XY
import numpy as np
import matplotlib.pyplot as plt


master = initialize_wksp_obs('test3.txt')
print(type(master['origin'][0][1]))

workspace = master['wksp']
origin = master['origin']
obs_dict = master['obs_dict']

print(origin)

start_location = (-35,5)
goal_location = [32.881275,-117.235466]

goal_location = LonLat_To_XY(goal_location[1],goal_location[0])

print(goal_location)


ws = Workspace(workspace,obs_dict,start_location,goal_location,boundary_type=1,buffer = 0.2,origin=origin)
path_coords = ws.path_coords


if __name__ == '__main__':
    

    shapely.plotting.plot_polygon(ws.free_workspace)

    for shape in ws.triangles:
        shapely.plotting.plot_polygon(shape)

    for edge in ws.edges:
        shapely.plotting.plot_line(edge)

    for node in ws.path:
        shapely.plotting.plot_points(ws.nodes[node])
    
    plt.pyplot.show()
    
    
