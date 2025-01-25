from sudoku_solver.search import *

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



    

