import math

def secant_iteration(x0: float, x1: float, tol: float = 1.e-6, max_iter: int = 100) -> float:
    """
    Finds the root of a function using the secant method.
    f(x) must be written by manually.

    Parameters:
        x0 (float): The first initial value.
        x1 (float): The second initial value.
        tol (float): The tolerance of the method.
        max_iter (int): The maximum number of iterations.

    Returns:
        float: The root.
    """

    def f(x: float) -> float:
        return x - math.cos(x)

    for i in range(max_iter):
        x_new = x1 - (f(x1) * (x1-x0) / (f(x1) - f(x0)))

        if abs(f(x1)) <= tol:
            print("f(x1) <= tolerance")
            break
        elif abs(x1-x0) <= tol:
            print("|x1 - x0| <= tolerance")
            break
        
        x0 = x1
        x1 = x_new

    return x_new

if __name__ == "__main__":
    x0 = 20
    x1 = 21
    tolerance = 1.e-8
    max_iteration = 250
    print(secant_iteration(x0, x1, tolerance, max_iteration))