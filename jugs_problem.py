from abc import ABC

from simpleai.search import SearchProblem
from simpleai.search.viewers import ConsoleViewer

my_viewer = ConsoleViewer()


class JugsProblem(SearchProblem, ABC):

    def __init__(self, initial_state=(0, 0, 0), max_capacity=None, target_volume=None):
        super().__init__(initial_state)
        self.max_capacity = max_capacity  # (C1,C2,C3)
        self.target_volume = target_volume  # (T1,T2,T3)

    def actions(self, state):
        all_actions = [
            'Fill Jug1',
            'Fill Jug2',
            'Fill Jug3',
            'Empty Jug1',
            'Empty Jug2',
            'Empty Jug3',
            'Pour Jug1 to Jug2',
            'Pour Jug1 to Jug3',
            'Pour Jug2 to Jug1',
            'Pour Jug2 to Jug3',
            'Pour Jug3 to Jug1',
            'Pour Jug3 to Jug2'
        ]
        return all_actions

    def result(self, state, action):
        next_state = list(state)
        if action == "Fill Jug1":
            next_state[0] = self.max_capacity[0]
            return tuple(next_state)
        elif action == "Fill Jug2":
            next_state[1] = self.max_capacity[1]
            return tuple(next_state)
        elif action == "Fill Jug3":
            next_state[2] = self.max_capacity[2]
            return tuple(next_state)
        elif action == "Empty Jug1":
            next_state[0] = 0
            return tuple(next_state)
        elif action == "Empty Jug2":
            next_state[1] = 0
            return tuple(next_state)
        elif action == "Empty Jug3":
            next_state[2] = 0
            return tuple(next_state)
        elif action == "Pour Jug1 to Jug2":
            current_jug1 = next_state[0]
            current_jug2 = next_state[1]
            capacity_jug2 = self.max_capacity[1]
            if capacity_jug2 - current_jug2 >= current_jug1:
                to_be_added = current_jug1
                current_jug2 += to_be_added
                current_jug1 = 0
            else:
                to_be_added = capacity_jug2 - current_jug2
                current_jug2 += to_be_added
                current_jug1 -= to_be_added
            next_state[0] = current_jug1
            next_state[1] = current_jug2
            return tuple(next_state)
        elif action == "Pour Jug1 to Jug3":
            current_jug1 = next_state[0]
            current_jug3 = next_state[2]
            capacity_jug3 = self.max_capacity[2]
            if capacity_jug3 - current_jug3 >= current_jug1:
                to_be_added = current_jug1
                current_jug3 += to_be_added
                current_jug1 = 0
            else:
                to_be_added = capacity_jug3 - current_jug3
                current_jug3 += to_be_added
                current_jug1 -= to_be_added
            next_state[0] = current_jug1
            next_state[2] = current_jug3
            return tuple(next_state)
        elif action == "Pour Jug2 to Jug1":
            current_jug1 = next_state[0]
            current_jug2 = next_state[1]
            capacity_jug1 = self.max_capacity[0]
            if capacity_jug1 - current_jug1 >= current_jug2:
                to_be_added = current_jug2
                current_jug1 += to_be_added
                current_jug2 = 0
            else:
                to_be_added = capacity_jug1 - current_jug1
                current_jug1 += to_be_added
                current_jug2 -= to_be_added
            next_state[0] = current_jug1
            next_state[1] = current_jug2
            return tuple(next_state)
        elif action == "Pour Jug2 to Jug3":
            current_jug3 = next_state[2]
            current_jug2 = next_state[1]
            capacity_jug3 = self.max_capacity[2]
            if capacity_jug3 - current_jug3 >= current_jug2:
                to_be_added = current_jug2
                current_jug3 += to_be_added
                current_jug2 = 0
            else:
                to_be_added = capacity_jug3 - current_jug3
                current_jug3 += to_be_added
                current_jug2 -= to_be_added
            next_state[1] = current_jug2
            next_state[2] = current_jug3
            return tuple(next_state)
        elif action == "Pour Jug3 to Jug1":
            current_jug1 = next_state[0]
            current_jug3 = next_state[2]
            capacity_jug1 = self.max_capacity[0]
            if capacity_jug1 - current_jug1 >= current_jug3:
                to_be_added = current_jug3
                current_jug1 += to_be_added
                current_jug3 = 0
            else:
                to_be_added = capacity_jug1 - current_jug1
                current_jug1 += to_be_added
                current_jug3 -= to_be_added
            next_state[0] = current_jug1
            next_state[2] = current_jug3
            return tuple(next_state)
        elif action == "Pour Jug3 to Jug2":
            current_jug2 = next_state[1]
            current_jug3 = next_state[2]
            capacity_jug2 = self.max_capacity[1]
            if capacity_jug2 - current_jug2 >= current_jug3:
                to_be_added = current_jug3
                current_jug2 += to_be_added
                current_jug3 = 0
            else:
                to_be_added = capacity_jug2 - current_jug2
                current_jug2 += to_be_added
                current_jug3 -= to_be_added
            next_state[1] = current_jug2
            next_state[2] = current_jug3
            return tuple(next_state)

    def state_representation(self, state):
        return str(state)

    def is_goal(self, state) -> bool:
        return state == self.target_volume

    def cost(self, state, action, state2):
        """Returns the cost of applying `action` from `state` to `state2`.
           The returned value is a number (integer or floating point).
           By default this function returns `1`.
        """
        s1_list = list(state)
        s2_list = list(state2)
        """
        cost is always 1, it does not change from action to action
        return 1
        """
        # return 1
        """
        the cost changes when water is added to a jug or when water is emptied from a jug.
        """
        return abs(s1_list[0] - s2_list[0]) + abs(s1_list[1] - s2_list[1]) + abs(s1_list[2] - s2_list[2])
