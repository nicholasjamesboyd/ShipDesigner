#Declare required components
import numpy as np
import math
import MotionFunctions as MF
import CostCalculator as CC
import StabilityCheck as STB

def CalculateRuns(hulltypes,lmin,lmax,lstep,bmin,bmax,bstep,tmin,tmax,tstep,nmin,nmax): #calculate all the runs we need so we can initialize an appropriate numpy array, add 1 to account for the first value
    lruns = math.floor((lmax-lmin)/lstep)+1
    bruns = math.floor((bmax-bmin)/bstep)+1
    truns = math.floor((tmax-tmin)/tstep)+1
    hullruns = len(hulltypes)
    nruns = nmax - nmin + 1
    return lruns*bruns*truns*hullruns*nruns

#Enter Sea Parameters
mu = 2.458 #Gumbel Mu Parameter for Wave Height
beta = 1.101 #Gumbel Beta Parameter for Wave Height
tmean = 10.05 #mean wave period
tdeviation = 2.008 #wave period standard deviation

h = np.zeros([73000,1]) #Intialize a numpy array for wave heights
t = np.zeros([73000,1]) #Initialize a numpy array for periods

for i in range(73000): #Generates a random significant wave height for 25 years of 3 hour seas
    h[i] = np.random.gumbel(mu, beta)
    t[i] = np.random.normal(tmean,tdeviation)
    while h[i] > t[i] - 2: #If We have an impossible sea state keep generating numbers till it works
        h[i] = np.random.gumbel(mu, beta)
        t[i] = np.random.normal(tmean,tdeviation)

h = np.where(h < 0, 0, h)

t = np.where(t<0,0,t)

Waves = np.hstack((h,t)) #Builds an array for each sea, each row is a significant wave height and peak period

#Enter Operational Parameters
field_distance = 250.0 #Distance in nautical miles
area_cargo = 1006.0 #Total deck area of cargo delivered per cycle m^2
volume_cargo = 2071.0 #Total bulk volument of cargo per cycle m^3
max_vert_velocity = 0.6 #Maximum tolerable vertical velocity for which the cargo operations can occur m/s
cycle_length = 72 #Length of a cargo cycle in hours
StandbyShipRequired = True #Is a ship required for standby
fuel_cost = 423 #Fuel cost is dollars/mt
engine_efficiency = 190 #Engine fuel efficiency in g/kwh

#Enter Design Limits
l_min = 60 #minimum length considered in m
l_max = 120 #maximum length considered in m
l_step = 5 #length stepping for design cases in m
b_min = 15 #minimum beam considered in m
b_max = 25 #maximum beam considered in m
b_step = 2 #beam stepping for design cases in m
t_min = 4 #minimum draft considered in m
t_max = 8 #maximum draft considered in m
t_step = 1 #draft stepping for design cases in m
n_max = 6 #Maximum fleet size considered
stabcriteria = 1.0 #Minimum GM value to be considered stable
designlife = 25 #Design Life of Ship in Years

if (StandbyShipRequired): #If a ship is required to be on standby we cannot have less than 2 ships
    n_min = 2
else:
    n_min = 1

hull_types = ["Axe", "X", "Vertical", "Bulbous"]

runs = CalculateRuns(hull_types,l_min,l_max,l_step,b_min,b_max,b_step,t_min,t_max,t_step,n_min,n_max)

results_table = np.zeros([runs,8]) #Initialize Array

cycle = 0 #For iterating steps

for hulltype in hull_types: #Check Every Type of Hull

    for length in range(l_min,l_max+1,l_step): #Check all possible design lengths

        for beam in range(b_min, b_max+1, b_step): #check all possible beams

            for draft in range(t_min,t_max+1,t_step): #check all possible drafts

                stable, displacement = STB.CheckStability(hulltype,length,beam,draft,stabcriteria) #Performs a check of the stability and freeboard for this specific hull design and calculates its displacement
                
                if(not stable): #if we find an unstable or not loadline compliant hull, don't proceed, skip to the next hull design
                    continue
                
                Downtime, SailingConditions = MF.CalculateMotions(hulltype,length,draft,Waves,max_vert_velocity) #Find the percentage of time the vessel is down and the conditions under which it would be allowed to sail
                
                for n in range(n_min,n_max+1,1): #for all possible fleet sizes
                    #Find the cost, average speed, and installed power required for this vessel arrangement
                    cost, designspeed, power, possible = CC.CalculateCost(hulltype,length,beam,draft,displacement,n,Downtime,SailingConditions,StandbyShipRequired,field_distance,area_cargo,volume_cargo,cycle_length,fuel_cost,engine_efficiency,designlife, Waves)
                    if (not possible): #If this is an impossible design, break the current iteration
                        continue
                    print(cycle) #Feedback on result progress
                    
                    results_table[cycle,:] = [hull_types.index(hulltype),n,length,beam,draft,designspeed,power,cost] #Reassign the results storage array to current result
                    
                    cycle += 1

results_table = np.delete(results_table,range(cycle,runs),axis=0) #Remove empty rows

results_table = results_table[np.argsort(results_table[:,7])] #Sort by the total annual cost

np.savetxt('FleetDesigns.csv',results_table,fmt = '%f', delimiter = ',', header = 'HullType,Number,Length,Beam,Draft,Speed,Power,AnnualCost') #Write the datatable to a csv file
print("Calculation Complete - View FleetDesigns.csv for table of results")