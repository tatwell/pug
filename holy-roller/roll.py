"""
    holy-roller.py

    A simple command-line dice-rolling application.

    USAGE:
    python holy-roller/roll.py [num die sides]
"""
import sys
import random

from bag.bag_of_dice import four_sided_die, six_sided_die, ten_sided_die, twenty_sided_die


def roll(die):
    return random.choice(die)

def main(args):
    sides = args[0]

    if sides == '4':
        result = roll(four_sided_die)
    elif sides == '6':
        result = roll(six_sided_die)
    elif sides == '10':
        result = roll(ten_sided_die)
    elif sides == '20':
        result = roll(twenty_sided_die)
    else:
        raise ValueError('Die not found!')

    print "Taking up your trusty %s-sided die, you roll a %d" % (sides, result)


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
