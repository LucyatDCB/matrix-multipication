# Function to input a matrix from user
def input_matrix():
    # Ask user for dimensions of the matrix
    rows, cols = map(int, input("Enter the number of rows and columns (e.g., '3 3' for a 3x3 matrix): ").split())
    
    # Initialize an empty matrix
    matrix = []

    # Iterate over each row
    for i in range(rows):
        # Ask user for elements of the current row
        row_input = input("Enter {cols} numbers separated by space for row {i + 1}: ")
        
        # Split the input and convert elements to integers
        row = list(map(int, row_input.split()))
        
        # Check if the number of elements matches the specified number of columns
        if len(row) != cols:
            print("Invalid input! Please enter exactly", cols, "numbers.")
            return None
        
        # Add the row to the matrix
        matrix.append(row)
    
    return matrix

# Function to multiply two matrices
def matrix_multiply(A, B):
    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_A, col_B)) for col_B in zip(*B)] for row_A in A]
    return result

# Input Matrix A
print("Enter Matrix A:")
A = input_matrix()

# Input Matrix B
print("Enter Matrix B:")
B = input_matrix()

# Check if matrices can be multiplied
if len(A[0]) != len(B):
    print("Matrices cannot be multiplied! Number of columns of Matrix A must be equal to number of rows of Matrix B.")
else:
    # Multiply matrices and display result
    result = matrix_multiply(A, B)
    print("Resultant Matrix:")
    for row in result:
        print(row)
