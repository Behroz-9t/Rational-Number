from Rational_class import rational 

class app:
    
    def run(self):
        
        num1=rational(4,4)
        num2=rational(8,16)

        print(num1+num2)
        print(num1-num2)

        print(f"The Greatest Common Mivisor of {num1.num}/{num1.deno} is:",num1.GCD(4,4))
        print(f"The Least Common Multiple of {num2.num}/{num2.deno} is:",num2.LCM(8,16))

        num3=rational(4,0) #--> Raises Value Error for the denominator