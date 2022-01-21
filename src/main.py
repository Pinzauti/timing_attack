"""
This file plots the graph.
"""
import random
import string
import matplotlib.pyplot as plt
import attack
import target


def stats(length):
    """
    This is necessary in order to plot the graph. We are generating random password to
    guess and then trying to guess them.
    :param length: The actual length of c, that then we will try to guess.
    :return: It returns the time that was necessary to crack the password.
    """
    target.C = ''.join(random.choices(string.ascii_lowercase, k=length))
    print(f'The password of length {int(length)} to guess is {target.C}')
    result = attack.attack(attack.guess_length())[0]
    time = attack.attack(attack.guess_length())[1]
    print(f'The guessed password of length {int(length)} is {result} and it required {int(time)}'
          f' nanoseconds to crack it')
    if target.C == result:
        return time
    return 0


x = [1, 2, 3, 4, 5]
y = [stats(1), stats(2), stats(3), stats(4), stats(5)]
plt.plot(x, y)
plt.xlabel('Length')
plt.ylabel('Time')
plt.title('Timing attack')
plt.show()
