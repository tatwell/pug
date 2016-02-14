"""
FizzBuzz

Write a program that prints the numbers from 1 to 100. But for multiples of three
print "Fizz" instead of the number and for the multiples of five print "Buzz". For
numbers which are multiples of both three and five print "FizzBuzz".

Source: http://c2.com/cgi/wiki?FizzBuzzTest
"""
import sys


def is_fizz(number):
    return number % 3 == 0

def is_buzz(number):
    return number % 5 == 0

def is_fizzbuzz(number):
    return is_fizz(number) and is_buzz(number)

def fizzbuzz_number(number):
    if is_fizzbuzz(number):
        return 'FizzBuzz'
    elif is_fizz(number):
        return 'Fizz'
    elif is_buzz(number):
        return 'Buzz'
    else:
        return number

def fizzbuzz(n):
    for n in range(1,n+1):
        print fizzbuzz_number(n)

def tests():
    cases = [
        # (number, expected)
        (1, 1),
        (3, 'Fizz'),
        (5, 'Buzz'),
        (15, 'FizzBuzz'),
        (100, 'Buzz')
    ]

    for number, expected in cases:
        assert fizzbuzz_number(number) == expected, "Failed for %s == %s" % (number, expected)

    print 'Test passed for cases: %s' % (cases)

def usage():
    print """
    USAGE
    To run fizzbuzz 1 to 100.:
        python fizzbuzz.py 100

    To run tests:
        python fizzbuzz.py test
"""

if __name__ == '__main__':
    # Default: run usage
    request = sys.argv[1] if len(sys.argv) > 1 else 'default'

    if request.isdigit():
        fizzbuzz(int(request))
    elif request == 'test':
        tests()
    else:
        usage()
