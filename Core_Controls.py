import math

def distance_normaliser(c1, c2, map_size=200):
    # takes just single pair of coordinates, doesn't really matter which one they are
    # also technically takes map size, defaulting to 200

    if ((c1 > 0) & (c2 < 0)) or ((c1 < 0) & (c2 > 0)):
        sign_imbalance = True
    else:
        sign_imbalance = False
    #print(sign_imbalance)

    if sign_imbalance:
        #EW HOW DOES THIS WORK???????
        new_dist =
        c2 = c2*-1
        mod = 1
    else:
        mod=0
    distance = abs(c1-c2) + mod

    return distance

def distance_calc(x1, x2, y1, y2 ,ts , arti_mod):
    # function takes 6 inputs - x,y (obvious, one for each co-ord of pair), ts (tournament square level),
    # and arti_mod (relevant artifact)

    # distance in travian can be calculated via triangle rules
    # abs(x1-x2)**2 + abs(y1-y2)**2 = distance**2
    # but we also need a way to handle splits across the map dimensions
    # this will utilise the distance_normaliser function

    x_dist = distance_normaliser(x1, x2)
    y_dist = distance_normaliser(y1, y2)
    print(x_dist,y_dist)
    x_dist = x_dist **2
    y_dist = y_dist **2
    true_dist = math.sqrt((x_dist+y_dist))
    return round(true_dist,2)

def basic_test():
    #passed
    t1 = distance_calc(19,20,194,194,20,0)
    print(t1)
    t2 = distance_calc(19,19,194,195,20,0)
    print(t2)
    t3 = distance_calc(19,20,194,195,20,0)
    print(t3)
    t4 = distance_calc(19, 19, 194, -200, 20, 0)
    print(t4)
#basic_test()
t5 = distance_calc(19,-37,194,-184,20,0)
print(t5)

