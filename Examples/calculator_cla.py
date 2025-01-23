import sys

def add(num1, num2):
    a = num1 + num2
    return a

def sub(num1, num2):
    s = num1 - num2
    return s

def mul(num1, num2):
    m = num1 * num2
    return m

def div(num1, num2):
    d = num1 / num2
    return d

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
   output = add(num1, num2)
   print("Addition:", output)

elif operation == "sub":
   output = sub(num1, num2)
   print("Subtraction:", output)

elif operation == "mul":
   output = mul(num1, num2)
   print("Multiplication:", output)

elif operation == "div":
   output = div(num1, num2)
   print("Division:", output)

else:
   print("a mismatch in the operation name")