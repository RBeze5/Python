#Import SymPy
import sympy as sp
#Define Symbols
x, y = sp.symbols('x y')
#Perform Symbolic Operations
#a) Simplify expressions
expression = (x**2 + 2*x + 1) / (x + 1)
simplified_expression = sp.simplify(expression)
print(simplified_expression)
#b) Solve equations
equation = x**2 - 4
solutions = sp.solve(equation, x)
print(solutions)
#c) Differentiate and integrate
expression = x**3 + 2*x**2 + x
derivative = sp.diff(expression, x)
integral = sp.integrate(expression, x)
print(derivative)
print(integral)
#d) Solve systems of equations
eq1 = 2*x + y - 5
eq2 = x - y + 1
solutions = sp.solve((eq1, eq2), (x, y))
print(solutions)
#Display Results
display(simplified_expression)
