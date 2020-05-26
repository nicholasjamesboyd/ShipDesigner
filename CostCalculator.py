def CalculateCost(hull_type, length, beam, draft, displacement, n, downtime, sailingconditions, standby, distance, area, volume, deadweight, cycle_length):

    if (hull_type == "Axe"):
        cost = 0.0
        designspeed = 0.0
        power = 0.0
        return cost, designspeed, power

    elif (hull_type == "X"):
        cost = 0.0
        designspeed = 0.0
        power = 0.0
        return cost, designspeed, power

    elif (hull_type == "Vertical"):
        cost = 0.0
        designspeed = 0.0
        power = 0.0
        return cost, designspeed, power

    elif (hull_type == "Bulbous"):
        cost = 0.0
        designspeed = 0.0
        power = 0.0
        return cost, designspeed, power

    else:
        cost = 0.0
        designspeed = 0.0
        power = 0.0
        return cost, designspeed, power

def CalculateCrewCost(length, beam, draft): #Function To Find the Crewing Cost of each vessel
    pass

def CalculateBuildCost(hull_type, length, beam, draft): #function to find the build cost of each vessel
    pass

def CalculateNumberDeliveries(length, beam, displacement, area, volume, deadweight): #function to find the number of deliveries that need to be completed in a given cycle
    pass

def CalculateRequiredPositionKeeping(length, beam, draft, displacement, number_deliveries, standby, cycle_length): #calculate the total fuel consumption holding position
    pass

def CalculateRequiredSpeed(cycle_length,number_deliveries,downtime,distance,n,standby): #calculate the required speed for delivery
    pass