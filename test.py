from mybasiccalculator import *

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))

for symbol in operations:
    print(symbol)

operation_symbol=input("enter the symbol:")

c__function=operations[operation_symbol]

answer1=c__function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer1}")

num3=int(input("enter the third number:"))
operation_symbol=input("enter the symbol:")
c__function=operations[operation_symbol]
answer2=c__function(answer1,num1)

print(f"{answer1} {operation_symbol} {num3} = {answer2}")