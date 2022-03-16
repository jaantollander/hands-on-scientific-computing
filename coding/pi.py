import random
import decimal


# --- Chudnovsky Aslgorithm ---
# Source for Chudnovsky algorithm:
# https://gist.github.com/thebecwar/b53f3a9b6e0428a40b27d99745c794a8

def fact(n):
    m = 1
    for i in range(1, n+1):
        m *= i
    return m

def den(k):
    a = decimal.Decimal(fact(6*k)*(545140134*k+13591409))
    b = decimal.Decimal(fact(3*k)*(fact(k)**3)*((-262537412640768000)**k))
    res = a / b
    if k > 0:
        return res + den(k - 1)
    else:
        return res

def num():
    d = decimal.Decimal(10005).sqrt()
    return 426880 * decimal.Decimal(10005).sqrt()
    

def chudnovsky(precision):
    k = 10 * precision
    decimal.getcontext().prec = precision + 1
    return num()/den(k)


# -- Monte Carlo pi ---

def is_in_circle(x, y):
    return x**2 + y**2 <= 1

def points_in_circle(iterations, n):
    count = 0
    for i in range(iterations):
        x = random.random() 
        y = random.random()
        if is_in_circle(x, y):
            count += 1
    return count 

def monte_carlo_pi(iterations, n):
    return 4*points_in_circle(iterations, n)/iterations

if __name__ == "__main__":
    pass
