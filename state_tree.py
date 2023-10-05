from collections import deque
from typing import Optional, Dict, List, Set, Deque
from state_node import StateNode, find_element


class StateTree:
    __root: Optional["StateNode"]
    __final_state: List[List[int]]
    __existing_nodes: Set["StateNode"]
    __solution_path: List[str]
    __found_solution: bool
    __iterations: int
    #__node_queue: Deque[Optional["StateNode"]]

    def __init__(self, root: Optional["StateNode"] = None,
                 start_state: List[List[int]] = None,
                 final_state: List[List[int]] = None):
        if start_state is not None:
            self.__root = StateNode(start_state)
        else:
            self.__root = root
        self.__final_state = final_state
        self.__existing_nodes = set()
        self.__solution_path = list()
        self.__found_solution = False
        self.__iterations = 0
        #self.__node_queue = deque()

    # ==========> METHODS
    def get_solution_path(self) -> List[str]:
        return self.__solution_path

    def get_root(self) -> Optional["StateNode"]:
        return self.__root

    # ==========> METHODS
    def build(self, heuristic_type: int) -> Optional["StateNode"]:
        node_queue: Deque[Optional["StateNode"]] = deque()
        node_queue.append(self.__root)
        self.__existing_nodes.add(self.__root)

        while len(node_queue) > 0:
            self.__iterations += 1
            current_node = node_queue.popleft()
            if current_node.get_space_matrix() == self.__final_state:
                print("Solution found")
                current_node.set_flag("S")
                self.__existing_nodes.add(current_node)
                print(self.__iterations)
                return current_node

            current_node.create_children()
            children = current_node.get_children()

            if heuristic_type == 1:
                self.compute_h1(children, self.__final_state)
            elif heuristic_type == 2:
                self.compute_h2(children, self.__final_state)
            else:
                print("No heuristic specified")
            children = sorted(children.items(), key=lambda item: item[1].get_heuristic_value())
            children = {key: value for key, value in children}

            for child in children.values():
                if child.get_space_matrix() == self.__final_state:
                    print("Solution found")
                if child in self.__existing_nodes:
                    child.set_flag("D")
                else:
                    self.__existing_nodes.add(child)
                    node_queue.appendleft(child)
        return None

    def compute_h1(self, children: Dict[str, Optional["StateNode"]], final_state: List[List[int]]) -> None:
        # Number of pieces not in the right place
        def compute_h1_for_child(current_state: List[List[int]], final_state: List[List[int]]) -> int:
            wrong_placed: int = 0
            for row in range(len(current_state)):
                for col in range(len(current_state[0])):
                    if current_state[row][col] != final_state[row][col]:
                        wrong_placed += 1
            return wrong_placed

        for child in children.values():
            h_val = compute_h1_for_child(child.get_space_matrix(), final_state)
            child.set_heuristic_value(h_val)

    def compute_h2(self, children: Dict[str, Optional["StateNode"]], final_state: List[List[int]]) -> None:
        # Sum of the distances of individual pieces from their final location
        def compute_h2_for_child(current_state: List[List[int]], final_state: List[List[int]]) -> int:
            dist_sum: int = 0
            for row in range(len(current_state)):
                for col in range(len(current_state[0])):
                    final_elm_pos = find_element(final_state, current_state[row][col])
                    dist_sum += abs(row - final_elm_pos[0]) + abs(col - final_elm_pos[1])
            return dist_sum

        for child in children.values():
            h_val = compute_h2_for_child(child.get_space_matrix(), final_state)
            child.set_heuristic_value(h_val)

    def move_right(self):
        pass

    def move_left(self):
        pass

    def move_down(self):
        pass

    def move_up(self):
        pass

    # ==========> PRIVATE METHODS
    def __are_children_d(self, children: Dict[str, Optional["StateNode"]]) -> bool:
        for child in children.values():
            if child.get_flag() != "D":
                return False
            return True

    def __exist(self, children: Dict[str, Optional["StateNode"]]) -> bool:
        for child in children.values():
            if child is None:
                return False
            return True
