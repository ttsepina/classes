from workspace import Workspace
from ROS2.coord_handling import initialize_wksp_obs,LonLat_To_XY
import numpy as np
import shapely

master = initialize_wksp_obs('test3.txt')

workspace = master['wksp']
origin = master['origin'][0]
obs_dict = master['obs_dict']

goal_location = (32.881275,-117.235466)
goal_location = np.subtract(LonLat_To_XY(goal_location[1],goal_location[0]),origin)

ws = Workspace(workspace,obs_dict,)