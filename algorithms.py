import math

# Iterate through each value for n
# for i in range(10000, 100001, 10000):
#     print(i)

P = [(1, 2), (2, 4), (9, 11)]

# Brute force algorithm implementation for closest points
def BruteForceClosestPoints(P):
    d_min = math.inf

    # Stop at the second to last element
    for i in range(0, len(P)-1):
        point_1 = P[i]
        x1, y1 = point_1[0], point_1[1]
        # print('X1:', x1)
        # print('Y1:', y1)
        for j in range(i+1, len(P)):
            point_2 = P[j]
            x2, y2 = point_2[0], point_2[1]
            # print('X2:', x2)
            # print('Y2:', y2)

            d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

            if d < d_min:
                d_min, index_1, index_2 = d, i, j
    return index_1, index_2

print(BruteForceClosestPoints(P))


# Divide-and-conquer algorithm for closest points