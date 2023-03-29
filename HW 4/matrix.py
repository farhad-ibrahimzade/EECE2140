import pickle

class Matrix:

    def __init__(self, elements: list):
        """Create a new matrix from a 2D list

        Args:
            elements (list): 2D List
        """
        self.elements = elements
        self.dim = (len(elements), len(elements[0]))

    def __add__(self, other):
        """Add two matrices of the same size

        Args:
            other (Matrix): matrix to add

        Raises:
            ValueError: If matrix dimensions don't match
            ValueError: If other object is not a matrix

        Returns:
            Matrix: Sum of two matrices
        """
        if (Matrix.is_matrix(other)):
            if(self.dim == other.dim):
                result = Matrix([[0 for j in range(self.dim[1])] for i in range(self.dim[0])])
                for i in range(len(self.elements)):
                    for j in range(len(self.elements[0])):
                        result.elements[i][j] = self.elements[i][j] + other.elements[i][j]

            else:
                raise ValueError("The matrices do not have the same dimensions")
        
        else:
            raise ValueError("Object must be of type Matrix")
        
        return result

    def __sub__(self, other):
        """Substracts two matrices of the same size

        Args:
            other (Matrix): matrix to substract

        Raises:
            ValueError: If matrix dimensions don't match
            ValueError: If other object is not a matrix

        Returns:
            Matrix: Difference of two matrices
        """
        if (Matrix.is_matrix(other)):
            if(self.dim == other.dim):
                result = Matrix([[0 for j in range(self.dim[1])] for i in range(self.dim[0])])
                for i in range(len(self.elements)):
                    for j in range(len(self.elements[0])):
                        result.elements[i][j] = self.elements[i][j] - other.elements[i][j]

            else:
                raise ValueError("The matrices do not have the same dimensions")

        else:
            raise ValueError("Object must be of type Matrix")
        
        return result

    def __mul__(self, other):
        """Multiply two matrices with appropriate dimensions

        Args:
            other (Matrix): matrix to multiply by

        Raises:
            ValueError: If matrix dimensions are inappropriate
            ValueError: If other object is not a matrix

        Returns:
            Matrix: Product of two matrices
        """
        if (Matrix.is_matrix(other)):
            if(self.dim[1] == other.dim[0]):
                result = Matrix([[0 for j in range(other.dim[1])] for i in range(self.dim[0])])
                for i in range(len(self.elements)):
                    for j in range(len(other.elements[0])):
                        product = 0
                        for k in range(len(self.elements[0])):
                            product += self.elements[i][k] * other.elements[k][j]

                        result.elements[i][j] = product

            else:
                raise ValueError("The number of columns of the first matrix must be equivalent \
                                to the number of rows of the second matrix")
        
        else:
            raise ValueError("Object must be of type Matrix")
        return result

    def __eq__(self, other) -> bool:
        """Check if two matrices are equivalent

        Args:
            other (Matrix): matrix to check against

        Raises:
            ValueError: If other object is not a Matrix

        Returns:
            bool: Result of the operation
        """
        if (Matrix.is_matrix(other)):
            if(self.dim == other.dim):
                result = True
                for i in range(len(self.elements)):
                    for j in range(len(self.elements[0])):
                        result = (self.elements[i][j] == other.elements[i][j])

            else:
                return False

        else:
            raise ValueError("Object must be of type Matrix")
        return result

    def __len__(self) -> int:
        """Returns the number of elements in the matrix

        Returns:
            int: Number of elements in matrix
        """
        return self.dim[0]*self.dim[1]

    def __str__(self) -> str:
        """Returns the matrix as a string

        Returns:
            str: matrix as a string
        """
        string = []
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                string.append(str(self.elements[i][j]))
                if j < (self.dim[1] - 1):
                    string.append(", ")
            string.append("\n")

        return "".join(string)

    def transpose(self):
        """Returns the transpose of the matrix

        Returns:
            Matrix: transpose of the matrix
        """
        result = Matrix([[0 for j in range(self.dim[0])] for i in range(self.dim[1])])
        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                result.elements[j][i] = self.elements[i][j]
        return result

    def is_matrix(A) -> bool:
        """Checks if the object is a matrix

        Args:
            A (any): object to check

        Returns:
            bool: Result of the operation
        """
        return isinstance(A, Matrix)

    def sort(self, reverse=False):
        """Sort a matrix and return it as a 1D list

        Args:
            reverse (bool, optional): Reverse order. Defaults to False.

        Returns:
            list: Sorted matrix as 1D array
        """
        output = []
        for row in self.elements:
            output.extend(row)

        return sorted(output, reverse=reverse)
            
    def save(self, filename: str):
        """Saves matrix to binary file

        Args:
            filename (str): Binary file name
        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    def load(self, filename: str):
        """Read matrix from binary file

        Args:
            filename (str): Binary file name

        Returns:
            Matrix: Matrix object
        """
        with open(filename, "rb") as f:
            return pickle.load(f)

    
