from typing import List, Dict
import numpy as np
from puzzle_solver import PuzzleSolver
from random import shuffle
from time import time


# ==========> FUNCTIONS
def run_test(number_of_tests: int = 3, bidirect: bool = False, mtx_m_size: int = 3, mtx_n_size: int = 3,
             next_node_select: int = 1) -> Dict[str, Dict[str, int]]:
    h1_result = {
        "avg_time": 0,
        "avg_depth": 0,
        "avg_nodes_created": 0
        }
    h2_result = {
        "avg_time": 0,
        "avg_depth": 0,
        "avg_nodes_created": 0
    }
    if bidirect:
        h1_result["avg_bd_time"] = 0
        h1_result["avg_bd_depth"] = 0
        h1_result["avg_bd_nodes_created"] = 0

        h2_result["avg_bd_time"] = 0
        h2_result["avg_bd_depth"] = 0
        h2_result["avg_bd_nodes_created"] = 0

    solver = PuzzleSolver()

    for i in range(number_of_tests):
        time_before = 0
        time_after = 0
        test_set = create_test_set(mtx_m_size, mtx_n_size)
        print(test_set["init_matrix"], "\n", test_set["final_matrix"])
        solver.set_states(test_set["init_matrix"], test_set["final_matrix"])
        time_before = int(time() * 1000)
        result = solver.solve(heuristic_type=1, next_node_select=next_node_select)
        time_after = int(time() * 1000)
        h1_result["avg_depth"] += result[1]
        h1_result["avg_nodes_created"] += result[2]
        h1_result["avg_time"] += time_after - time_before
        # print(result[0])

        time_before = int(time() * 1000)
        result = solver.solve(heuristic_type=2, next_node_select=next_node_select)
        time_after = int(time() * 1000)
        h2_result["avg_depth"] += result[1]
        h2_result["avg_nodes_created"] += result[2]
        h2_result["avg_time"] += time_after - time_before
        # print(result[0])

        if bidirect:
            solver.set_states(test_set["final_matrix"], test_set["init_matrix"])
            time_before = int(time() * 1000)
            result = solver.solve(heuristic_type=1, next_node_select=next_node_select)
            time_after = int(time() * 1000)
            h1_result["avg_bd_depth"] += result[1]
            h1_result["avg_bd_nodes_created"] += result[2]
            h1_result["avg_bd_time"] += time_after - time_before
            # print(result[0])

            time_before = int(time() * 1000)
            result = solver.solve(heuristic_type=2, next_node_select=next_node_select)
            time_after = int(time() * 1000)
            h2_result["avg_bd_depth"] += result[1]
            h2_result["avg_bd_nodes_created"] += result[2]
            h2_result["avg_bd_time"] += time_after - time_before
            # print(result[0])
    h1_result = {key: value/number_of_tests for key, value in h1_result.items()}
    h2_result = {key: value/number_of_tests for key, value in h2_result.items()}
    return {
        "h1_result": h1_result,
        "h2_result": h2_result
    }


def create_test_set(m_size: int = 3, n_size: int = 3, solvable: bool = True) -> Dict[str, List[List[int]]]:
    # Generates two random matrices of given size. If solvable is set to True, the solvability criterion must be met
    elements = list((range(0, m_size*n_size)))
    shuffle(elements)
    init_matrix = np.array(elements).reshape(m_size, n_size).tolist()
    shuffle(elements)
    final_matrix = np.array(elements).reshape(m_size, n_size).tolist()
    if solvable:
        puzzle_solver = PuzzleSolver(init_matrix, final_matrix)
        while not puzzle_solver.is_solvable():
            shuffle(elements)
            final_matrix = np.array(elements).reshape(m_size, n_size).tolist()
            puzzle_solver.set_states(init_matrix, final_matrix)
    print("==========>\nTest set created")
    return {"init_matrix": init_matrix,
            "final_matrix": final_matrix}
