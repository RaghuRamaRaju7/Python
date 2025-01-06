def addition(a1,b1):
    return a1+b1
def subtraction(a1,b1):
    return a1-b1
def multiplication(a1,b1):
    return a1*b1
def division(a1,b1):
    if b1!=0:
        return a1/b1
    else:
        return "Zero By Division Error"
def modulo(a1,b1):
    return a1%b1

print("Choose a operation")
print("1:Addition")
print("2:Subtraction")
print("3:Multiplication")
print("4:Division")
print("5:Modulo")

choice=int(input("Enter your choice:"))

a=int(input("Enter a value:"))
b=int(input("Enter b value:"))

if choice==1:
    ans=addition(a,b)
    operation="addition"

elif choice == 2:
    ans = subtraction(a, b)
    operation = "Subtraction"
elif choice == 3:
    ans = multiplication(a, b)
    operation = "Multiplication"
elif choice == 4:
    ans = division(a, b)
    operation = "Division"
elif choice ==5:
    ans=modulo(a,b)
    operation="Modulo"
else:
    ans = "Invalid choice"
    operation = "None"

if operation != "None":
    print(f"The result of {operation} is: {ans}")
else:
    print(ans)