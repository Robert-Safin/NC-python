from collections import deque
from typing import List,Tuple

def bfs_path(grid: List[List[int]]) -> int:
    # helper variables used checking if index is in bounds
    rows, cols = len(grid), len(grid[0])

    # start cell and goal cell
    start = (0, 0)
    end = (rows - 1, cols - 1 )

    # deque for BFS (r, c, distance from start)
    queue = deque([(start[0], start[1], 1)])

    # track visited cells
    visited = set()

    # push to init the loop
    visited.add(start)

    # loop until there are valid neighbors in the deque
    while queue:
        # get next in line neighbor
        r, c, dist = queue.popleft()

        # break loop if arrived at goal cell
        if (r, c) == end:
            return dist

        # generate neighbor coordinates (up/down/left/right) based on cell from deque
        neighbors = [   (r + 1, c),
                        (r - 1, c),
                        (r, c + 1),
                        (r, c - 1),
                        (r + 1,c + 1),
                        (r + 1,c - 1),
                        (r - 1,c + 1),
                        (r - 1,c - 1)]

        # check if neighbor is valid
        for neighbor in neighbors:
            (neighbor_r, neighbor_c) = neighbor

                # neighbor is does not have negative indices
            if (neighbor_r >= 0 and neighbor_c >= 0 and
                # neighbor is does not have above bounds indices
                neighbor_r < rows and neighbor_c < cols and
                # neighbor has not been visited before
                (neighbor_r, neighbor_c) not in visited and
                # neighbor is allowed to be stepped on
                grid[neighbor_r][neighbor_c] != 1
                ):

                # if all above are true, its a valid neighbor
                # added to visited, add to deque's tail, bump distance from start cell by 1
                visited.add((neighbor_r, neighbor_c))
                queue.append((neighbor_r, neighbor_c, dist + 1))

    # if no goal cell is reached
    return -1


grid1 = [   [0,1],
            [1,0]] # 2

grid2 = [   [0,0,0],
            [1,1,0],
            [1,1,0]] #4

grid3 = [   [1,0,0],
            [1,1,0],
            [1,1,0] ] # 4

print(bfs_path(grid3))  # Expected output: 2
