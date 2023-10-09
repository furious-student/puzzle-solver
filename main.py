from puzzle_solver import PuzzleSolver
from tester import run_test, create_test_set
from json import dumps


def main():
    space_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    space_matrix2 = [
        [5, 1, 0],
        [4, 6, 8],
        [7, 3, 2],
    ]

    space_matrix_h1 = [
        [8, 3, 1],
        [0, 6, 2],
        [5, 7, 4]
    ]
    space_matrix2_h2 = [
        [1, 6, 5],
        [7, 2, 8],
        [4, 3, 0]
    ]

    space_matrix_15_v1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]

    space_matrix_15_v2 = [
        [0, 2, 3, 4],
        [1, 6, 7, 8],
        [5, 9, 10, 11],
        [13, 14, 15, 12]
    ]

    json_format = run_test(number_of_tests=15, bidirect=True, mtx_n_size=3, mtx_m_size=3, next_node_select=2)
    print("Result with next node from children (3x3):")
    print(dumps(json_format, indent=4))

    json_format = run_test(number_of_tests=15, bidirect=True, mtx_n_size=3, mtx_m_size=3, next_node_select=1)
    print("Result with next best node (3x3):")
    print(dumps(json_format, indent=4))

    json_format = run_test(number_of_tests=15, bidirect=True, mtx_n_size=4, mtx_m_size=4, next_node_select=2)
    print("Result with next node from children (4x4):")
    print(dumps(json_format, indent=4))

    json_format = run_test(number_of_tests=15, bidirect=True, mtx_n_size=4, mtx_m_size=4, next_node_select=1)
    print("Result with next best node (4x4):")
    print(dumps(json_format, indent=4))

    json_format = run_test(number_of_tests=5, bidirect=False, mtx_n_size=5, mtx_m_size=5, next_node_select=2)
    print("Result with next node from children (5x5):")
    print(dumps(json_format, indent=4))

    # test_set = create_test_set(3, 3, True)
    # solver = PuzzleSolver()
    # solver.set_states(space_matrix_h1, space_matrix2_h2)
    # result = solver.solve(heuristic_type=1, next_node_select=2)
    # print(result[0], "\n", result[1], "\n", result[2])
    # print()
    # result = solver.solve(heuristic_type=2)
    # print(result[0], "\n", result[1], "\n", result[2])


if __name__ == '__main__':
    main()
