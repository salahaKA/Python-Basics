# class Math:
#     def __init__(self, n):
#         self.num= n
#         print(f"I am object {self.num}")

#-------------------------------
# class Math:
#     def __init__(self, a, b):
#         self.a= a
#         self.b= b
#     def addition(self):
#         return self.a+self.b

#----------------------
# #Directy passing value to the functn
# class Math:
#     def __init__(self):
#         pass
#     def addition(self, a, b):
#         return a+b
# #------------------------------------- 
# class Math:
#     def __init__(self):
#         pass
#     def addition(a, b):
#         return a+b
# #-------------------------
# class Math:
#     def __init__(self, a, b):
#         self.a= a
#         self.b= b
#         self.addition()
#         self.subtraction()
#         self.multiplication()
#     def addition(self):
#         print(self.a+self.b)
#     def subtraction(self):
#         print(self.a-self.b)
#     def multiplication(self):
#         print(self.a*self.b)
# # #-------------------------
# class Math:
#     def __init__(self, n):
#         self.n=n 
#         self.list=[]
#         self.oddorev()
#         self.factorial()
#         self.tables()
#         print(self.list)

#     def oddorev(self):
#         if self.n%2==0:
#             self.list.append("even")
            
#         else:
#             self.list.append("odd")

#     def factorial(self):
#         fact=1
#         for i in range(1,self.n+1):
#             fact=fact*i
#         self.list.append(f"Factorial is:{fact}")

#     def tables(self):
#         t_list=[]
#         for i in range(0,11):
#             t_list.append(self.n*i)
#         self.list.append(t_list)

# #-----------------------------------------------------
    
# class Math1:
#     def __init__(self):
#         pass

#     def addition(a,b):
#         print(a+b)

# class Math2(Math1):
#     def __init__(self):
#         super.__init__()

#     def subtract(a,b):
#         print(a-b)

#--------------------------------

from turtle import Turtle
class Spiro(Turtle):
    def __init__(self):
        super.__init__()

    def spirograph(self):
        t= Turtle()
        t.speed(0)
        for i in range(180):
            t.circle(100)
            t.left(2)







        
