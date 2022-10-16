#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a/ b
        print("{} / {} = {}".format(a, b, div))
    except ZeroDivisionError:
        div = "None"
        print("{} / {} = {}".format(a, b, div))
    finally:
        print("Inside result: {}".format(div))
