# solution_checker
Differential Equation Solution Checker 
For now it works on Windows OS only
What is it:
  An input file is a LaTeX source file with .tex extension, containing ODEs (Ordinary Differential Equations) and corresponding solutions.
  The application reads the input file. 
  Then it uses latex2sympy to convert LaTeX expressions to sympy expressions. 
  Then the applications creates an output file as a LaTeX source file.
  Then it checks wether the given equation is a solution for the ODE and prints result to the output file. If the given solution is incorrect, the application solves the ODE and prints the correct solution.
  Then it uses "pdflatex.exe" to create the .pdf file out of .tex file containing results.
  Finally it opens .pdf file with default .pdf viewer.
   
   For an example of input file see "sample_input.tex" file.
