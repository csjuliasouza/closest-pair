import math

# Iterate through each value for n
# for i in range(10000, 100001, 10000):
#     print(i)

points = [(9, 1), (3, 2), (1, 5), (2, 4)]

# Brute force algorithm implementation for closest points
def brute_force_closest_points(p):
    d_min = math.inf
    
    # For each point in the array, compare the distance
    # with successive points to find the minimum distance
    for i in range(0, len(p)-1):
        point_1 = p[i]
        x1, y1 = point_1[0], point_1[1]
        # print('X1:', x1)
        # print('Y1:', y1)
        for j in range(i+1, len(p)):
            point_2 = p[j]
            x2, y2 = point_2[0], point_2[1]
            # print('X2:', x2)
            # print('Y2:', y2)

            d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

            if d < d_min:
                d_min, index_1, index_2 = d, i, j
    return index_1, index_2

print(brute_force_closest_points(points))


# Divide-and-conquer algorithm - INCOMPLETE
def closest_pair(p):
    p_x = sorted(p, key=lambda x: x[0])
    p_y = sorted(p, key=lambda x: x[1])
    # print(p_x)
    # print(p_y)

    # result = closest_pair_rec(p_x, p_y)

def closest_pair_rec(p_x, p_y):
    pass

print(closest_pair(points))