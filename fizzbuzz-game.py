print('Please Hit Enter')
fizzBuzz = input()

for fizzBuzz in range(1, 101):
    if fizzBuzz % 3 == 0 and fizzBuzz % 5 == 0:
        print(str(fizzBuzz) + ' it\'s a FizzBuzz')
    elif fizzBuzz % 3 == 0:
        print(str(fizzBuzz) + ' it\'s a Fizz')
    elif fizzBuzz % 5 == 0:
        print(str(fizzBuzz) + ' it\'s a Buzz')
    else:
        print(str(fizzBuzz))