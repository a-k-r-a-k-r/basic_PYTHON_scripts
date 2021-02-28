num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
num3=float(input("Enter the third number: "))
if num2 <= num1 >= num3:
    print("Greatest: ",num1)
elif num1 <= num2 >= num3:
    print("Greatest: ",num2)
elif num1 <= num3 >= num2:
    print("Greatest: ",num3)