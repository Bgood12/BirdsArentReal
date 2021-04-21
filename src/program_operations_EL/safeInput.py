
"""
This class is designed to clean up commandParser.py by doing error handling for user inputs
"""

def getFloatPositive(minValue, maxValue, prompt):
    flt = -1
    inStr = "ya-yeet"
    # in the event the min and max are the same, it is assumed there is no dev-imposed maximum
    while flt < minValue or (flt > maxValue and minValue != maxValue):
        try:
            inStr = input(prompt)
            flt = float(inStr)
        except ValueError:
            print(inStr + " is not a value between " + str(minValue) + " and " + str(maxValue))
    return flt


def getIntPositive(prompt):
    intgr = -1
    inStr = "ya-yeet"
    while intgr < 0:
        try:
            inStr = input(prompt)
            intgr = int(inStr)
        except ValueError:
            print(inStr + " is not a valid positive integer")
    return intgr

def getValidDifficulty(prompt):
    dif = 'very_medium'  # the most premium difficulty
    while not (dif == 'very_easy' or dif == 'easy' or dif == 'medium' or dif == 'hard' or dif == 'very_hard'):
        dif = input(prompt)
    return dif