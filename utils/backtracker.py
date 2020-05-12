from utils.collections import *


class Configuration:
    def get_children(self) -> list:
        raise NotImplementedError('Method not implemented')

    def is_valid(self) -> bool:
        raise NotImplementedError('Method not implemented')

    def is_goal(self) -> bool:
        raise NotImplementedError('Method not implemented')


class Backtracker:
    BFS = Queue
    DFS = Stack

    def run(self, init_config: Configuration, search_coll: Collection, goal_halts = True, debug = False) -> tuple:
        if type(search_coll) == type:
            search_coll = search_coll()

        goals = []

        search_coll.push(init_config)
        while len(search_coll) > 0:
            config = search_coll.pop()

            if not config.is_valid():
                continue

            if debug:
                print(config)

            if config.is_goal():
                goals.append(config)
                if goal_halts:
                    return tuple(goals)
            else:
                search_coll.push_many(config.get_children())

        return tuple(goals)
