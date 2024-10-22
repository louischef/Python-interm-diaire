from module.calculator import calculate

def main():
    a = 10
    b = 10
    
    operators = ['+', '-', '*', '/', '=']
    for operator in operators:
        print(calculate(a,b,operator))
        
        
if __name__ == '__main__':
    main()