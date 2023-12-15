from mybasiccalculator import basicCalc
def add(num1,num2):
    return num1+num2
def subract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
operations={
    "+":add,
    "-":subract,
    "*":multiply,
    "/":divide
}
num1=int(input("enter the first number:"))
for symbol in operations:
    print(symbol)
num2=int(input("enter the second number:"))
operation_symbol=input("enter the symbol:")
c__function=operations[operation_symbol]
answer1=c__function(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {answer1}")
num3=int(input("enter the third number:"))
operation_symbol=input("enter the symbol:")
c__function=operations[operation_symbol]
answer2=c__function(answer1,num1)
print(f"{answer1} {operation_symbol} {num3} = {answer2}")
