def fixed_point_iteration(x0: float, tol: float = 1.e-6, max_iter: int = 100) -> float:
    """
    Finds the root of a function using the fixed-point method.
    f(x) and g(x) must be written by manually.

    Parameters:
        x0 (float): The initial guess for the root.
        tol (float): The tolerance of the method.
        max_iter (int): The maximum number of iterations.

    Returns:
        float: The root.
    """

    def f(x: float) -> float:
        return (x+1)**0.5 - x

    def g(x: float) -> float:
        return (x+1)**0.5
    
    x = x0

    for i in range(max_iter):
        x_new = g(x)

        if abs(f(x)) <=  tol:
            print("f(x) <= tolerance")
            break
        elif abs(x_new - x) <= tol:
            print("|x(n) − x(n−1)| <= tolerance")
            break

        x = x_new

    return x


if __name__ == "__main__":
    x0 = 25.0
    tolerance = 1.e-8
    max_iteration = 250
    print(fixed_point_iteration(x0, tolerance, max_iteration))