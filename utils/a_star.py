from utils.collections import *

# Credit: https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode (accessed 12/5/2020)

class Node:
    def __init__(self):
        self.fScore = None

    def __lt__(self, other: 'Node') -> bool:
        return self.fScore[self] - self.fScore[other] < 0

    def __repr__(self) -> str:
        return str(self.fScore[self]) if self.fScore is not None and self in self.fScore else f'???'

    def set_fScore(self, fScore):
        self.fScore = fScore

    def matches_goal(self, goal) -> bool:
        raise NotImplementedError

    # h is the heuristic function. h() estimates the cost to reach goal from this node.
    def h(self) -> int:
        raise NotImplementedError

    def get_neighbors(self):
        raise NotImplementedError

    def dist_to(self, other: 'Node') -> int:
        raise NotImplementedError


def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path


class AStarMinHeap(MinHeap):
    def __init__(self, init, fScore):
        super().__init__(init)

        self._fScore = fScore

    def copy(self) -> 'Collection':
        return self.__class__(self._lst.copy(), self._fScore)

    def push(self, item: Node):
        item.set_fScore(self._fScore)
        super().push(item)

# A* finds a path from start to goal.
def a_star(start: Node, goal = None):
    # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    # how short a path from start to finish can be if it goes through n.
    fScore = dict()
    fScore[start] = start.h()

    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    # This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet = AStarMinHeap([start], fScore)

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    # to n currently known.
    cameFrom = dict()

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore = dict()
    gScore[start] = start.dist_to(start)

    while len(openSet) != 0:
        # This operation can occur in O(1) time if openSet is a min-heap or a priority queue
        current = openSet.pop()
        if current.matches_goal(goal):
            return reconstruct_path(cameFrom, current)

        for neighbor in current.get_neighbors():
            # d(current,neighbor) is the weight of the edge from current to neighbor
            # tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore = gScore[current] + current.dist_to(neighbor)
            if neighbor not in gScore or tentative_gScore < gScore[neighbor]:
                # This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + neighbor.h()
                if neighbor not in openSet:
                    openSet.push(neighbor)

    # Open set is empty but goal was never reached
    return None
