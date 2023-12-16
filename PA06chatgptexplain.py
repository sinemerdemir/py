# This function reads a labyrinth from a file and returns it as a list of lists.
def read_labyrinth(filename="labyrinth.dat"):
    labyrinth = []  # Create an empty list to store the labyrinth.
    with open(filename, 'r') as file:  # Open the file for reading.
        for line in file:  # Loop through each line in the file.
            row = list(line.strip())  # Convert each line into a list of characters.
            labyrinth.append(row)  # Add the list of characters to the labyrinth list.
    return labyrinth  # Return the final labyrinth.

# This function performs Breadth-First Search to find the distance between two points in a labyrinth.
def bfs(start, end, labyrinth):
    queue = [(start, 0)]  # Create a queue with the starting point and distance initialized to 0.
    visited = set()  # Create a set to keep track of visited points.

    while queue:  # Continue as long as there are points in the queue.
        current, distance = queue.pop(0)  # Get the first point in the queue.
        row, col = current  # Get the row and column of the current point.

        if current == end:  # Check if the current point is the destination.
            return distance  # If yes, return the distance traveled.

        # Check the neighboring points in the up, down, left, and right directions.
        for neighbor in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            n_row, n_col = neighbor  # Get the row and column of the neighbor.
            # Check if the neighbor is within the labyrinth boundaries and is a valid path ('P').
            if 0 <= n_row < len(labyrinth) and 0 <= n_col < len(labyrinth[0]) and labyrinth[n_row][n_col] == 'P' and neighbor not in visited:
                # If yes, add the neighbor to the queue with an increased distance.
                queue.append((neighbor, distance + 1))
                # Mark the neighbor as visited.
                visited.add(neighbor)

    # If the destination is not reached, return -1 to indicate that there is no path.
    return -1

# This function calculates the distance between two points in a labyrinth.
def abstand(s, t, dateiname="labyrinth.dat"):
    labyrinth = read_labyrinth(dateiname)  # Read the labyrinth from the specified file.
    return bfs(s, t, labyrinth)  # Use BFS
