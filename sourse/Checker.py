# Author: Rusanov jrojer Aleksei
# Checker.py; 
# 2016-04-06 18:11; 

import sympy

def Check( ode, sol):
    """ 
    returns   : tupple(bool, sympy.Eq) 
    arguments : sympy.Eq ode, sympy.Eq sol 
    """
    res = sympy.ode.checkodesol(ode, sol, solve_for_func=False)
    if res[0] == False :
        print('>>> Incorrect solution')
        print('>>>> Solving ... ')
        return (False, sympy.ode.dsolve(ode) )
    else :
        print('>>> Solution is Correct')
        return (True, 0)
  


