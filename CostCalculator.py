import math

def CalculateCost(hull_type, length, beam, draft, displacement, n, downtime, sailingconditions, standby, distance, area, volume, deadweight, cycle_length, fuel_cost):
    runs = CalculateNumberDeliveries(length,beam,displacement,area,volume,deadweight)
    designspeed, possible = CalculateRequiredSpeed(cycle_length,runs,downtime,distance,n,standby)
    cost = 0.0
    power = 0.0
    return cost, designspeed, power, possible

def CalculateCrewCost(length, beam, draft): #Function To Find the Crewing Cost of each vessel
    pass

def CalculateBuildCost(hull_type, length, beam, draft): #function to find the build cost of each vessel
    if (hull_type == "Axe"):
        pass

    elif (hull_type == "X"):
        pass

    elif (hull_type == "Vertical"):
        pass

    elif (hull_type == "Bulbous"):
        pass

    else:
        pass

def CalculateNumberDeliveries(length, beam, displacement, area, volume, deadweight): #function to find the number of deliveries that need to be completed in a given cycle
    Area_Ratio = 0.5 #Ratio between vessel block area and usable cargo area
    Volume_Ratio = 0.5 #Ratio between the displacement and the bulk volume capacity
    Weight_Ratio = 0.75 #Ratio between the deadweight capacity and total displacement
    Area_Capacity = length * beam * Area_Ratio
    Volume_Capacity = displacement * Volume_Ratio
    Weight_Capacity = displacement * Weight_Ratio
    runs = max(area/Area_Capacity,volume/Volume_Capacity,deadweight/Weight_Capacity)
    runs = math.ceil(runs)
    return runs

def CalculateRequiredPositionKeeping(length, beam, draft, displacement, number_deliveries, standby, cycle_length): #calculate the total fuel consumption holding position
    pass

def CalculateRequiredSpeed(cycle_length,number_deliveries,downtime,distance,n,standby): #calculate the required speed for delivery
    time_to_load = 8 #time required to load up the vessel in hours
    time_to_unload = 8 #time required to unload cargo offshore
    total_time = cycle_length * n
    if standby:
        available_time = total_time - cycle_length
    else:
        available_time = total_time
    loading_time = number_deliveries * time_to_load
    net_time = available_time - loading_time
    sailing_time = (1-downtime) * net_time
    voyage_time = sailing_time - number_deliveries * time_to_unload
    hours_per_sail = voyage_time / number_deliveries
    if hours_per_sail <= 0:
        possible = False
        speed = 0.0
    else:
        speed = distance / hours_per_sail
        possible = True
        if speed < 10.0: #If lots of time is available, the speed doesnt need to be fast, but we still would not design a vessel for less than 10 knots, ships would simply spend more time in port
            speed = 10.0
        if speed > 40.0: #Reject vessels that require impossibly fast designs
            possible = False
        speed = math.ceil(speed)
    return speed, possible

def CalculateFuelCost(hull_type,length,beam,draft,speed,sailing_conditions,runs,distance,cycle_length,fuel_cost): #Calculates the fuel cost for the vessel
    if (hull_type == "Axe"):
        pass

    elif (hull_type == "X"):
        pass

    elif (hull_type == "Vertical"):
        pass

    elif (hull_type == "Bulbous"):
        pass

    else:
        pass