class Rational:
    def __init__(self,num,deno):
        
        if deno==0 : #Value check for denominator to not be 0
            raise ValueError("Denominator cannot be Zero!!")
        self.num=num
        self.deno=deno
        
      
    @staticmethod #Static method either can be empty or can hold any other argument other than self
    def GCD (n,d): #static or void function for greatest common divisor

        while d != 0: # looped until "d" is 0
            n , d = d , n % d # Assigns the value of "d" to "n" and in "d" it extracts the remainder of "n" and "d"
        return (n) # returns "n"
    

    @staticmethod
    def LCM (n,d):# Static method for Lcm 

        return (n*d) // Rational.GCD(n,d) # Multiplies n and d and takes integer division by GCD function calling.


    def __add__(self,other): # Add dunder function for method overloading for "+" operation
        
        # Takes sum of products of (num. of self and deno. of other) and (deno. of other and num. of other)
        # and stores it in new_num
        new_num=self.num * other.deno + self.deno * other.num
        new_deno=self.deno * other.deno # Multiplies deno. of self and other and stores in new_deno

        cancel = Rational.GCD(new_num,new_deno) # Here stores GCD in cancel variable
        reduced_num=new_num // cancel # Takes integer division of "new num" and "cancel" to reduce it to lowest and stores it in reduced num
        reduced_deno=new_deno // cancel # Same done for the denominator 
        return  Rational(reduced_num,reduced_deno)  
    

    def __sub__(self,other): #Subtract dunder method for "-"

        #Same mechanics for __sub__ like __add__
        new_num=self.num * other.deno - self.deno * other.num
        new_deno=self.deno * other.deno

        cancel = Rational.GCD(new_num,new_deno)
        reduced_num=new_num // cancel
        reduced_deno=new_deno // cancel
        
        return  Rational(reduced_num,reduced_deno)


    def __str__(self): #String represnetation
        
        return f"The new rational number after the operation: {self.num}/{self.deno}"






