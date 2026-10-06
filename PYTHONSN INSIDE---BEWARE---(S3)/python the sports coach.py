# Python the sports coach
teamA = []
teamB = []
pointsA = 0
pointsB = 0
def most_points(pointsA,pointsB):
    if pointsA > pointsB:
        return "Team A win!"
    elif pointsB > pointsA:
        return "Team B win!"
    else:
        return "It's a draw!"
heightA = float(input("Student from TeamA,input your height"))