class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if a>=0 and b>=0:
            for i in range(b):
                result = self.add(result, a)
        elif a>=0 and b<0 :
            for i in range(a):
                result = self.add(result, b)
        elif a<0 and b<0:
            for i in range(abs(a)):
                result = self.add(result, abs(b))
       
        return result
    
    def divide(self, a, b):
        result = 0
        while a >= b and a>0 and b>0:
            a = self.subtract(a, b)
            result +=1
        while a >= b and a>0 and b<0:
            a = self.add(a, b)
            result -=1
        while a < b and a>0 and b>0:
            a = self.add(a, b)
            result
        while a < b and a<0 and b>0:
            a = self.add(a, b)
            result -=1
        while a>=b and a<0 and b<0:
            b =self.subtract(b,a)
            result +=1
        while a <= b and a<0 and b<0:
            a = self.subtract(a, b)
            result +=1
        while a <= b and a<0 and b>0:
            a = self.add(a, b)
            result +=1
            if result+b >0:
                result +=1
        return result
    
    def modulo(self, a, b):
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(-4, 6))
    print("Example: multiplication: ", calc.multiply(-6, -4))
    print("Example: division: ", calc.divide(1, -10))
    print("Example: modulo: ", calc.modulo(9, 10))