from MotionFunctions import MotionFunctions as MF

class CostCalculator():

    def findAxeCost():
        sailing_conditions, exceedance = MF.axeMotion()
        print(sailing_conditions)
        print(exceedance)

    def findXCost():
        sailing_conditions, exceedance = MF.xMotion()
        print(sailing_conditions)
        print(exceedance)

    def findVertCost():
        sailing_conditions, exceedance = MF.vertMotion()
        print(sailing_conditions)
        print(exceedance)

    def findBulbCost():
        sailing_conditions, exceedance = MF.bulbMotion()
        print(sailing_conditions)
        print(exceedance)

