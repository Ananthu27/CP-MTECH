def turn(x,y,z):
    # return determinent after shifting y to the origin
    return ((x[0]-y[0])*(z[1]-y[1]))-((x[1]-y[1])*(z[0]-y[0]))

# recursive function remove last but one until no turning left
def reduceL(hull):
    if len(hull)<3:
        return hull
    else :
        a = hull[-3]
        b = hull[-2]
        c = hull[-1]
        res = turn(a,b,c)
        # no turn or right turn
        if res >= 0 :
            return hull
        
        # left trurn
        else :
            r = hull.pop(-2)
            return reduceL(hull)
        
# recursive function remove last but one until no turning left
def reduceR(hull):
    if len(hull)<3:
        return hull
    else :
        a = hull[-3]
        b = hull[-2]
        c = hull[-1]
        res = turn(a,b,c)
        
        # no turn or left turn
        if res <= 0 :
            return hull
        
        # right turn
        else :
            r=hull.pop(-2)
            return reduceR(hull)

# input = [(2,4),(2,2),(1,1),(4,4),(4,2),(5,1),(3,2)]
from random import randint
input = []
for i in range(50):
    cordinate = (randint(1,50),randint(1,40))
    if cordinate not in input:
        input.append(cordinate) 
input.sort()

upper_hull = []
for cordinate in input :
    upper_hull.append(cordinate)
    upper_hull = reduceL(hull=upper_hull)

lower_hull = []
for cordinate in input :
    lower_hull.append(cordinate)
    lower_hull = reduceR(hull=lower_hull)

# import matplotlib.pyplot as plt 
# plt.plot(
#     [item[0] for item in upper_hull],
#     [item[1] for item in upper_hull],
#     color='red'
# )
# plt.plot(
#     [item[0] for item in lower_hull],
#     [item[1] for item in lower_hull],
#     color='red'
# )
# plt.scatter(
#     x=[item[0] for item in input],
#     y=[item[1] for item in input]
# )
# plt.show()