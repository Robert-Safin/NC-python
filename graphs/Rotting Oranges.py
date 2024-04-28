from collections import deque
from typing import List, Tuple,Deque

def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue:Deque[Tuple[int,int]] = deque()
    fresh = 0

    # Initialize the queue with all initial rotten oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    # Early exit if there are no fresh oranges
    if fresh == 0:
        return 0

    time = 0  # Start time counter at zero
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 4 possible directions

    # Process the queue
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()

            # Check all four possible directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Mark the orange as rotten
                    fresh -= 1  # Decrement the count of fresh oranges
                    queue.append((nr, nc))  # Add this new rotten orange to the queue

        time += 1  # Increment time after processing all oranges at the current time step

    # Check if there are still fresh oranges left
    return time - 1 if fresh == 0 else -1

# Example usage
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
print(orangesRotting(grid))  # Output: 4
