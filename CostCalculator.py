def CalculateCost(hull_type, length, beam, draft, displacement, n, downtime, sailingconditions, standby, distance, area, volume, deadweight, cycle_length, fuel_cost):
    cost = 0.0
    designspeed = 0.0
    power = 0.0
    return cost, designspeed, power

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
    pass

def CalculateRequiredPositionKeeping(length, beam, draft, displacement, number_deliveries, standby, cycle_length): #calculate the total fuel consumption holding position
    pass

def CalculateRequiredSpeed(cycle_length,number_deliveries,downtime,distance,n,standby): #calculate the required speed for delivery
    pass

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