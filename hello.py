# Adding two numbers
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=a+b
print(c)

# Swapping(Without Third Variable)
a=10
b=20
a,b=b,a
print(a)
print(b)

# Swapping using thid variable
a=10
b=20
c=a
a=b
b=c
print(a)
print(b)
print(c)

name="raghu"
print(type(name))

age=22
print(type(age))

a=10
b=20
if(a>b):
    print("A is Biggest")
else:
    print("B is Biggest")
    


def check_even_odd(number):
    if number%2==0:
        return "even"
    else:
        return "odd"
 
num = int(input("Enter a number:"))
result=check_even_odd(num)
print(f"{num} is {result}")


    