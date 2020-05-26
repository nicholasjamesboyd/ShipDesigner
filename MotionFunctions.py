import numpy as np

def CalculateMotions(hull_type, Length, Beam, Draft, Seas, MaxVelocity):
    if (hull_type == "Axe"):
        Motions = []
        DownTime = 0.0
        SailingConditions = []
        return DownTime, SailingConditions

    elif (hull_type == "X"):
        Motions = []
        DownTime = 0.0
        SailingConditions = []
        return DownTime, SailingConditions

    elif (hull_type == "Vertical"):
        Motions = []
        DownTime = 0.0
        SailingConditions = []
        return DownTime, SailingConditions

    elif (hull_type == "Bulbous"):
        Motions = []
        DownTime = 0.0
        SailingConditions = []
        return DownTime, SailingConditions

    else:
        DownTime = 1.0
        SailingConditions = []
    return DownTime, SailingConditions