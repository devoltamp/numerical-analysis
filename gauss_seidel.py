import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=100):
    """
    Solve Ax = b using Gauss-Seidel iteration.
    
    Args:
        A: n x n coefficient matrix.
        b: n-length right-hand side vector.
        x0: Initial guess (defaults to zeros).
        tol: Convergence tolerance (||x_new - x_old||).
        max_iter: Maximum iterations.
    
    Returns:
        Solution vector x, number of iterations used.
    """
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    x = x0.copy().astype(float)
    
    for iteration in range(1, max_iter + 1):
        x_old = x.copy()
        
        # Update each variable using latest values
        for i in range(n):
            # Sum lower triangle (new values) + upper (old values)
            s = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x_old[i+1:])
            x[i] = (b[i] - s) / A[i, i]  # Assume diagonal != 0
        
        # Check convergence
        error = np.linalg.norm(x - x_old)
        if error < tol:
            return x, iteration
        
    print("Warning: Maximum iterations reached without convergence.")
    return x, max_iter


A = np.array([[4, 1, 2],
              [3, 5, 1],
              [1, 1, 3]], dtype=float)
b = np.array([4, 7, 3], dtype=float)

solution, iterations = gauss_seidel(A, b)
print("Solution:", solution)
print("Converged in", iterations, "iterations")