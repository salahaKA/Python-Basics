# # 06/11/2023

# name= "Salaha"
# mark= 95
# print(f"My name is: {name} and mark is: {mark}")  #formatting string
# print("My name is:"+name+"\t"+" Mark is:"+str(mark))
# #---------------------------------------------
#MULTIPLICATION TABLE
# #Type-1
# num= int(input("Enter a number:"))
# for i in range(0,11):
#     print(num*i)

# #type-2
# num= int(input("Enter a number:"))
# for i in range(num,num*10+1,num):  #stepsize by 8
#     print(i)
# # --------------------------------------------------
# # FACTORIAL
# #Type-1
# num=int(input("Enter a number:"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(f"Factorial is:{fact}")

#-----------------------------
#Sum of digit in 100th and 1000 place, input from user (eg: i/p->56732 o/p=> 6+7=13)
# #Type-1
# num=int(input("Enter a number:"))
# n=str(num)
# l= len(n)
# sum= int(n[l-3])+int(n[l-4])
# print(sum)

# #Type-2
# n=int(input("Enter a number:"))
# sum=(n//100)%10 + (n//1000)%10
# print(sum)
#---------------------------------------------------------
# #AMSTRONG NUMBER
# #program to print amstrong number b/w 1 to 500 (there are 5 amstrong number b/w 1-500)
# #Eg: 153
#
# #TYPE-1
# for i in range(1,501):
#     temp=i
#     sum=0
#     while temp>0:
#         sum=sum+(temp%10)**3
#         temp= temp//10
#     if sum==i:
#         print(f"amstrong no:{sum}")   #o/p=> 1, 153, 370, 371, 407
#         #OR
#         #print(f"amstrong no:{i}")  # sum~i

# #TYPE-2
# for i in range(1,501):
#     temp=str(i)
#     sum=0
#     for digit in temp:
#         sum+=int(digit)**3
#     if sum==i:
#         print(i)
#--------------------------------
# # Q. i/p-> 514 and o/p=>282 ie; (5*(5^1))+(1*(1^2))+(4*(4^3))= 282
# num=int(input("Enter a number:"))
# n= str(num)
# sum=0
# i=1
# for digit in n:
#     sum+= int(digit)**i * int(digit)
#     i+=1
# print(sum)

#------------------------------------------

#  # # # # 07/11/2023
# import random
# list=["a", "b", "c"]
# a= random.randint(0,2)
# print(list[a])


# #-----------------------------------------------
# import random
# import string
#
# alphabets = list(string.ascii_letters)  #52 letters
# #print(alphabets)
#
# number=[0,1,2,3,4,5,6,7,8,9]
# symbol=["@","#","_","$","*","-","%","(",")","~"]
#
# a= random.randint(6,10)
# n= random.randint(2,4)
# s= random.randint(2,4)
#
# password_list= []
#
# for i in range(1, a+1):
#     x= random.randint(0,51)
#     password_list.append(alphabets[x])
# for i in range(1, n + 1):
#     y= random.randint(0,9)
#     password_list.append(number[y])
# for i in range(1, s + 1):
#     z = random.randint(0, 9)
#     password_list.append(symbol[z])
# random.shuffle(password_list)
# print(password_list)
#
# final_password= ""
# for i in password_list:
#     final_password+= str(i)
# print(final_password)
#
# #-----------------------------------------
# import random
# score= 0
# ans= 0
# c_ans=0
# for i in range(1,6):
#     q_list=["added to","subtracted to","multiplied to","floor_devided to"]
#     c= random.randint(0,3)  #operator
#     a = random.randint(1, 10) #operand1
#     b = random.randint(1, 10) #operand2
#
#     if c==0:
#         c_ans= a+b
#     elif c==1:
#         c_ans= a-b
#     elif c==2:
#         c_ans= a*b
#     elif c==3:
#         c_ans= a//b
#
#     ans= int(input(f"Q{i}.What is {a}{q_list[c] }{b}? \n"))
#
#     if ans==c_ans:
#         score+=1
#         print(f"Correct answer acore:{score}")
#     else:
#         print(f"Wrong answer acore:{score}")
# print(f"Your test is over and final score is:{score}")

# #----------------------------------
# d= {"apple":"fruit","lion":"animal","parrot":"bird"}
# for key in d:
#     print(f"{key}:{d[key]}")
#
# #-------------------------------

# s= input("Enter a string:") #name
# d= {}
# for i in s:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# for key in d:
#     print(f"{key}:{d[key]}")

# #----------------------------------
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f= f*i
#     return f
# s=input()  #onion o/p= 30
# num= fact(len(s))
# d={}
# for i in s:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# den=1
# for key in d:
#     den*=fact(d[key])
# print(num//den)   # whwre num means numerator and den means denomenator
#---------------------------

