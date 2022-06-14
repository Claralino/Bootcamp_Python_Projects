is_prime = True


def prime_number(number):
    for i in range(2, number):
        if number % 2 == 0:
           is_prime = False
    if is_prime:
        print("it is a prime number")
    else:
        print("not a prime number")



number = int(input("type a number: "))
prime_number(number)