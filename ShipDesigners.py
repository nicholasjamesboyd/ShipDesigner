#Declare required components
import numpy as np
import math
import MotionFunctions as MF
import CostCalculator as CC
import StabilityCheck as STB

#Enter Sea Parameters
hmean = 4.0 #mean wave height
hmode = np.sqrt(2/np.pi) * hmean
tmean = 6.5 #mean wave period
tdeviation = 1.0 #wave period standard deviation
h = np.reshape(np.random.rayleigh(hmode,(73000)),(-1,1)) #Generates a random significant wave height for 25 years of 3 hour seas
t = np.reshape(np.random.normal(tmean,tdeviation,(73000)),(-1,1)) #Generates random period for 25 years of 3 hour seas
Waves = np.hstack((h,t)) #Builds an array for each sea, each row is a significant wave height and peak period

#Enter Operational Parameters
field_distance = 200.0 #Distance in nautical miles
area_cargo = 1500.0 #Total deck area of cargo delivered per cycle m^2
volume_cargo = 8000.0 #Total bulk volument of cargo per cycle m^3
deadweight_cargo = 16000.0 #Total weight of cargo per cycle tonnes
max_vert_velocity = 0.4 #Maximum tolerable vertical velocity for which the cargo operations can occur m/s
cycle_length = 72 #Length of a cargo cycle in hours
StandbyShipRequired = True #Is a ship required for standby
fuel_cost = 289.0 #Fuel cost is dollars/mt

#Enter Design Limits
l_min = 60 #minimum length considered in m
l_max = 120 #maximum length considered in m
l_step = 1 #length stepping for design cases in m
b_min = 20 #minimum beam considered in m
b_max = 30 #maximum beam considered in m
b_step = 1 #beam stepping for design cases in m
t_min = 4 #minimum draft considered in m
t_max = 8 #maximum draft considered in m
t_step = 1 #draft stepping for design cases in m
if (StandbyShipRequired): #If a ship is required to be on standby we cannot have less than 2 ships
    n_min = 2
else:
    n_min = 1
n_max = 6 #Maximum fleet size considered
stabcriteria = 0.15 #Minimum GM value to be considered stable

hull_types = ["Axe", "X", "Vertical", "Bulbous"]

def CalculateRuns(hulltypes,lmin,lmax,lstep,bmin,bmax,bstep,tmin,tmax,tstep,nmin,nmax): #calculate all the runs we need so we can initialize an appropriate numpy array, add 1 to account for the first value
    lruns = math.floor((lmax-lmin)/lstep)+1
    bruns = math.floor((bmax-bmin)/bstep)+1
    truns = math.floor((tmax-tmin)/tstep)+1
    hullruns = len(hulltypes)
    nruns = nmax - nmin + 1
    return lruns*bruns*truns*hullruns*nruns

runs = CalculateRuns(hull_types,l_min,l_max,l_step,b_min,b_max,b_step,t_min,t_max,t_step,n_min,n_max)

results0 = np.zeros([runs,7]) #Initialize Array
results1 = np.empty([runs,1],dtype = "<U8") #Initialize a string array for the hull type labels (necessary since numpy won't allow string to override the float if created as 1 array)
results = np.hstack((results1,results0)) #Build the storage array for results

cycle = 0 #For iterating steps

# Main Program Algorithm
for hulltype in hull_types: #Check Every Type of Hull

    for length in range(l_min,l_max+1,l_step): #Check all possible design lengths

        for beam in range(b_min, b_max+1, b_step): #check all possible beams

            for draft in range(t_min,t_max+1,t_step): #check all possible drafts

                stable, displacement = STB.CheckStability(hulltype,length,beam,draft,stabcriteria) #Performs a check of the stability for this specific hull design and calculates its displacement
                
                if(not stable): #if we find an unstable hull, don't proceed, skip to the next hull design
                    continue
                
                Downtime, SailingConditions = MF.CalculateMotions(hulltype,length,draft,Waves,max_vert_velocity) #Find the percentage of time the vessel is down and the conditions under which it would be allowed to sail
                
                for n in range(n_min,n_max+1,1): #for all possible fleet sizes
                    #Find the cost, average speed, and installed power required for this vessel arrangement
                    cost, designspeed, power = CC.CalculateCost(hulltype,length,beam,draft,displacement,n,Downtime,SailingConditions,StandbyShipRequired,field_distance,area_cargo,volume_cargo,deadweight_cargo,cycle_length,fuel_cost)
                    
                    print(cycle) #Feedback on result progress
                    
                    results[cycle] = [hulltype,n,length,beam,draft,designspeed,power,cost] #Reassign the results storage array to current result
                    
                    cycle += 1

print("Calculation Complete - View xxx.csv for table of results")

#TODO sort the np.array by lowest cost

table = np.vstack((["Hull Type","Number of Ships","Length","Beam","Draft","Design Speed","Power","Annual Cost"],results)) #Adds a header to the table

#TODO Write the sorted results to a csv file with headers