import calculator

def multiplication(num1, num2):
    mul = num1 * num2
    return mul

def division(num1, num2):
    div = num1 / num2
    return div

print("Addition:", calculator.addition(5, 15))
print("Subtraction:", calculator.subtraction(20, 18))
print("Multiplication:", multiplication(25, 4))
print("Division:", division(45, 5))