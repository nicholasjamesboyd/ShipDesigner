import math

def CheckStability(hull_type, length, beam, draft, stabcriteria):
    if (hull_type == "Axe"):
            BM = 10**(0.49 + 0.088*beam -0.15*draft - 0.0011*beam**2 + 0.0065*draft**2)
            KB = 0.81725 * draft
            KG = 0.8 * draft * 1.839
            if (KB + BM - KG < stabcriteria):
                return False, 0.0
            displacement = math.floor(1860.05 - 22.78*length - 97.21*beam - 325.45*draft + 1.11*length*beam + 3.70*length*draft + 16.61*beam*draft)
            tabular_freeboard = 0.0000849*length**2 + 0.00352*length + 0.06108 #Formula approximating loadling table
            if (displacement/1.025 > 0.68*length*beam*draft): #correction for displacement
                tabular_freeboard *= ((displacement/1.025)/(length*beam*draft) + 0.68)/1.36
            depth = draft*1.838
            if (depth > length/15):
                tabular_freeboard += ((depth - length/15)*length/0.48)/1000
            if (depth - draft < tabular_freeboard):
                return False, displacement
            return True, displacement

    elif (hull_type == "X"):
            BM = 10**(0.13 + 0.088*beam -0.15*draft - 0.0011*beam**2 + 0.0064*draft**2)
            KB = 0.5505 * draft
            KG = 0.8 * draft * 1.333333
            if (KB + BM - KG < stabcriteria):
                return False, 0.0
            displacement = math.floor(7086.32 - 83.04*length - 369.82*beam - 1239.96*draft + 4.22*length*beam + 14.09*length*draft + 63.23*beam*draft)
            tabular_freeboard = 0.0000849*length**2 + 0.00352*length + 0.06108 #Formula approximating loadling table
            if (displacement/1.025 > 0.68*length*beam*draft): #correction for displacement
                tabular_freeboard *= ((displacement/1.025)/(length*beam*draft) + 0.68)/1.36
            depth = draft*1.333
            if (depth > length/15):
                tabular_freeboard += ((depth - length/15)*length/0.48)/1000
            if (depth - draft < tabular_freeboard):
                return False, displacement
            return True, displacement

    elif (hull_type == "Vertical"):
            BM = 10**(0.13 + 0.088*beam -0.15*draft - 0.0011*beam**2 + 0.0064*draft**2)
            KB = 0.55225 * draft
            KG = 0.8 * draft * 1.333333
            if (KB + BM - KG < stabcriteria):
                return False, 0.0
            displacement = math.floor(7253.76 - 84.99*length - 378.88*beam - 1268.95*draft + 4.32*length*beam + 14.42*length*draft + 64.75*beam*draft)
            tabular_freeboard = 0.0000849*length**2 + 0.00352*length + 0.06108 #Formula approximating loadling table
            if (displacement/1.025 > 0.68*length*beam*draft): #correction for displacement
                tabular_freeboard *= ((displacement/1.025)/(length*beam*draft) + 0.68)/1.36
            depth = draft*1.333
            if (depth > length/15):
                tabular_freeboard += ((depth - length/15)*length/0.48)/1000
            if (depth - draft < tabular_freeboard):
                return False, displacement
            return True, displacement

    elif (hull_type == "Bulbous"):
            BM = 10**(0.12 + 0.088*beam -0.15*draft - 0.0011*beam**2 + 0.0064*draft**2)
            KB = 0.5584 * draft
            KG = 0.8 * draft * 1.333333
            if (KB + BM - KG < stabcriteria):
                return False, 0.0
            displacement = math.floor(7358.70 - 86.22*length - 384.20*beam - 1287.21*draft + 4.39*length*beam + 14.63*length*draft + 65.66*beam*draft)
            tabular_freeboard = 0.0000849*length**2 + 0.00352*length + 0.06108 #Formula approximating loadling table
            if (displacement/1.025 > 0.68*length*beam*draft): #correction for displacement
                tabular_freeboard *= ((displacement/1.025)/(length*beam*draft) + 0.68)/1.36
            depth = draft*1.333
            if (depth > length/15):
                tabular_freeboard += ((depth - length/15)*length/0.48)/1000
            if (depth - draft < tabular_freeboard):
                return False, displacement
            return True, displacement
    else:
            return False, 0.0