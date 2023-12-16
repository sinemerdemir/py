def read_labyrinth(filename="labyrinth.dat"):
    labyrinth = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(line.strip())  
            labyrinth.append(row)
    return labyrinth

def bfs(start, end, labyrinth):
    queue = [(start, 0)]  
    visited = set()  

    while queue:
        current, distance = queue.pop(0)
        row, col = current

        if current == end:
            return distance

        for neighbor in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            n_row, n_col = neighbor
            if 0 <= n_row < len(labyrinth) and 0 <= n_col < len(labyrinth[0]) and labyrinth[n_row][n_col] == 'P' and neighbor not in visited:
                queue.append((neighbor, distance + 1))
                visited.add(neighbor)

    return -1  

def abstand(s, t, dateiname="labyrinth.dat"):
    labyrinth = read_labyrinth(dateiname)
    return bfs(s, t, labyrinth)


