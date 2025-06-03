class Matrix:
    def __init__(self, data: list[list[float]]):
        """Initialize a matrix from a list of lists."""
        self.data = [row[:] for row in data]  # Create a deep copy
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    

    def __repr__(self):
        """String representation of the matrix."""
        return str(self.data)


def matrix(data: list[list[float]]) -> Matrix:
    """
    Create a matrix from a 2D list representing the matrix data.
    
    Args:
        data (list[list[float]]): 2D list representing the matrix data.
    
    Returns:
        Matrix: Matrix object
    """
    return Matrix(data)

# Export the matrix function for external use
__all__ = ["matrix"]
