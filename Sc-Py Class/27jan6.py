import cmath

def solve_quad(a, b, c):
    #calculate the discriminant
    disc = cmath.sqrt(b**2 - 4*a*c)

    #calculate the solutions
    sol1 = (-b + disc) / (2*a)
    sol2 = (-b - disc) / (2*a)

    return sol1, sol2

a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter the coefficient of x: "))
c= int(input("Enter the constant: "))

print(solve_quad(a, b, c))