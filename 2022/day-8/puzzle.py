import numpy as np

from typing import List, Tuple


def main():
    fname = "puzzle_data.txt"

    grid = ingest_file(fname)
    visible_trees = scan_tree_grid(grid)
    print("-------- Part 1 --------")
    print(visible_trees)
    i, j, score = calculate_scenic_score(grid)
    print("-------- Part 2 --------")
    print(i, j, score)

def ingest_file(fname: str) -> List[str]:
    """
    Reads a file with a grid of numbers and returns a 2D list of integers representing the grid.

    Args:
        fname (str): The file name to read from.

    Returns:
        List[List[int]]: A 2D list of integers representing the grid in the file.

    Examples:
        >>> grid = ingest_file("grid.txt")
        >>> grid
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    with open(fname, "r") as f:
        lines = f.readlines()

    lines = [l.strip() for l in lines]
    grid = [[*l] for l in lines]
    grid = [[int(char) for char in line] for line in lines]
    return np.asarray(grid)

def get_tree_directions(i: int, j: int, grid: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Returns the elements in the grid to the left, right, up, and down of the element at index i, j.

    Args:
        i (int): The row index of the element.
        j (int): The column index of the element.
        grid (np.ndarray): The 2D grid of elements.

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: A tuple containing the elements to the
            left, right, up, and down of the element at index i, j. The left and up directions are
            returned in reverse order.

    Examples:
        >>> grid = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> get_tree_directions(0, 0, grid)
        (np.array([]), np.array([2, 3]), np.array([]), np.array([4, 7]))
    """

    height, width = grid.shape

    if j == 0:
        left = np.array([])
    else:
        left = grid[i, :j]

    if j == width - 1:
        right = np.array([])
    else:
        right = grid[i, j + 1:]

    if i == 0:
        up = np.array([])
    else:
        up = grid[:i, j]

    if i == height - 1:
        down = np.array([])
    else:
        down = grid[i + 1:, j]

    return np.flip(left), right, np.flip(up), down

def scan_tree_grid(grid: np.ndarray) -> int:
    """
    Returns the number of trees that are visible from the border of the grid.

    Args:
        grid (np.ndarray): The 2D grid of trees.

    Returns:
        int: The number of trees that are visible from the border of the grid.

    Examples:
        >>> grid = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> scan_tree_grid(grid)
        7
        >>> grid = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
        >>> scan_tree_grid(grid)
        1
    """
    height, width = grid.shape

    visible_trees = 0

    for i in range(height):
        for j in range(width):
            current_tree = grid[i][j]

            left, right, up, down = get_tree_directions(i, j, grid)

            if all(current_tree > tree for tree in left):
                visible_trees += 1
                continue

            if all(current_tree > tree for tree in right):
                visible_trees += 1
                continue

            if all(current_tree > tree for tree in up):
                visible_trees += 1
                continue

            if all(current_tree > tree for tree in down):
                visible_trees += 1
                continue

    return visible_trees

def find_distance_viewed(current_tree: int, tree_row: np.ndarray) -> int:
    """
    Returns the distance from the current tree to the nearest tree of equal or taller height in the tree_row.

    Args:
        current_tree (int): The height of the current tree.
        tree_row (np.ndarray): A row or column of trees in the grid.

    Returns:
        int: The distance from the current tree to the nearest tree of equal or taller height in the tree_row.

    Examples:
        >>> find_distance_viewed(3, [1, 2, 3, 4, 5])
        3
        >>> find_distance_viewed(4, [9, 8, 7])
        1
    """

    ct = 0
    for tree in tree_row:
        ct += 1
        if tree >= current_tree:
            break

    return ct

def calculate_scenic_score(grid: np.ndarray) -> Tuple[int, int, int]:
    """
    Returns the location and scenic score of the tree with the highest scenic score in the grid.

    Args:
        grid (np.ndarray): The 2D grid of trees.

    Returns:
        Tuple[int, int, int]: A tuple containing the row and column indices of the tree with the
            highest scenic score, as well as the value of the scenic score.

    Examples:
        >>> grid = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> calculate_scenic_score(grid)
        (1, 1, 1)
    """
    height, width = grid.shape
    top_score = 0
    top_score_location = None
    for i in range(height):
        for j in range(width):
            current_tree = grid[i][j]

            left, right, up, down = get_tree_directions(i, j, grid)

            left_ct = find_distance_viewed(current_tree, left)
            right_ct = find_distance_viewed(current_tree, right)
            up_ct = find_distance_viewed(current_tree, up)
            down_ct = find_distance_viewed(current_tree, down)

            current_tree_score = left_ct * right_ct * up_ct * down_ct

            if current_tree_score > top_score:
                top_score = current_tree_score
                top_score_location = i, j

    return top_score_location[0], top_score_location[1], top_score

if __name__ == "__main__":
    main()