def false_position_iteration(a: float, b: float, tol: float = 1.e-6, max_iter: int = 100) -> float:
    """
    Finds the root of a function using the false-position method.
    f(x) must be written by manually.

    Parameters:
        a (float): The first endpoint value.
        b (float): The second endpoint value.
        tol (float): The tolerance of the method.
        max_iter (int): The maximum number of iterations.

    Returns:
        float: The root.
    """

    def f(x: float) -> float:
        return (x**3) + (x**2)- (4*x) - 3

    if (f(a) < 0 and f(b) < 0) or (f(a) > 0 and f(b) > 0):
        raise "The signs of f(a) and f(b) must be different from each other"
    if a > b:
        a,b = b,a

    for i in range(max_iter):
        c = b - ( f(b) * (b-a) / (f(b)-f(a)) )

        if abs(f(c)) <= tol:
            print("f(c) <= tolerance")
            break
        elif abs(b-a) <= tol:
            print("|b - a| <= tolerance")
            break

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return c


if __name__ == "__main__":
    a = 0
    b = 10
    tolerance = 1.e-8
    max_iteration = 250
    print(false_position_iteration(a,b, tolerance, max_iteration))