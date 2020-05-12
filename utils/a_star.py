# Credit: https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode (accessed 12/5/2020)

class Node:
    def matches_goal(self, goal) -> bool:
        raise NotImplementedError

    def get_neighbors(self):
        raise NotImplementedError

    def dist_to(self, other: 'Node'):
        raise NotImplementedError


def reconstruct_path(cameFrom, current):
    total_path = set([current])
    while current in cameFrom:
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path


# A* finds a path from start to goal.
# h is the heuristic function. h(n) estimates the cost to reach goal from node n.
# d(current,neighbor) is the weight of the edge from current to neighbor
def a_star(start: Node, goal, h):
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    # This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet = set([start])

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    # to n currently known.
    cameFrom = dict()

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore = dict()
    gScore[start] = 0

    # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    # how short a path from start to finish can be if it goes through n.
    fScore = dict()
    fScore[start] = h(start)

    while len(openSet) != 0:
        # This operation can occur in O(1) time if openSet is a min-heap or a priority queue
        current = min(openSet, key=lambda n: fScore[n])
        if current.matches_goal(goal):
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        for neighbor in current.get_neighbors():
            # d(current,neighbor) is the weight of the edge from current to neighbor
            # tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore = gScore[current] + current.dist_to(neighbor)
            if tentative_gScore < gScore[neighbor]:
                # This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + h(neighbor)
                if neighbor not in openSet:
                    openSet.add(neighbor)

    # Open set is empty but goal was never reached
    return None
