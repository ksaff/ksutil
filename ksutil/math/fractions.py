# coding: utf-8
"""
Fraction convenience functions
"""


def gcf(a, b):
    """Get greatest common factor of two numbers using Euclidean algorithm."""
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return gcf(b, a % b)
    else:
        return gcf(a, b % a)


def fractionify(n):
    """
    Get numerator and base 10 denominator from a decimal number. Rational 
    number expected.
    """
    i = 0
    while True:
        if not n * 10 ** i % 1:
            break
        i += 1
    return n * 10 ** i, 10 ** i


def reduce(nume, denom):
    """Reduce fraction"""
    factor = gcf(nume, denom)
    return nume / factor, denom / factor


def fractionify_and_reduce(n):
    """Get a reduced fraction from a decimal number."""
    nume, denom = fractionify(n)
    return reduce(nume, denom)


def print_hole_center_distance(d1, d2, spacing=0.25):
    total = spacing + d1 / 2 + d2 / 2
    print "{}/{}".format(*fractionify_and_reduce(total))
