import math

def CheckStability(hull_type, length, beam, draft, stabcriteria):
    if (hull_type == "Axe"):
            BM = 10**(0.51 + 0.085*beam -0.15*draft - 0.0010*beam**2 + 0.0064*draft**2)
            KB = 0.81725 * draft
            KG = 0.8 * draft * 1.839
            if (KB + BM - KG < stabcriteria):
                return False, 0.0
            displacement = math.floor(1939.90 - 22.79*length - 97.31*beam - 340.17*draft + 1.11*length*beam + 3.88*length*draft + 16.62*beam*draft)
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
            BM = 10**(0.16 + 0.085*beam -0.15*draft - 0.0010*beam**2 + 0.0064*draft**2)
            KB = 0.5505 * draft
            KG = 0.8 * draft * 1.333333
            if (KB + BM - KG < stabcriteria):
                return False, 0.0
            displacement = math.floor(7387.42 - 86.80*length - 370.59*beam - 1295.41*draft + 4.23*length*beam + 14.76*length*draft + 63.28*beam*draft)
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
            BM = 10**(0.15 + 0.085*beam -0.15*draft - 0.0010*beam**2 + 0.0064*draft**2)
            KB = 0.55225 * draft
            KG = 0.8 * draft * 1.333333
            if (KB + BM - KG < stabcriteria):
                return False, 0.0
            displacement = math.floor(7564.22 - 88.87*length - 379.46*beam - 1326.42*draft + 4.33*length*beam + 15.11*length*draft + 64.79*beam*draft)
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
            BM = 10**(0.15 + 0.085*beam -0.15*draft - 0.0010*beam**2 + 0.0064*draft**2)
            KB = 0.5584 * draft
            KG = 0.8 * draft * 1.333333
            if (KB + BM - KG < stabcriteria):
                return False, 0.0
            displacement = math.floor(7669.85 - 90.12*length - 384.76*beam - 1344.94*draft + 4.39*length*beam + 15.32*length*draft + 65.70*beam*draft)
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