def largest_number():

 a=int(input("enter first number:"))
 b=int(input("enter second number:"))

 if a>b :
    print("the largest number is",a)
 else:
    print("the largest number is",b)



# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# c=int(input("enter third number:"))

# if a>b and a>c:
#     print("largest number is",a)
    
# if b>a and b>c:
#     print("largest number is",b)
    
# if c>b and c>a:
#     print("largest number is",c)
    
    
    
    
# a=int(input("enter first number:"))  

# if a%2==0:
#     print("this is an even number")
# else:
#     print("this is an odd number")
    
    

 
    
    
# a=int(input("enter first number:"))  

# if a%10==0:
#     print("divisible by 10")
# else:
#     print("not divisible by 10")
    
    
# age=int(input("enter age:"))  

# if age<18:
#     print("the person is minor")
# else:
#     print("the person is major")



# a=(input("enter a number:"))
# print(len(a))



# year=int(input("enter a year:"))

# if (year%4==0 and year%100!=0) or (year%400==0):
#     print("year is leap year")
# else:
#     print("year is not leap year")




# a=int(input("enter first angle:"))  
# b=int(input("enter second angle:"))  
# c=int(input("enter third angle:")) 

# c=a+b+c

# if c==180:
#     print("this is a valid triangle")
# else:
#     print("this is a not valid triangle")




# a=int(input("enter first number:"))

# if a<0:
#   print(-a)
# else:
#   print(a)





# length=int(input("enter length:"))
# breadth=int(input("enter breadth:"))

# area=length*breadth
# perameter=2*(length+breadth)


# if area>perameter:
#   print("area is greater")
# else:  
#   print("perameter is greater")







# x1=int(input("enter first point:"))
# y1=int(input("enter second point:"))
# x2=int(input("enter third point:"))
# y2=int(input("enter fourth point:"))
# x3=int(input("enter fifth point:"))
# y3=int(input("enter sixth point:"))

# area_of_triangle=x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)

# if area_of_triangle==0:
#   print("all points are on same line")
# else:
#   print("all points are not on same line")





x1=int(input("enter first point:"))
y1=int(input("enter second point:"))

radius=sqrt(x1*x1+y1*y1)

print(radius)
