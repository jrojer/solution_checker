# Author: Rusanov jrojer Aleksei
# ParseTex.py; 
# 2016-03-31 18:02; 

def FindFuncAndVar(fo):

    function = ''
    variable = ''
    func_found = False
    var_found  = False

    line = fo.readline()
    #print ('> line', line )
    while ( line != '' ):
        if line.strip() == 'Function:':
            fo.readline() # skip $$
            function = fo.readline().strip()
            fo.readline() # skip $$
            func_found = True

        if line.strip() == 'Variable:':
            fo.readline() # skip $$
            variable = fo.readline().strip()
            fo.readline() # skip $$
            var_found = True

        if func_found and var_found:
            return [function, variable]

        line = fo.readline()
        #print ('> line', line )

    return ['',''] 

def ParseTex(fo):
    equation = ''
    solution = ''

    ode_found = False
    sol_found = False

    line = fo.readline()
    #print ('> line', line )
    while ( line != ''  ):

        if line.strip() == 'Equation:':
            fo.readline() # skip $$
            equation = fo.readline().strip()
            fo.readline() # skip $$
            ode_found = True
        if line.strip() == 'Solution:':
            fo.readline() # skip $$
            solution = fo.readline().strip()
            fo.readline() # skip $$
            sol_found = True

        if ode_found and sol_found:
            yield [equation, solution]
            ode_found = False
            sol_found = False
            equation = ''
            solution = ''

        line = fo.readline()
        #print ('> line', line )
        

if __name__ == '__main__':
    fo = open( './test.tex','r')
    print ( FindFuncAndVar(fo) )
    for x in ParseTex(fo):
        print (x)
    fo.close()
