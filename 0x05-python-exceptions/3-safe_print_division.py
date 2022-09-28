#!/usr/bin/python3

def safe_print_division(a, b):
    """safe_print_division tries a safe print division

    Arguments:
        a -- first arg
        b -- second arg

    Returns:
        the division
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
