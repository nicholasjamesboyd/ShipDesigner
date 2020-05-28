import numpy as np

def CalculateMotions(hull_type, Length, Draft, Seas, MaxVelocity):
    if (hull_type == "Axe"):
        Motions = (0.24 - 0.0080*Length - 0.025*Draft + 0.12*Seas[:,0] + 0.11*Seas[:,1] - 0.00043*Length*Seas[:,0] + 0.0024*Draft*Seas[:,1] + 0.0075*Seas[:,0]*Seas[:,1] + 0.000032*Length**2 - 0.0071*Seas[:,0]**2 - 0.0063*Seas[:,1]**2)**2
        DownTime = np.size(Motions[Motions>MaxVelocity],0)/np.size(Seas,0)
        DownTime = round(DownTime,3)
        SailingIndices = Motions < MaxVelocity
        SailingConditions = Seas[SailingIndices,:]
        return DownTime, SailingConditions

    elif (hull_type == "X"):
        Motions = (-1.20 - 0.0036*Length + 0.093*Seas[:,0] + 0.68*Seas[:,1] - 0.002 * Length * Seas[:,1] + 0.0068 * Seas[:,0] * Seas[:,1] + 0.000036 * Length**2 - 0.0073*Seas[:,0]**2 - 0.064 * Seas[:,1]**2 + 0.00012 * Length * Seas[:,1]**2 + 0.0018 * Seas[:,1]**3)**2
        DownTime = np.size(Motions[Motions>MaxVelocity],0)/np.size(Seas,0)
        DownTime = round(DownTime,3)
        SailingIndices = Motions < MaxVelocity
        SailingConditions = Seas[SailingIndices,:]
        return DownTime, SailingConditions

    elif (hull_type == "Vertical"):
        Motions = (-1.11 + 0.0035 * Length + 0.031 * Seas[:,0] + 0.58 * Seas[:,1] - 0.0022 * Length * Seas[:,1] + 0.0072 * Seas[:,0] * Seas[:,1] - 0.053 * Seas[:,1]**2 + 0.00014 * Length * Seas[:,1]**2 + 0.0014 * Seas[:,1]**3)**2
        DownTime = np.size(Motions[Motions>MaxVelocity],0)/np.size(Seas,0)
        DownTime = round(DownTime,3)
        SailingIndices = Motions < MaxVelocity
        SailingConditions = Seas[SailingIndices,:]
        return DownTime, SailingConditions

    elif (hull_type == "Bulbous"):
        Motions = (0.58 - 0.014*Length - 0.12*Draft + 0.039 * Seas[:,0] + 0.25*Seas[:,1] - 0.000012*Length*Seas[:,1] + 0.033*Draft*Seas[:,1] + 0.0068*Seas[:,0]*Seas[:,1] + 0.000056*Length**2 - 0.037*Seas[:,1]**2 - 0.0019*Draft*Seas[:,1]**2 + 0.0018*Seas[:,1]**3)**2
        DownTime = np.size(Motions[Motions>MaxVelocity],0)/np.size(Seas,0)
        DownTime = round(DownTime,3)
        SailingIndices = Motions < MaxVelocity
        SailingConditions = Seas[SailingIndices,:]
        return DownTime, SailingConditions

    else:
        DownTime = 1.0
        SailingConditions = np.zeros((1,2))
    return DownTime, SailingConditions