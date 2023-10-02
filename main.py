from state_node import StateNode


def main():
    space_matrix = [
        [1, 2, 3, 11],
        [4, 0, 5, 10],
        [6, 7, 8, 14]
    ]
    root = StateNode(space_matrix=space_matrix)
    root.print_space_matrix()
    print()
    root.create_right_child()
    root.create_right_child()
    root.create_right_child()
    root.print_space_matrix()


if __name__ == '__main__':
    main()

