#https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

## https://www.khanacademy.org/math/geometry/xff63fac4:hs-geo-conic-sections/hs-geo-circle-expanded-equation/a/circle-equation-review


# Definimos la ecuacióin de un círculo (segundo enlace)

def circleEq(x0,y0,x,y):
    return ((x-x0)**2 + (y-y0)**2)


def countPointInside(points, queries):

    output = []
    for lst1 in queries:
        count = 0

        for point in points:
            eq_circle = lst1[:2] + point
            point_in_circle = circleEq(*eq_circle)

            if point_in_circle <= lst1[-1]**2:
                count+=1

        output.append(count)
    
    return output



points = [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]
print(countPointInside(points, queries))

points = [[1,1],[2,2],[3,3],[4,4],[5,5]]
queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
print(countPointInside(points, queries))