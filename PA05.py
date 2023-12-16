#This is a test comment. Comment number 1.

def get_linedistance(points,line):
    n=len(points)
    distance=0
    for i in range(0,n):
        xi,yi=points[i] 
        D=(line[0]*xi+ line[1]- yi)**2 
        distance += D 
    return distance

       
def get_optimal_line(points):
    n=len(points)
    sx=0
    sy=0
    summe_difference_x=0
    sdifference_x=0
    summe_difference_xy=0
    for i in range(0,n):
        xi,yi=points[i]
        sy += yi
        sx += xi 
    avgx=sx/n
    avgy=sy/n
    for i in range(0,n):
        xi,yi=points[i]
        difference_x=(xi-avgx)
        sdifference_x=(difference_x)**2
        summe_difference_x += sdifference_x
        difference_y=(yi-avgy)
        mdifference_xy= difference_x * difference_y 
        summe_difference_xy+= mdifference_xy

    a = summe_difference_xy/summe_difference_x
    b = avgy - a* avgx
    return a,b

def distance_to_opt(points,lines):
    Differenz=0
    best_line_distance=0
    Anzahl_l=len(lines)
    distances=[]
    for i in range(0,Anzahl_l):
        distance= get_linedistance(points,lines[i])
        distances.append(distance)
    best_line_distance=min(distances)
    a,b=get_optimal_line(points)
    optimal_distance=get_linedistance(points,(a,b))
    Differenz= best_line_distance - optimal_distance
    return Differenz






