from latex2sympy.process_latex import process_sympy
import sympy
from sympy import Function,Derivative, Symbol, E,pi


def SimpleIdentify( ode , sol , func, var ):
    # name function in ode and sol
    # sympy.Equation ode,sol
    # str func, var

    f   = Function(func)(Symbol(var))
    df  = Symbol('d'+func)
    v   = Symbol(var)
    dv  = Symbol('d'+var)

    ode = ode.subs(Symbol(func),f)
    sol = sol.subs(Symbol(func),f)

    ode = ode.subs(df,Derivative(f,v)*dv)
    sol = sol.subs(df,Derivative(f,v)*dv)

    sol = sol.subs(Symbol('e'),E)
    ode = ode.subs(Symbol('e'),E)
    sol = sol.subs(Symbol('\\pi'),pi)
    ode = ode.subs(Symbol('\\pi'),pi)

    return (ode,sol)


def ProcessData(data):

    # str list[4] data

    ode  = process_sympy( data[0] )
    sol  = process_sympy( data[1] )
    func = data[2] 
    var  = data[3]

    #Print_data_before_identification(ode,sol)

    return SimpleIdentify(ode ,sol, func, var)
    #id_ret = identify_symbols(ode, sol) TODO

