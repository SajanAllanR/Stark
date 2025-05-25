'''
op=input('What do you want to do? \n 1.Add\t2.Substract\t3.Multiply\t4.Divide\t5.Exit')
if op=='Add':
    add1 = input("Provide first number: ");
    add2 = input("Provide second number: ");
    print(float(add1) + float(add2));
if op=='Substract':
    sub1 = input("Provide first number: ");
    sub2 = input("Provide second number: ");
    print(float(sub1) - float(sub2));
if op=='Multiply':
    mult1 = input("Provide first number: ");
    mult2 = input("Provide second number: ");
    print(float(mult1) * float(mult2));
if op=='Divide':
    div1 = input("Provide first number: ");
    div2 = input("Provide second number: ");
    print(float(div1) // float(div2));
'''
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

print("Addition: ", a+b)
print("Substraction: ", a-b)
print("Multiplication: ", a*b)
print("Division: ", a/b)
