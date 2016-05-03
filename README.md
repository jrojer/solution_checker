# solution_checker

Differential Equation Solution Checker 

For now it works on Windows OS only
  
How it works:
  1. User tells the app where the pdflatex.exe and input file are. The the user hits "Run" button.
  2. The app verifies the input file. The input file must be compilable .tex file.
  3. App opens input file, creates and initializes output file.
  4. The input file is read line by line. Firstly a function and variable symbol identified (see sample_input.tex).  
  5. ODE and solution are read as str objects and then converted to sympy objects.
  6. Function symbol substituted with function object.
  7. Check wether the equation is a solution of the ODE and output printed to the output tex file. If the equation is not a solution then the correct solution is printed.
  8. If no errors occured, pdf file is made out of output tex file and default pdf viewer launched to show the pdf.
  
   
  For an example of input file see "sample_input.tex" file.
