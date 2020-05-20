# Used excel and manually-discovered points... cheating?
SE = 1
SW = 2
NW = 3
NE = 4

def corner(depth: int, direction: int) -> int:
    return 2*depth*direction + 4*depth*(depth-1) + 1


SIZE = 1001
MAX_DEPTH = (SIZE - 1) // 2
result = 1 + sum(corner(depth, dir)
    for depth in range(1, MAX_DEPTH+1)
    for dir in range(1, 5)
)

print(result)

