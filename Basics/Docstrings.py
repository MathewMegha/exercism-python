# An example from PEP257 of a multi-line docstring.
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """

    if imag == 0.0 and real == 0.0:
        return complex_zero
    

"""
1. robots can real docstring by,
 Sphinx is a tool that:

Goes through ALL your code
Reads all the docstrings
Automatically builds a beautiful website with all the instructions!

Think of it like:

"A robot reads all your instruction booklets and makes a giant help manual!"

2. Asking Python to show the docstring
pythonprint(raise_to_power.__doc__)

.__doc__ is like asking:


"Hey Python, show me the instruction booklet for this function!"

And Python prints it out.
"""


    
"""
explaining an additional toipc:
# Calling methods or functions in classes and modules.
>>> start_text = "my silly sentence for examples."
>>> str.upper(start_text)  # Calling the upper() method from the built-in str class on start_text.
'MY SILLY SENTENCE FOR EXAMPLES.'


# Importing the math module
import math

>>> math.pow(2,4)  # Calling the pow() function from the math module
16.0

"""