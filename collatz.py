def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

n = input("Give me a number:\n ")
while n != 1:
    n = collatz(int(n))

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)

        elif number % 2 == 1:
            number = number * 3 + 1
            print(number)

try:
    num = int(input("Enter a positive integer to output its collatz number:\n"))
    collatz(num)
except ValueError:
    print('Please use whole numbers only.')

def collatznumber(number):
    while number !=1:
        if number%2==0:
            number=number//2
            print(number)
        else:
            number=number*3+1
            print(number)
num=int(input("Enter a positive number Please:\n"))
collatznumber(num)





