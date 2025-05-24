#Celsuis <----> Fahrenheit converter

a=input("What value do you have. C or F?")
if a=="C":
    c=input("Enter Celsuis Value: ")
    d = float(c) * 9 / 5 + 32
    print("Fahrenheit Value: ", d)
else:
    e = input("Enter Fahrenheit value: ")
    f = float(e)  * (5/9) - 32
    print("Celsius Value: ", f)