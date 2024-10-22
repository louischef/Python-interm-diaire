from module.addition import addition
from module.division import division
from module.substract import substract
from module.multiplication import multiplication

def calculate(a: float,b: float, operation: str) -> float:
    if operation not in("+", "-", "*", "/"):
        print(f"erreur avec l'operateur {operation}")
        return None
    elif operation == '/':
        return division(a,b)
    elif operation == '+':
      return addition(a,b)
    elif operation == '-':
      return substract(a,b)
    elif operation == '*':
        return multiplication(a,b)
    return None