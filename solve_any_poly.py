import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def symbolic_fn(coef):
  """
  Generating function using coefficients
  The function takes the list of input coefficients and generate Symbolic function
  """
  sym_fun=0
  x=sym.Symbol('x')
  for i,val in enumerate(coef):
    sym_fun=sym_fun+coef[-1-i]*x**i
  return sym_fun


def evaluate_sym_exp(exp, value):
    """Evaluating the symbolic function"""
    return exp.subs(list(exp.free_symbols)[0], value)


def newtons_method(fn):
  """
  Newtons Method
  The function takes a symbolic expression as the input and gives one root of the function as output
  """
  n=0
  x=1
  while n < 10:
    fn_val=evaluate_sym_exp(fn, x)
    dif_fn_val=evaluate_sym_exp(sym.diff(fn), x)
    x = x - (fn_val/dif_fn_val)
    n = n + 1
  return round(x)


def synthetic_division(coef,root):
  """
  Synthetic Division
  It takes one of the roots of n-degree polynomial and outputs a polynomial of n-1 degree
  """
  quotient=[]
  val=coef[0]
  for i,j in enumerate(coef):
    if i==0:
      quotient.append(coef[i])
    else:
      val=val*root+coef[i]
      quotient.append(val)
  quotient.pop()
  return (quotient)


def solve_any_poly(coef):
  """
  Solving Polynomial
  The function takes the list of coefficients of the polynomial of any degree
  and outputs list of all roots of the given polynomial
  """
  roots=[]
  for i,j in enumerate(coef):
    while len(coef)>2:
      fn = symbolic_fn(coef)
      root=newtons_method(fn)
      roots.append(root)
      coef=synthetic_division(coef,root)
  return roots + [-coef[-1]]


def plot_fn(coef, roots):
    """
    Plotting the graph of the polynomial with solution
    coefficient of the equation
    """
    # compile equation into a symbolic expression
    sym_exp = symbolic_fn(coef)
    # plot equation with roots
    plt.figure(figsize=(20, 8))
    plt.axhline(0, color='b')
    plt.axvline(0, color='b')
    X = np.linspace(-3, 12, 100, endpoint=True)
    y_eval = [ evaluate_sym_exp(sym_exp, xi) for xi in X ]
    plt.plot(X, y_eval)

    # mark roots in graph
    plt.scatter(roots, np.zeros_like(roots))

    # annotate roots
    for i in roots:
      plt.annotate(i, (i, -1))

    plt.title(sym_exp)
    plt.xlabel('x', fontsize=15)
    plt.ylabel('y', fontsize=15)
    #plt.grid()
    plt.show()


if __name__ == '__main__':
    #coeff = [1, -14, 33, 80, -100]
    coeff_str = str(input('Enter Coefficients of Equation (comma separated):'))
    coeff = [ int(item) for item in coeff_str.replace(' ', '').split(',') ]
    roots = solve_any_poly(coeff)
    plot_fn(coeff, roots)
