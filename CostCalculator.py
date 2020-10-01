import math
import numpy as np

def CalculateCost(hull_type, length, beam, draft, displacement, n, downtime, sailingconditions, standby, distance, area, volume, cycle_length, fuel_cost,efficiency,designlife,seastates):
    runs = CalculateNumberDeliveries(length,beam,displacement,area,volume) #Find the number of required delivery runs

    designspeed, possible = CalculateRequiredSpeed(cycle_length,runs,downtime,distance,n,standby) #Determine the speed and if this vessel isn't impossibly fast
    if(not possible):
        return 0.0, designspeed, 0.0, possible

    power, fuel_annual_cost = CalculateFuelCost(hull_type,length,beam,draft,designspeed,sailingconditions,runs,distance,cycle_length,fuel_cost,efficiency) #Determine the total required engine power and fleet fuel costs
    
    Operating_Cost = CalculateOperatingCost(displacement, n) #Determine the cost of crewing required for this vessel
    
    buildcost, possible = CalculateBuildCost(hull_type, displacement, power) #Determine the cost to build and if this vessel's power plant and equipment are too heavy to be possible
    if(not possible):
        return 0.0, designspeed, 0.0, possible
    
    apr = 0.05 #Annual mortgage rate APR
    amortization = 12 * buildcost * n * (apr/12*(1+apr/12)**(designlife*12))/((1+apr/12)**(designlife*12)-1) #Amortize the build cost of the fleet over their life based on the interest rate
    
    station_keeping_cost = CalculateRequiredPositionKeeping(seastates,sailingconditions,beam,draft,standby,n,runs,cycle_length,fuel_cost,efficiency, displacement, length)
    
    cost = fuel_annual_cost + Operating_Cost + amortization + station_keeping_cost
    
    return cost, designspeed, power, possible

def CalculateOperatingCost(displacement, n): #Function To Find the Crewing Cost of each vessel
    officers = 12 #Number of Officers Per Ship
    ratings = 25 #Number of Non Officers Per Ship
    officer_rate = 105773 #Average Officer Salary
    rating_rate = 84288 #Average Crew Salary
    allowances = 706236 #Additional Crew Allowances
    
    crew_cost_per_ship = officers * officer_rate + ratings * rating_rate + allowances #Assign Crew Costs
    crew_cost = crew_cost_per_ship * n
    
    insurance_per_ship = (85.99 * (0.471 * displacement / 1000) ** 0.6942) * 365 * 2.57 #Calculate Insurance Costs
    insurance_costs = insurance_per_ship * n

    repair_per_ship = (105.4 * (0.471 * displacement / 1000) ** 0.6942) * 365 * 2.57 #Calculate Repair Costs
    repair_costs = repair_per_ship * n

    victuals_cost = 421480 #Assign Victuals Cost

    operating_cost = crew_cost + insurance_costs + repair_costs + victuals_cost
    
    return round(operating_cost,0)

