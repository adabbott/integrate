"""
This file contains the implementation of the Simpson rule
"""

import numpy as np


def evaluate(bounds, func):
    """
    Evaluates simpsons rule on an array of bounds and a function pointer. 
    (latex code)

    Parameters
    ----------
    bounds : array_like   
        An array with a dimension of two containing the lower and upper bounds
        of the integration
    func : function
        The integrand. 

    Returns
    -------
    integral : float
        The integral of the function between the bounds.
    """
    if len(bounds) != 2:
        raise ValueError("Bounds should be a length of two, found %d." % len(bounds))
    a = bounds[0]
    b = bounds[1]
    ya = func(a)
    yb = func((a + b) / 2.0)
    yc = func(b)
    integral = (b - a) * (ya + 4 * yb + yc) / 6.0
    return integral 
