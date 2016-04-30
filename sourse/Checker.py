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
        return (False, sympy.ode.dsolve(ode) )
    else : return (True, 0)
  