def CalculateBuildCost(hull_type, displacement, power): #function to find the build cost of each vessel
    if (hull_type == "Axe"):
         lightship = 0.529 * displacement
         equip_weight = lightship * 0.128
         plant_weight = 0.0376 * power - 24.491
         if (plant_weight < 7.2):
             plant_weight = 7.2
         hull_weight = lightship - equip_weight - plant_weight
         if hull_weight <= 0: #If our other weights are too high then we should reject this vessel
             possible = False
             qs = 1994.663
             hull_weight = 0
         else:
             qs = 1994.663 + 0.015549 * hull_weight - 154.0222 * (hull_weight ** 0.2471932)
             possible = True
         qe = 9749.0427 + 14.66748 * equip_weight - 16.71265 * equip_weight ** 0.9963722
         qp = 16720.374 + 0.7839685 * plant_weight - 221.3641 * plant_weight ** 0.510682
         cost = round(qe * equip_weight + qp * plant_weight + qs * hull_weight,0)
         return cost, possible

    elif (hull_type == "X"):
         lightship = 0.529 * displacement
         equip_weight = lightship * 0.128
         plant_weight = 0.0376 * power -24.491
         if (plant_weight < 7.2):
             plant_weight = 7.2
         hull_weight = lightship - equip_weight - plant_weight
         if hull_weight <= 0: #If our other weights are too high then we should reject this vessel
             possible = False
             qs = 1994.663
             hull_weight = 0
         else:
             qs = 1994.663 + 0.015549 * hull_weight - 154.0222 * (hull_weight ** 0.2471932)
             possible = True
         qe = 9749.0427 + 14.66748 * equip_weight - 16.71265 * equip_weight ** 0.9963722
         qp = 16720.374 + 0.7839685 * plant_weight - 221.3641 * plant_weight ** 0.510682
         labour_cost_per_ton = qs - 500 #subtract the steel cost from the hull cost
         labour_costs = labour_cost_per_ton * hull_weight
         labour_costs *= 0.85
         cost = round(qe * equip_weight + qp * plant_weight + 500 * hull_weight + labour_costs,0)
         return cost, possible

    elif (hull_type == "Vertical"):
         lightship = 0.529 * displacement
         equip_weight = lightship * 0.128
         plant_weight = 0.0376 * power -24.491
         if (plant_weight < 7.2):
             plant_weight = 7.2
         hull_weight = lightship - equip_weight - plant_weight
         if hull_weight <= 0: #If our other weights are too high then we should reject this vessel
             possible = False
             qs = 1994.663
             hull_weight = 0
         else:
             qs = 1994.663 + 0.015549 * hull_weight - 154.0222 * (hull_weight ** 0.2471932)
             possible = True
         qe = 9749.0427 + 14.66748 * equip_weight - 16.71265 * equip_weight ** 0.9963722
         qp = 16720.374 + 0.7839685 * plant_weight - 221.3641 * plant_weight ** 0.510682
         cost = round(qe * equip_weight + qp * plant_weight + qs * hull_weight,0)
         return cost, possible

    elif (hull_type == "Bulbous"):
         lightship = 0.529 * displacement
         equip_weight = lightship * 0.128
         plant_weight = 0.0376 * power -24.491
         if (plant_weight < 7.2):
             plant_weight = 7.2
         hull_weight = lightship - equip_weight - plant_weight
         if hull_weight <= 0: #If our other weights are too high then we should reject this vessel
             possible = False
             qs = 1994.663
             hull_weight = 0
         else:
             qs = 1994.663 + 0.015549 * hull_weight - 154.0222 * (hull_weight ** 0.2471932)
             possible = True
         qe = 9749.0427 + 14.66748 * equip_weight - 16.71265 * equip_weight ** 0.9963722
         qp = 16720.374 + 0.7839685 * plant_weight - 221.3641 * plant_weight ** 0.510682
         cost = qe * equip_weight + qp * plant_weight + qs * hull_weight
         bulb_weight = displacement * 0.0138
         bulb_cost = (0.03395 * 0.55 * 2.292 * bulb_weight ** 0.772) * 1000000
         cost += bulb_cost
         cost = round(cost,0)
         return cost, possible

    else:
        return 0,False

def CalculateNumberDeliveries(length, beam, displacement, area, volume): #function to find the number of deliveries that need to be completed in a given cycle
    Area_Ratio = 0.41 #Ratio between vessel block area and usable cargo area
    Volume_Ratio = 0.376 #Ratio between the displacement and the bulk volume capacity
    Area_Capacity = length * beam * Area_Ratio
    Volume_Capacity = displacement * Volume_Ratio
    runs = max(area/Area_Capacity,volume/Volume_Capacity)
    runs = math.ceil(runs)
    return runs

