#python program to to solve the Fabinocci series using recursion

# def fib(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return(fib(n-1)+fib(n-2))
# print(fib(7))

#Find the largest among three input  numbers
# num1=float(input("Enter num1:"))
# num2=float(input("Enter num2:"))
# num3=float(input("Enter num3:"))
# if num1>=num2 and num1>=num3:
#     largest=num1
# elif num2>=num1 and num2>=num3:
#     largest=num2
# else:
#     largest=num3
# print(largest)

#Python program to check if a number is positive or negative or 0
# num=int(input("Enter a number:"))
# if num>0:
#     print("Number is positive")
# elif num<0:
#     print("Number is negative")
# else:
#     print("Number is 0")

#Check if a number is Armstrong or not without using power function
n=int(input("enter a number:"))
s=n
l=len(str(n))
sum=0
while n!=0:
    r=n%10
    sum=sum+(r**l)
    n=n//10
    print(n)
if s==sum:
    print("Armstrong")
else:
    print("Not Armstrong")
