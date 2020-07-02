from tkinter import *
import math 
class calc: 
  
    def getandreplace(self): 
        self.expression = self.e.get() 
        self.newtext=self.expression.replace('/','/') 
        self.newtext=self.newtext.replace('x','*') 
