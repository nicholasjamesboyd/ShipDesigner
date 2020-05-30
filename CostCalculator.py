import math
import numpy as np

def CalculateCost(hull_type, length, beam, draft, displacement, n, downtime, sailingconditions, standby, distance, area, volume, deadweight, cycle_length, fuel_cost,efficiency):
    runs = CalculateNumberDeliveries(length,beam,displacement,area,volume,deadweight)
    designspeed, possible = CalculateRequiredSpeed(cycle_length,runs,downtime,distance,n,standby)
    if(not possible):
        return 0.0, designspeed, 0.0, possible
    power, fuel_annual_cost = CalculateFuelCost(hull_type,length,beam,draft,designspeed,sailingconditions,runs,distance,cycle_length,fuel_cost,efficiency)
    crew_cost = 0.0
    amortization = 0.0
    station_keeping_cost = 0.0
    cost = fuel_annual_cost + crew_cost + amortization + station_keeping_cost
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
        if speed > 30.0: #Reject vessels that require impossibly fast designs
            possible = False
        speed = math.ceil(speed)
    return speed, possible

def CalculateFuelCost(hull_type,length,beam,draft,speed,sailing_conditions,runs,distance,cycle_length,fuel_cost,efficiency): #Calculates the fuel cost for the vessel
    if (hull_type == "Axe"):
        all_resistance = 10 ** (-0.15 - 0.0077*length + 0.021*beam + 0.25*draft + 0.15 * sailing_conditions[:,0] + 0.095 * speed - 0.0018*length*draft + 0.000086 * length ** 2 - 0.019 * sailing_conditions[:,0] ** 2 - 0.00091 * speed ** 2)
        average_resistance = np.mean(all_resistance)
        power = round(average_resistance * speed * 0.5144,0)
        fuel_cost_per_run = power * distance/speed * efficiency * fuel_cost / 1000000
        cost_per_cycle = runs * fuel_cost_per_run
        fuel_annual_cost = round(8760 / cycle_length * cost_per_cycle,0)
        return power, fuel_annual_cost

    elif (hull_type == "X"):
        all_resistance = 10 ** (-2.68 - 0.0033*length + 0.025*beam + 0.71*draft + 0.034*sailing_conditions[:,0] + 0.68*sailing_conditions[:,1] + 0.067*speed - 0.00013 * length * speed - 0.11*draft*sailing_conditions[:,1] - 0.029 * sailing_conditions[:,1]**2 + 0.0047*draft*sailing_conditions[:,1])
        average_resistance = np.mean(all_resistance)
        power = round(average_resistance * speed * 0.5144,0)
        fuel_cost_per_run = power * distance/speed * efficiency * fuel_cost / 1000000
        cost_per_cycle = runs * fuel_cost_per_run
        fuel_annual_cost = round(8760 / cycle_length * cost_per_cycle,0)
        return power, fuel_annual_cost

    elif (hull_type == "Vertical"):
        all_resistance = 10 ** (-4.62 - 0.011*length - 0.056*beam + 1.22*draft + 0.10*sailing_conditions[:,0] + 1.22*sailing_conditions[:,1] + 0.054 * speed + 0.00022*length*beam - 0.20*draft*sailing_conditions[:,1] - 0.0049*sailing_conditions[:,0]*sailing_conditions[:,1] + 0.0015*beam**2 - 0.05*sailing_conditions[:,1]**2 + 0.0082*draft*sailing_conditions[:,1]**2)
        average_resistance = np.mean(all_resistance)
        power = round(average_resistance * speed * 0.5144,0)
        fuel_cost_per_run = power * distance/speed * efficiency * fuel_cost / 1000000
        cost_per_cycle = runs * fuel_cost_per_run
        fuel_annual_cost = round(8760 / cycle_length * cost_per_cycle,0)
        return power, fuel_annual_cost

    elif (hull_type == "Bulbous"):
        all_resistance = 10 ** (-0.91 + 0.01*length + 0.023*beam + 0.2*draft + 0.032*sailing_conditions[:,0] + 0.14*speed - 0.0013 * length * draft - 0.00034 * length * speed - 0.00063 * speed ** 2)
        average_resistance = np.mean(all_resistance)
        power = round(average_resistance * speed * 0.5144,0)
        fuel_cost_per_run = power * distance/speed * efficiency * fuel_cost / 1000000
        cost_per_cycle = runs * fuel_cost_per_run
        fuel_annual_cost = round(8760 / cycle_length * cost_per_cycle,0)
        return power, fuel_annual_cost

    else:
        power = 0.0
        fuel_annual_cost = 0.0
        return power, fuel_annual_cost