from tkinter import *
import math 
class calc: 
  
    def getandreplace(self): 
        self.expression = self.e.get() 
        self.newtext=self.expression.replace('/','/') 
        self.newtext=self.newtext.replace('x','*') 
    def squareroot(self): 
        self.getandreplace() 
        try: 
        
            self.value= eval(self.newtext)  
        except SyntaxError or NameError: 
            self.e.delete(0,END) 
            self.e.insert(0,'Invalid Input!') 
        else: 
            self.sqrtval=math.sqrt(self.value) 
            self.e.delete(0,END) 
            self.e.insert(0,self.sqrtval) 
  
    def square(self): 
        self.getandreplace() 
        try: 
            self.value= eval(self.newtext)  
        except SyntaxError or NameError: 
            self.e.delete(0,END) 
            self.e.insert(0,'Invalid Input!') 
        else: 
            self.sqval=math.pow(self.value,2) 
            self.e.delete(0,END) 
            self.e.insert(0,self.sqval) 

    def equals(self): 
        self.getandreplace() 
        try: 
            self.value= eval(self.newtext)  
        except SyntaxError or NameError: 
            self.e.delete(0,END) 
            self.e.insert(0,'Invalid Input!') 
        else: 
            self.e.delete(0,END) 
            self.e.insert(0,self.value) 
     def clearall(self): 
            self.e.delete(0,END) 
  
    def clear1(self): 
            self.txt=self.e.get()[:-1] 
            self.e.delete(0,END) 
            self.e.insert(0,self.txt) 
  
    def action(self,argi): 
            self.e.insert(END,argi) 
  
 