from sudoku_solver.sudoku_solver import *
from sudoku_solver.search import *

def main():
    initial_state = tuple(tuple(row) for row in [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])

    print(type(initial_state))
    print(type(initial_state[0]))
    print(type(initial_state[0][0]))

    problem = Sudoku(initial_state)

    # Solve the problem using a search function (you need to import or implement it)
    solution = depth_first_graph_search(problem)

    if solution:
        print(type(solution.path()[-1].state))
        print(type(solution.path()[-1].state[0]))
        print(type(solution.path()[-1].state[0][0]))
        print(solution.path()[-1].state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()