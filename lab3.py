import math

g = 9.80665
h = 1
#R data from experiment
data = {
    "R0": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    # angle      15      30      45      60      75       [min,max]
    "R15-75": [[1, 10],[1, 10],[1, 10],[1, 10],[1, 10]]
}
R0_average= sum(data["R0"])/len(data["R0"])
v0=R0_average*math.sqrt(g/2/h)
# theoretical_R=[R15,R30,R45,R60,R75]
theoretical_R=[v0**2*math.sin(math.radians((x + 1)*15*2))/2/g*(1+math.sqrt(1+2*g*h/v0**2/math.sin(math.radians((x + 1)*15))**2)) for x in range(5)]
print("R0_average=",R0_average)
print("v0=",v0)

# print([(x + 1)*15 for x in range(5)])
# print([math.sin(math.radians((x + 1)*15*2)) for x in range(5)])
# print([(x + 1)*15*2 for x in range(5)])
# print(theoretical_R)
for x in range(5):
    angle = (x + 1)*15
    print("R",angle,"=",theoretical_R[x],"theoretical")

best_angle=math.degrees(math.atan(1/math.sqrt(1+2*g*h/v0**2)))
print("best_angle=",best_angle)
R_max = v0**2/g*math.sqrt(1+2*g*h/v0**2)
print("R_max=",R_max)
R_experimental = [(x[0]+x[1])/2 for x in data["R15-75"]]
for x in range(5):
    angle = (x + 1)*15
    print("R",angle,"=",R_experimental[x],"experimental")
R_uncertainty_experimental = [(x[1]-x[0])/2 for x in data["R15-75"]]
for x in range(5):
    angle = (x + 1)*15
    print("R",angle,"=",R_uncertainty_experimental[x],"Uncertainty")