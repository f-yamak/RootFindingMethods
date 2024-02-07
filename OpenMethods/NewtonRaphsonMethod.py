def newton_raphson_iteration(x0: float, tol: float = 1.e-6, max_iter: int = 100) -> float:
    """
    Finds the root of a function using the Newton-Raphson method.
    f(x) must be written by manually.

    Parameters:
        x0 (float): The initial guess for the root.
        tol (float): The tolerance of the method.
        max_iter (int): The maximum number of iterations.

    Returns:
        float: The root.
    """

    def f(x: float) -> float:
        return (2*(x**4)) + (5*(x**3)) - (3*(x**2)) - 1
     
    def f_derivative(x: float) -> float:
        """
        Calculates the derivative of f(x) using the Central 
        Difference Approximation, a numerical derivative method

        Parameters:
            x (float): The point at which the derivative is calculated. 

        Returns:
            float: Derivative of f(x)
        """
        h = 0.1
        return (f(x + (h/2)) - f(x - (h/2))) / h
    
    x = x0

    for i in range(max_iter):
        x_new = x - (f(x) / f_derivative(x))
        print(f"f(x): {f(x)} \t\t f'(x): {f_derivative(x)}")

        if abs(f(x)) <=  tol:
            print("f(x) <= tolerance")
            break
        elif abs(x_new - x) <= tol:
            print("|x(n) − x(n−1)| <= tolerance")
            break
        
        x = x_new

    return x



if __name__ == "__main__":
    x0 = -10
    tolerance = 1.e-8
    max_iteration = 250
    print(newton_raphson_iteration(x0, tolerance, max_iteration))