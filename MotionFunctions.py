import numpy as np

def CalculateMotions(hull_type, Length, Beam, Draft, Seas, MaxVelocity):
    if (hull_type == "Axe"):
        Motions = (0.24 - 0.0080*Length - 0.025*Draft + 0.12*Seas[:,0] + 0.11*Seas[:,1] - 0.00043*Length*Seas[:,0] + 0.0024*Draft*Seas[:,1] + 0.0075*Seas[:,0]*Seas[:,1] + 0.000032*Length**2 - 0.0071*Seas[:,0]**2 - 0.0063*Seas[:,1]**2)**2
        DownTime = np.size(Motions[Motions>MaxVelocity],0)/np.size(Seas,0)
        DownTime = round(Downtime,3)
        SailingIndices = Motions < MaxVelocity
        SailingConditions = Seas[SailingIndices,:]
        return DownTime, SailingConditions

    elif (hull_type == "X"):
        Motions = 0.0 #TODO Define
        DownTime = np.size(Motions[Motions>MaxVelocity],0)/np.size(Seas,0)
        DownTime = round(Downtime,3)        
        SailingIndices = Motions < MaxVelocity
        SailingConditions = Seas[SailingIndices,:]
        return DownTime, SailingConditions

    elif (hull_type == "Vertical"):
        Motions = 0.0 #TODO Define
        DownTime = np.size(Motions[Motions>MaxVelocity],0)/np.size(Seas,0)
        DownTime = round(Downtime,3)        
        SailingIndices = Motions < MaxVelocity
        SailingConditions = Seas[SailingIndices,:]
        return DownTime, SailingConditions

    elif (hull_type == "Bulbous"):
        Motions = 0.0 #TODO Define
        DownTime = np.size(Motions[Motions>MaxVelocity],0)/np.size(Seas,0)
        DownTime = round(Downtime,3)        
        SailingIndices = Motions < MaxVelocity
        SailingConditions = Seas[SailingIndices,:]
        return DownTime, SailingConditions

    else:
        DownTime = 1.0
        SailingConditions = np.zeros((1,2))
    return DownTime, SailingConditions