"""
This file contains the actual timing attacks machinery.
"""
from time import process_time_ns
import itertools
import random
import string
import target

MAXIMUM = 10  # Max length of password.


def guess_length():
    """
    This function try (with random values) password of different lengths, up to a
    maximum value defined globally. The match function start to compare the single
    characters of the password p only if the length is correct and those comparisons
    require time. Because of that we guess that the right length of the password is when
    tha match function execution require the most time.
    :return: It returns a guess of the password length.
    """
    i = 0
    length_time = []

    while i < MAXIMUM:
        length_time.append(target.match(random.sample(range(MAXIMUM), i))[1])
        i = i + 1

    return length_time.index(max(length_time))


def guess_letter(length, result):
    """
    This function try to guess a single character of the password p. The guess is composed by
    three parts: - The previously guessed characters (i.e. the param result) by this same
    function. - A random character which we now change until we think it is correct. How do we
    know that it is correct? It should be the character that requires the function to run in less
    time. That is because when the character is correct we do not need to set 'value' equal to
    false (an operations which, as all operations do, requires time). This time is scaled by the
    addition of the while loops, but does not change the concept behind it. - Random characters
    that we add in order to respect the password length, but of which we don't care about. In
    order to prevents possible errors in time calculation (i.e. some of this characters might be
    correct, and than there would be a mismatch in time comparisons) it is recommended to use
    characters that we are certain (or we are reasonably sure) can not be find in the actual
    password c.
    :param length: It is the number of characters which we still don't know and we are going to
    guess in this and other iterations.
    :param result: It is a string containing the previous guessed characters by this same function.
    :return: It returns a single character which we think is equal to the one in the same position
    in c (c is the password to guess).
    """
    attack_time = {}
    chars = string.ascii_lowercase
    for item in itertools.product(chars, repeat=1):
        attack_time[''.join(item)] = target.match(result + ''.join(item) +
                                                  ''.join(random.choices(['('], k=length - 1)))[1]
    return min(attack_time, key=attack_time.get)


def attack(length):
    """
    This function start with an empty string and starts to fill it (until its length it is equal
    to the param length) with the characters guessed by the guess_letter function.
    :param length: It is the guessed length of the password, generated by the function guess_length.
    :return: It returns a tuple, the first value is the guess of the password, the second value is
    the time that was necessary to crack it.
    """
    time = process_time_ns()

    result = ''
    while length:
        result += guess_letter(length, result)
        length -= 1

    return result, process_time_ns() - time
