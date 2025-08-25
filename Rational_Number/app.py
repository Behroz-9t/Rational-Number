from Rational_class import Rational 

class app:
    
    def run(self):
        
        num1=Rational(4,4)
        num2=Rational(8,16)

        print(num1+num2)
        print(num1-num2)

        print(f"The Greatest Common Divisor of {num1.num}/{num1.deno} is:",num1.GCD(4,4))
        print(f"The Least Common Multiple of {num2.num}/{num2.deno} is:",num2.LCM(8,16))

        num3=Rational(4,0) #--> Raises Value Error for the denominator