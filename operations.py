import os
os.system('cls')

input1 = int(input("Enter a Number :"))
input2 = int(input("Enter a Number :"))

operator = input ("Select a operator : \n1.plus \n2.minus\n3.multipy:").lower()

if operator == "plus" or operator == "1":
    print(input1+input2)

elif operator == "minus" or operator == "2":
    print(input1-input2)

elif operator == "multipy" or operator == "3":
    print(input1 * input2)

else:
    print("Invalid operator")