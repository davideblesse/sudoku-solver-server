from search import *

class Sudoku(Problem):
    def __init__(self, initial):
        super().__init__(initial)
    
    def find_free_cell(self, state):
        for i, row in enumerate(state):  # Use enumerate for better readability
            for j, value in enumerate(row):  # Enumerate the row directly
                if value == 0:  # Free cell found
                    return i, j
        return -1, -1  # No free cell found
    
    def are_rows_valid(self, state):
        """
        Check that all rows in the state have unique non-zero values.
        """
        for row in state:
            if not self.is_unique(row):
                return False
        return True

    def are_columns_valid(self, state):
        """
        Check that all columns in the state have unique non-zero values.
        """
        # Transpose the state to get columns as rows
        transposed_state = zip(*state)
        for column in transposed_state:
            if not self.is_unique(column):
                return False
        return True

    def are_blocks_valid(self, state):
        """
        Check that all 3x3 blocks in the state have unique non-zero values.
        """
        blocks_state = [
            [state[j // 3 + (i // 3) * 3][j % 3 + (i % 3) * 3] for j in range(len(state))]
        for i in range(len(state))
        ]
        for block in blocks_state:
            if not self.is_unique(block):
                return False
        return True
    
    @staticmethod
    def is_unique(values):
        """
        Helper method to check if all non-zero elements in a list are unique.
        """
        non_zero_values = [v for v in values if v != 0]
        return len(non_zero_values) == len(set(non_zero_values))


    def actions(self, state):
        """
        Return a list of valid numbers for the next free cell.
        """
        new_state = [list(row) for row in state]
        moves = []
        free_cell_i, free_cell_j = self.find_free_cell(new_state)

        for i in range(1, 10):
            new_state[free_cell_i][free_cell_j] = i
            if(self.is_valid(new_state)):
                moves.append(i)
        return moves

    def result(self, state, action):
        """
        Apply the action and return the resulting state.
        """
        new_state = [list(row) for row in state]
        free_cell_i, free_cell_j = self.find_free_cell(new_state)
        new_state[free_cell_i][free_cell_j] = action

        return tuple(tuple(row) for row in new_state)

    def goal_test(self, state):
        """
        Check if the Sudoku is completely filled and valid.
        """
        return self.is_filled(state) and self.is_valid(state)
    
    def is_valid(self, state):
        """
        Check if the entire Sudoku state is valid (rows, columns, blocks).
        """
        return (
            self.are_rows_valid(state) and
            self.are_columns_valid(state) and
            self.are_blocks_valid(state)
        )
    def is_filled(self, state):
        """
        Check if the Sudoku grid is completely filled (no zeros).
        """
        return all(all(value != 0 for value in row) for row in state)


class SudokuNode(Node):
    def __str__(self):
        """
        Returns a string representation of the Sudoku grid in a formatted layout.
        """
        grid = ""
        for i, row in enumerate(self.state):  # No need to convert rows; iterate over tuples directly
            # Format each row, replacing 0 with '.'
            row_str = " ".join(str(num) if num != 0 else "." for num in row)
            # Add 3x3 block separators
            grid += row_str[:5] + " | " + row_str[6:11] + " | " + row_str[12:] + "\n"
            
            # Add horizontal separators after every 3rd row (blocks)
            if i in [2, 5]:
                grid += "-" * 21 + "\n"
        return grid
        

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

    
    problem = Sudoku(initial_state)

    # Solve the problem using a search function (you need to import or implement it)
    solution = depth_first_graph_search(problem)

    if solution:
        print(SudokuNode(solution.path()[-1].state))
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()


    

