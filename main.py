from state_node import StateNode


def main():
    space_matrix = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    root = StateNode(space_matrix=space_matrix)
    root.print_space_matrix()
    print()
    root.create_children()
    children = root.get_children()
    children["left"].print_space_matrix()
    print()
    children["right"].print_space_matrix()
    print()
    children["up"].print_space_matrix()
    print()
    children["down"].print_space_matrix()


if __name__ == '__main__':
    main()