def CalculateRequiredPositionKeeping(seastates, sailingconditions, beam, draft, standby, n, runs, cycle_length, fuel_cost, efficiency, displacement, length): #calculate the total fuel consumption holding position
    
    StandbyWind = 6.5327*seastates[:,0]**0.6549 #Finds wind speeds corresponding to sea states
   
    UnloadWind = 6.5327*sailingconditions[:,0]**0.6549 #Finds wind speeds corresponding to seas during unloading
    
    #Assign Currents based on waves
    StandbyCurrent = seastates[:,0]
    StandbyCurrent = np.where(StandbyCurrent<0.4,0.25,StandbyCurrent)
    StandbyCurrent = np.where((StandbyCurrent>=0.4) & (StandbyCurrent<0.8),0.5,StandbyCurrent)
    StandbyCurrent = np.where(StandbyCurrent>=0.8,0.75,StandbyCurrent)

    UnloadCurrent = sailingconditions[:,0]
    UnloadCurrent = np.where(UnloadCurrent<0.4,0.25,UnloadCurrent)
    UnloadCurrent = np.where((UnloadCurrent>=0.4) & (UnloadCurrent<0.8),0.5,UnloadCurrent)
    UnloadCurrent = np.where(UnloadCurrent>=0.8,0.75,UnloadCurrent)

    #Wind assumed to be bow on
    WindCoefficient = 0.423

    Depth = 1.333*draft + 9 #Hull depth at the bow, to account for a 2 deck forecastle structure and breakwater
    HullArea = (Depth-draft) * beam

    DeckhouseBeam = beam
    DeckhouseHeight = 9 #Accounts for normal of 3 decks above the top of focsle

    DeckhouseArea = DeckhouseBeam * DeckhouseHeight

    StandbyWindLoads = 0.5 * 0.001225 * StandbyWind **2 * WindCoefficient * HullArea #IMCA Hull Wind
    StandbyWindLoads += 0.000615 * 1 * 1.18 * DeckhouseArea * StandbyWind **2 #IMCA Deckhouse Wind

    UnloadWindLoads = 0.5 * 0.001225 * UnloadWind **2 * WindCoefficient * HullArea
    UnloadWindLoads += 0.000615 * 1 * 1.18 * DeckhouseArea * UnloadWind **2

    CurrentFactor = 0.07 #Current coefficient for supply ships at 0 deg incidence current

    StandbyCurrentLoads = 0.5 * 1.025 * StandbyCurrent ** 2 * beam * draft * CurrentFactor #Formula to derive the loading acting due to current in all cases
    UnloadCurrentLoads = 0.5 * 1.025 * UnloadCurrent ** 2 * beam * draft * CurrentFactor
   
    StandbyTsurge = seastates[:,1] / (0.9 * length ** (1/3)) #From DNV calculation for dynamic positioning loads
    UnloadTSurge = sailingconditions[:,1] / (0.9 * length ** (1/3))

    FStandbyTSurge = np.where(StandbyTsurge < 1, 1, StandbyTsurge ** (-3) * np.exp(1 - StandbyTsurge ** (-3))) #From DNV Calculation
    FUnloadTSurge = np.where(UnloadTSurge < 1, 1, UnloadTSurge ** (-3) * np.exp(1 - UnloadTSurge ** (-3)))

    StandbyWaveLoads = 0.5 * 1.025 * 9.81 * seastates[:,0] ** 2 * beam * 0.0628 * FStandbyTSurge #From DNV Calculation
    UnloadWaveLoads = 0.5 * 1.025 * 9.81 * sailingconditions[:,0] ** 2 * beam * 0.0628 * FUnloadTSurge

    StandbyTotalLoads = StandbyWindLoads + StandbyCurrentLoads +  StandbyWaveLoads #Combine all station keepign loads
    UnloadTotalLoads = UnloadWindLoads + UnloadCurrentLoads + UnloadWaveLoads

    StandbyAverageLoad = np.mean(StandbyTotalLoads) #Find the average requirement across all sea states
    UnloadAverageLoad = np.mean(UnloadTotalLoads)

    ThrusterEfficiency = 0.10 #Efficiency of propellor to thrust in kN/kw power including mechanical losses and flow losses

    StandbyPower = StandbyAverageLoad / ThrusterEfficiency #Get the power requirements to maintain this position
    UnloadPower = UnloadAverageLoad / ThrusterEfficiency

    StandbyFuel = StandbyPower * cycle_length * efficiency / 1000000
    UnloadFuel = UnloadPower * runs * 8 * efficiency/ 1000000

    StandbyCost = StandbyFuel * fuel_cost
    UnloadCost = UnloadFuel * fuel_cost

    if (standby):
        return round((StandbyCost + UnloadCost) * 8760 / cycle_length,0)
    else:
        return round(UnloadCost * 8760 / cycle_length,0)

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
    voyage_time = sailing_time - number_deliveries * time_to_unload #Unloading is only done if we are in the weather window
    hours_per_sail = voyage_time / number_deliveries
    
    if hours_per_sail <= 0:
        possible = False
        speed = 0.0
    
    else:
        speed = 2 * distance / hours_per_sail #Speed needs to be doubled to allow time for ship to return to port
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
        power = round(average_resistance * speed * 0.5144,0) #Effective Power

        # Power Efficiency Losses
        QPC = 0.55 #Quasi Propulsive Coefficient accounts for and propellor efficiency
        Eta_g = 0.95 #Gearbox Losses 
        Eta_s = 0.98 #Shaft Losses
        Eta_sw = 0.998 #Switchboard Losses
        Eta_fc = 0.985 #Frequency Convertor Losses
        Eta_motor = 0.97 #Electric Motor Efficiency

        power = power / (QPC * Eta_g * Eta_s * Eta_sw * Eta_fc * Eta_motor) #Required Generator Power

        fuel_cost_per_run = power * 2 * distance/speed * efficiency * fuel_cost / 1000000
        cost_per_cycle = runs * fuel_cost_per_run
        fuel_annual_cost = round(8760 / cycle_length * cost_per_cycle,0)
        return power, fuel_annual_cost

    elif (hull_type == "X"):
        all_resistance = 10 ** (-2.68 - 0.0033*length + 0.025*beam + 0.71*draft + 0.034*sailing_conditions[:,0] + 0.68*sailing_conditions[:,1] + 0.067*speed - 0.00013 * length * speed - 0.11*draft*sailing_conditions[:,1] - 0.029 * sailing_conditions[:,1]**2 + 0.0047*draft*sailing_conditions[:,1]**2)
        average_resistance = np.mean(all_resistance)
        power = round(average_resistance * speed * 0.5144,0)

        # Power Efficiency Losses
        QPC = 0.55 #Quasi Propulsive Coefficient accounts for and propellor efficiency
        Eta_g = 0.95 #Gearbox Losses 
        Eta_s = 0.98 #Shaft Losses
        Eta_sw = 0.998 #Switchboard Losses
        Eta_fc = 0.985 #Frequency Convertor Losses
        Eta_motor = 0.97 #Electric Motor Efficiency

        power = power / (QPC * Eta_g * Eta_s * Eta_sw * Eta_fc * Eta_motor) #Required Generator Power

        fuel_cost_per_run = power * 2*distance/speed * efficiency * fuel_cost / 1000000
        cost_per_cycle = runs * fuel_cost_per_run
        fuel_annual_cost = round(8760 / cycle_length * cost_per_cycle,0)
        return power, fuel_annual_cost

    elif (hull_type == "Vertical"):
        all_resistance = 10 ** (-4.62 - 0.011*length - 0.056*beam + 1.22*draft + 0.10*sailing_conditions[:,0] + 1.22*sailing_conditions[:,1] + 0.054 * speed + 0.00022*length*beam - 0.20*draft*sailing_conditions[:,1] - 0.0049*sailing_conditions[:,0]*sailing_conditions[:,1] + 0.0015*beam**2 - 0.05*sailing_conditions[:,1]**2 + 0.0082*draft*sailing_conditions[:,1]**2)
        average_resistance = np.mean(all_resistance)
        power = round(average_resistance * speed * 0.5144,0)
        
        # Power Efficiency Losses
        QPC = 0.55 #Quasi Propulsive Coefficient accounts for and propellor efficiency
        Eta_g = 0.95 #Gearbox Losses 
        Eta_s = 0.98 #Shaft Losses
        Eta_sw = 0.998 #Switchboard Losses
        Eta_fc = 0.985 #Frequency Convertor Losses
        Eta_motor = 0.97 #Electric Motor Efficiency        

        fuel_cost_per_run = power * 2 * distance/speed * efficiency * fuel_cost / 1000000
        cost_per_cycle = runs * fuel_cost_per_run
        fuel_annual_cost = round(8760 / cycle_length * cost_per_cycle,0)
        return power, fuel_annual_cost

    elif (hull_type == "Bulbous"):
        all_resistance = 10 ** (-0.91 + 0.01*length + 0.023*beam + 0.2*draft + 0.032*sailing_conditions[:,0] + 0.14*speed - 0.0013 * length * draft - 0.00034 * length * speed - 0.00063 * speed ** 2)
        average_resistance = np.mean(all_resistance)
        power = round(average_resistance * speed * 0.5144,0)
        
        # Power Efficiency Losses
        QPC = 0.55 #Quasi Propulsive Coefficient accounts for and propellor efficiency
        Eta_g = 0.95 #Gearbox Losses 
        Eta_s = 0.98 #Shaft Losses
        Eta_sw = 0.998 #Switchboard Losses
        Eta_fc = 0.985 #Frequency Convertor Losses
        Eta_motor = 0.97 #Electric Motor Efficiency        
        
        fuel_cost_per_run = power * 2 * distance/speed * efficiency * fuel_cost / 1000000
        cost_per_cycle = runs * fuel_cost_per_run
        fuel_annual_cost = round(8760 / cycle_length * cost_per_cycle,0)
        return power, fuel_annual_cost

    else:
        power = 0.0
        fuel_annual_cost = 0.0
        return power, fuel_annual_cost