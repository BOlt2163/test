def prime(num):
    if num == 0 or n == 1:
        return print("it is not a prime no.")
    else:
        for i in range(2,num//2):
            if num%i == 0:
                return print("it is not a prime no.")

            else:
                return print("It is a prime no.")

if __name__ == '__main__':
    n = int(input("Enter the no.:\n"))
    print(prime(n))