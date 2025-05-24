def factorial(n):
    n = int(n)
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

a=input("Enter a number: ")
f=factorial(a)
print("Factorial of a is" ,int(f))
