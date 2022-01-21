"""
This file defines the password that we want to crack and the function that checks
if the password is correct.
"""

from time import process_time_ns

C = ''  # The password to guess, it will be initialized randomly later.


def match(password):
    """
    This function was provided by the exercise.
    There are two things to point out:
    - The variable c is not passed into the function but it is instead a global
    variable. This does not change how the function work, it is just in order not
    to pass the variable across many functions.
    - Two useless while where added. This again does not change how the function works,
    or the relative cost of the single operations in terms of time but it allows to use
    real system time instead of a fake one. That is because when we are measuring the time
    of the process, the operations in the match function are too simple to be relevant and
    to keep track  of, even using nanoseconds. Adding those while we are scaling times in order
    to be able to track them, maybe it is not the most elegant solution, but I did not find valid
    alternatives.
    :param password: The password that we are trying to see if is correct.
    :return: It returns a tuple, the first item is a bool that says if the password p is correct
    or not, the second value is the time required for the execution of the whole function.
    """
    time = process_time_ns()

    value = True

    if len(C) != len(password):
        value = False

    if value:
        for i, _ in enumerate(C):
            k = 0
            while k < 1500:
                if C[i] != password[i]:
                    j = 0
                    while j < 1500:
                        value = False
                        j += 1
                k += 1

    return value, process_time_ns() - time
