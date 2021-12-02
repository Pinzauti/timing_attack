import random
import string
import matplotlib.pyplot as plt
import attack
import target


def stats(length):
    """
    This is necessary in order to plot the graph. We are generating random password to guess and then trying to guess
    them.
    :param length: The actual length of c, that then we will try to guess.
    :return: It returns the time that was necessary to crack the password.
    """
    target.c = ''.join(random.choices(string.ascii_lowercase, k=length))
    print('The password of length %d to guess is %s' % (int(length), target.c))
    result = attack.attack(attack.guess_length())[0]
    time = attack.attack(attack.guess_length())[1]
    print('The guessed password of length %d is %s and it required %d nanoseconds to crack it' % (int(length), result,
                                                                                                  int(time)))
    if target.c == result:
        return time


x = [1, 2, 3, 4, 5]
y = [stats(1), stats(2), stats(3), stats(4), stats(5)]
plt.plot(x, y)
plt.xlabel('Length')
plt.ylabel('Time')
plt.title('Timing attack')
plt.show()
