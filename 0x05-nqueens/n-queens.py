#!/usr/bin/python3
"""N-Queens Solution Finder Module.
"""
import sys

results = []
"""The list of possible solutions to the N-Queens problem.
"""
board_size = 0
"""The size of the chessboard.
"""
positions = None
"""The list of possible positions on the chessboard.
"""


def retrieve_input():
    """Retrieves and validates the program's argument.
    Returns:
        int: The size of the chessboard.
    """
    global board_size
    board_size = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        board_size = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    return board_size


def in_conflict(pos1, pos2):
    """Checks if two queens are in a conflict position.
    Args:
        pos1 (list or tuple): Position of the 1st queen.
        pos2 (list or tuple): Position of the 2nd queen.
    Returns:
        bool: True if the queens are in a conflicting position, otherwise False.
    """
    if (pos1[0] == pos2[0]) or (pos1[1] == pos2[1]):
        return True
    return abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


def solution_exists(candidate):
    """Checks if a candidate solution exists in the list of results.
    Args:
        candidate (list of tuples): A candidate group of queen positions.
    Returns:
        bool: True if the candidate exists, otherwise False.
    """
    global results
    for solution in results:
        count = 0
        for sol_pos in solution:
            for cand_pos in candidate:
                if sol_pos[0] == cand_pos[0] and sol_pos[1] == cand_pos[1]:
                    count += 1
        if count == board_size:
            return True
    return False


def generate_solution(row, candidate):
    """Recursively builds solutions for the N-Queens problem.
    Args:
        row (int): The current row in the chessboard.
        candidate (list of lists): The current candidate positions.
    """
    global results
    global board_size
    if row == board_size:
        temp_solution = candidate.copy()
        if not solution_exists(temp_solution):
            results.append(temp_solution)
    else:
        for col in range(board_size):
            index = (row * board_size) + col
            pairings = zip([positions[index]] * len(candidate), candidate)
            conflicting_positions = map(lambda x: in_conflict(x[0], x[1]), pairings)
            candidate.append(positions[index].copy())
            if not any(conflicting_positions):
                generate_solution(row + 1, candidate)
            candidate.pop(len(candidate) - 1)


def find_solutions():
    """Finds solutions for the given chessboard size.
    """
    global positions, board_size
    positions = list(map(lambda x: [x // board_size, x % board_size], range(board_size ** 2)))
    generate_solution(0, [])


board_size = retrieve_input()
find_solutions()
for result in results:
    print(result)
