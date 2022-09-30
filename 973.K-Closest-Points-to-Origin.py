# Given an array of points where points[i] = [xi, yi] represents 
# a point on the X-Y plane and an integer k, return the k closest 
# points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean 
# distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed 
# to be unique (except for the order that it is in).

def kClosest(points, k):
    res = {}
    def findDistance(point):
        sum = point[0] ** 2 + point[1] ** 2
        return math.sqrt(sum)

    for point in points:
        dist = findDistance(point)
        if dist not in res:
            res[dist] = [point]
        else:
            res[dist].append(point)
    
    keys = list(res.keys())
    keys.sort()
    result = []
    for i in keys:
        result = result + res[i]
    print(result)
    return result[:k]
