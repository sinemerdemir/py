from PA05 import * 

points = [(-2,2),(1,3),(2,2),(6,-2)]
lines = [(1,1),(-1,4)]
d0 = get_linedistance(points, lines[0])
d1 = get_linedistance(points, lines[1])
(a,b) = get_optimal_line(points)

get_linedistance(points, (a,b))
distance_to_opt(points, lines)
print(distance_to_opt(points,lines))