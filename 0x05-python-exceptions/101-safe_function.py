#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ZeroDivisionError, TypeError, ValueError, IndexError) as err:
        import sys
        print("Exception: {}".format(err), file=sys.stderr)
        return None
