from collections import deque
def findShortestWay(maze, ball, hole):


    def maze_cell(r, c):
        if [r, c] == hole:
            return -1
        elif 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == 0:
            return 0
        return 1

    def vertical(dirn):
        return dirn in {"d", "u"}

    def perpendicular(dirn):
        return ["r", "l"] if vertical(dirn) else ["u", "d"]  # reverse lexicographical order

    visited = set()  # stores tuples (r, c, dirn)
    queue = deque()
    dirns = {"d": (1, 0), "u": (-1, 0), "r": (0, 1), "l": (0, -1)}
    for dirn in dirns.keys():
        queue.append((ball[0], ball[1], [dirn]))

    while queue:
        r, c, moves = queue.popleft()
        if (r, c, moves[-1]) in visited:
            continue
        visited.add((r, c, moves[-1]))

        dr, dc = dirns[moves[-1]]
        nm = maze_cell(r + dr, c + dc)

        if nm == -1:
            print(moves)
            return

        # move in same direction as previous if possible
        elif nm == 0:
            queue.append((r + dr, c + dc, moves))  # add to back of queue

        # else move in a perpendicular direction if possible and not at start
        elif [r, c] != ball:
            trial_dirns = perpendicular(moves[-1])
            for trial_dirn in trial_dirns:
                queue.appendleft((r, c, moves + [trial_dirn]))  # add to front of queue

    print(-1)


A = [
  [1, 1, 0, 1],
  [0, 0, 0, 1],
  [1, 0, 0, 1],
  [0, 0, 1, 0]
]
B = [ 1, 1 ]
C = [ 2, 1 ]
findShortestWay(A,B,C)






