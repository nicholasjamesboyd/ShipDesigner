import numpy as np
from MotionFunctions import MotionFunctions as MF
from CostCalculator import CostCalculator as CC
from StabilityCheck import Stability as STB

#Enter Sea Parameters
hmean = 4.0
hmode = np.sqrt(2/np.pi) * hmean
tmean = 6.5
tdeviation = 1.0
h = np.reshape(np.random.rayleigh(hmode,(73000)),(-1,1)) #Generates a random significant wave height for 25 years of 3 hour seas
t = np.reshape(np.random.normal(tmean,tdeviation,(73000)),(-1,1)) #Generates random period for 25 years of 3 hour seas
Waves = np.hstack((h,t)) #Builds an array for each sea, each row is a significant wave height and peak period

#Enter Operational Parameters
field_distance = 200.0
area_cargo = 1500.0
volume_cargo = 8000.0
deadweight_cargo = 16000.0
max_vert_velocity = 4.0
cycle_length = 72

#Enter Design Limits
l_min = 60
l_max = 120
l_step = 1
b_min = 20
b_max = 30
b_step = 1
t_min = 4
t_max = 8
t_step = 1
n_min = 1
n_max = 6
stabcriteria = 0.15

hull_types = ["Axe", "X", "Vertical", "Bulbous"]

# Main Program Algorithm
for hulltype in hull_types: #Check Every Type of Hull
    for length in range(l_min,l_max+1,l_step): #Check all possible design lengths
        for beam in range(b_min, b_max+1, b_step): #check all possible beams
            for draft in range(t_min,t_max+1,t_step): #check all possible drafts
                stable, displacement = STB.CheckStability(hulltype,length,beam,draft,stabcriteria) #Performs a check of the stability for this specific hull design and calculates its displacement
                if(not stable): #if we find an unstable hull, don't proceed, skip to the next hull design
                    continue
