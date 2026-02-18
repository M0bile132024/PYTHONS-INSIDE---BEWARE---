# Whitebaord Activity
# 1.Valid aging
def valid_aging(age):
    '''Program that validates a positive age and loop until it has got it'''
    global INVALID
    try:
        age = int(age)
    except:
        INVALID = True
        return "That is not an option..."
    if age > 0:
        INVALID = False
        return "SUCCESS"
    else:
        INVALID = True
        return "That is not an option..."
INVALID = True
while INVALID:
    AGE = input("Give me an ageeeeeeee.....:")
    print(valid_aging(AGE))