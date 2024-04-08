import math

def distance_normaliser(c1, c2, map_size=200):
    # takes just single pair of coordinates, doesn't really matter which one they are
    # also technically takes map size, defaulting to 200
    #just to make life simpler, we're going to add 200 to each value (no negative numbers)
    c1 += 200
    c2 += 200
    map_size += map_size

    if c1 > c2:
        t1 = True
    else:
        t1 = False

    #derive distance in both possible directions, select smallest one
    if t1:
        v1 = c1-c2
    else:
        v1 = c2-c1
    #this should be the direction that involves zero looping over the map
    #now try the other direction
    if t1:
        var = map_size - c1
        v2 = var + c2 + 1 #add one for looping over 0 axis
    else:
        var = map_size - c2
        v2 = var + c1 + 1
    distance = min(v1, v2)

    return distance

def distance_calc(x1, x2, y1, y2):
    # function takes 4 inputs - x,y (obvious, one for each co-ord of pair)

    # distance in travian can be calculated via triangle rules
    # abs(x1-x2)**2 + abs(y1-y2)**2 = distance**2
    # but we also need a way to handle splits across the map dimensions
    # this will utilise the distance_normaliser function

    x_dist = distance_normaliser(x1, x2)
    y_dist = distance_normaliser(y1, y2)
    print(f' x, y dists are {x_dist} , {y_dist}')
    x_dist = x_dist **2
    y_dist = y_dist **2
    true_dist = math.sqrt((x_dist+y_dist))
    return round(true_dist,2)

def basic_test():
    #passed
    t1 = distance_calc(19,20,194,194)
    print(t1)
    t2 = distance_calc(19,19,194,195)
    print(t2)
    t3 = distance_calc(19,20,194,195)
    print(t3)
    t4 = distance_calc(19, 19, 194, -200)
    print(t4)
    t5 = distance_calc(20, -33, 194, -190)
    print(t5)

def duration_calc(dist, ts, arti):

    base_speed = 3*arti
    if dist < 20:
        dur = dist/base_speed
    else:
        dist2 = dist-20
        dur1 = 20/base_speed
        base_speed2 = base_speed * (1+(0.2*ts))
        dur2 = dist2/base_speed2
        dur = dur1 + dur2

    return dur

def basic_test2():
    #passed, provisionally
    t1 = distance_calc(19,20,194,194)
    d1 = duration_calc(t1, 0, 1)
    print(t1)
    print(d1)
    t2 = distance_calc(19,19,194,195)
    d2 = duration_calc(t2, 0, 1)
    print(t2)
    print(d2)
    t3 = distance_calc(19,20,194,195)
    d3 = duration_calc(t3, 0, 1)
    print(t3)
    print(d3)
    t4 = distance_calc(19, 19, 194, -200)
    d4 = duration_calc(t4, 0, 1)
    print(t4)
    print(d4)
    t5 = distance_calc(20, -33, 194, -190)
    d5 = duration_calc(t5, 0, 1)
    d6 = duration_calc(t5, 20, 1)
    d7 = duration_calc(t5, 20, 2)
    print(t5)
    print(d5)
    print(d6)
    print(d7)

basic_test2()