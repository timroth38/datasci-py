'''
Loops and recursion.
'''
from util import *

'''
Exercise 1:
Implement a half-life function that uses a while loop.
f(t) = a * (1/2)^t
'''
def half_life_while(a, t):
    time = 1  
    while t > 0:
        time = 1/2 * time
        t -= 1
    return a * time
    

'''
Exercise 2:
Implement a half-life function that uses a for loop.
'''
def half_life_for(a, t):
    time = 1.0
    for i in range(t):
        time = 1/2 * time
    return a * time
    

'''
Exercise 3:
Implement factorial using recursion.
Recall that n! = n * (n - 1) * ... 1
For simplicity, assume that 0! = (-1)! = 0.
'''
def factorial_recur(n):
    if n == 1:
        return 1
    elif n < 1:
        return 0
    else: 
        return n * factorial_recur(n-1)

'''
Exercise 4:
Implement fibonacci using recursion.
'''
def fib(n):
    fibo = 1
    if n < 1:
        return 0
    elif n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

'''
Exercise 5:
Implement the combination function.
  Recall nCr = n!/((n-r)!r!)

Write your own function and call it combination.
Use the factorial_iter function located in util.py; it has already
  been imported for you so you just need to call factorial_iter(number)
'''
def combination(n, r):
    if r > n:
        return 0
    elif n == 0 or n == r:
        return 1
    else:
        return factorial_iter(n)/(factorial_iter(n-r)*factorial_iter(r))

############################# Test cases ######################################
def test_factorial():
  test_cases = [3, 5, -1, 1, 10]
  print('>>> Testing recursive factorial...')
  for test_case in test_cases:
    recur_val = factorial_recur(test_case)
    iter_val = factorial_iter(test_case)
    if recur_val != iter_val:
      print('{}!\tFAIL: Expected {} but got {}'.format(
            test_case, iter_val, recur_val))
    else:
      print('{}!\tPASS: {}'.format(test_case, recur_val))
  print()

def test_fib():
  test_cases = [1, 2, 3, 4]
  print('>>> Testing recursive fibonacci...')
  for test_case in test_cases:
    print('fib({}) = {}'.format(test_case, fib(test_case)))
  print()

def test_half_life():
  test_cases = [(100, 2), (1, 4), (50, 75)]
  print('>>> Testing half-life...')
  for a, t in test_cases:
    print('a:{}, t:{}\t{}, {}'.format(
      a, t, half_life_while(a, t), half_life_while(a, t)))
  print()
################################## main #######################################
if __name__ == "__main__":
  test_half_life()
  test_factorial()
  test_fib()
