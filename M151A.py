from math import *
import sys
#sys.path.append('/Users/havenville/miniconda3/lib/python3.8/site-packages/')
import sympy as sym


# generate derivatives

x = sym.symbols('x')    # since x is our only variable symbol here

# generate derivatives
#deriv_0 = '1 - 4*x*cos(x) + 2*x**2 + cos(2*x)'  # aka original
deriv_0 = 'exp(x) + 2**(-x) + 2*cos(x) - 6'
deriv_1 = sym.diff(deriv_0, x)
deriv_2 = sym.diff(deriv_1, x)

f = sym.lambdify(x, deriv_0)   # original
fp = sym.lambdify(x, deriv_1)   # first derivative
fpp = sym.lambdify(x, deriv_2)

mu = lambda x: f(x) / fp(x)     #f(x)/fp(x) by definition
mup = lambda x: ( fp(x)*fp(x) - f(x)*fpp(x) ) / fp(x)**2    # quotient rule

# different numerical analysis methods

def bisection(a, b, N, acc):
    i = 1
    accuracy = pow(10, acc)
    p =  -1
    while i < N:
        
        # print(str(i) + " iteration")
        
        p = a+(b-a)/2

        result = f(p)
        print('result: ' + str(result))

        # if within accuracy range
        if  abs(result) < accuracy:
            print("bisection root is: " + str(p))
            print("error: " + str(result))
            print("iterations: " + str(i))
            return

        # iterative case
        if result > 0:
            b = p
        elif result < 0:
            a = p
        i += 1

    print("Max iteration " + str(N) + " reached.")


def fixed_point(low, high, max_iter, acc):
    p_in=low      # starting point (the input to equation)
    accuracy = pow(10,acc)
    for i in range(1, max_iter+1):
        p_out = f(p_in)      # output of the equation
        
        print('In: ' + str(p_in) + ' Out: ' + str(p_out))

        error = abs(p_out-p_in)
        
        if (error < accuracy):        # if error is within accuracy requirement
            print("fixed point is: " + str(p_out))
            print("error = " + str(error))
            print("iterations: " + str(i))
            return
        p_in = p_out
    print("Max iteration " + str(max_iter) + " reached.")
        

def secant_method(a, b, max_iter, acc):
    accuracy = pow(10,acc)
    p0 = a      # taking start to be lower bound
    p1 = a+(b-a)/2      # using bisection to get second point
    
    for i in range(1, max_iter+1):
        p2 = p1 - (f(p1) / (f(p1) - f(p0))) * (p1 - p0)

        #print('(' + str(i) + ')' + ': ' + str(p2))
        
        error = abs(p2-p1)      # again, define error as difference (not how close to 0)

        if (error < accuracy):
            print("secant root is: " + str(p2))
            print("error = " + str(error))
            print("iterations: " + str(i))
            return
        p0 = p1
        p1 = p2

    print("Max iteration " + str(max_iter) + " reached.")


# usually slower than secant method in practice
def false_position_method(a, b, max_iter, acc):
    accuracy = pow(10,acc)
    p0 = a      # taking start to be lower bound
    p1 = a+(b-a)/2
    
    for i in range(1, max_iter+1):
        p2 = p1 - (f(p1) / (f(p1) - f(p0))) * (p1 - p0)

        #print('Out: ' + str(p2))

        error = abs(p2 - p1)
        
        if (error < accuracy):        # if error is within accuracy requirement around 0
            print("false position root is: " + str(p2))
            print("error = " + str(error))
            print("iterations: " + str(i))
            return


        # print("analysis: " + str(f(p1)) + ", " + str(f(p2)))
        
        if (f(p1) * f(p2) < 0):
            p0 = p1
            p1 = p2
            # print("using p1, p2: " + str(p0) + ", " + str(p1))
        else:
            p0 = p0
            p1 = p2
            # print("using p0, p2: " + str(p0) + ", " + str(p1))


    print("Max iteration " + str(max_iter) + " reached.")


def newton(a, max_iter, acc, opt):   
    accuracy = pow(10,acc)
    p0 = a      # random guess within the range
    p1 = -1
    
    for i in range(1, max_iter+1):
        if opt == 0:          # run normal newton
            p1 = p0 - f(p0)/fp(p0)
        elif opt == 1:          # modified
            p1 = p0 - mu(p0)/mup(p0)
        else:
            print("yeah sorry, we don't support that option here")
            return


        print('(' + str(i) + ')' + ': ' + str(p1))

        error = abs(p1 - p0)    # error defined as difference between consecutive terms
                                # not how close to zero it is (since it is a fixed point method)
        
        if (error < accuracy):        # if error is within accuracy requirement around 0
            print("newton root is: " + str(p1))
            print("error = " + str(error))
            print("iterations: " + str(i))
            return

        p0 = p1     # update for next iteration

    print("Max iteration " + str(max_iter) + " reached.")


def testing_before():
    print()

    # bisection method
    print("running bisection")
    print("---------------------------------")
    bisection(5, 0, 100, -15)      # third parameter is max # of iterations
    print()
    # fixed point
    # fixed_point(1, 2, 100, -4)

    # secant method
    print("running secant")
    print("---------------------------------")
    secant_method(0, 5, 100, -5)
    print()

    # method of false position
    print("running false position")
    print("---------------------------------")
    false_position_method(0.5, pi/4, 1000, -5)
    print()


def testing_now():
    print()


    # newton's method
    print("running newton's method")
    print("---------------------------------")
    newton(1, 100, -5, 0)
    print()

    # modified newton's method
    print("running modified newton's method")
    print("---------------------------------")
    newton(1, 100, -5, 1)
    print()

if __name__ == '__main__':
    testing_now()






