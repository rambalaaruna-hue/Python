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
# n=int(input("enter a number:"))
# s=n
# l=len(str(n))
# sum=0
# while n!=0:
#     r=n%10
#     sum=sum+(r**l)
#     n=n//10
#     print(n)
# if s==sum:
#     print("Armstrong")
# else:
#     print("Not Armstrong")

#Check if a number is even or odd
# num=int(input("Enter a number:"))
# if num%2==0:
#     print("{0} is even.".format(num))
# else:
#     print("{0} is Odd.".format(num))

#Python program to get a substring of a string
# str="this is python"
# print(str[8:14])

#Add two given lists using map and lambda
# l1=[1,2,3]
# l2=[3,4,5]
# print("Original lists")
# print(l1)
# print(l2)
# result=map(lambda x,y:x+y,l1,l2)
# print("Result")
# print(list(result))

#Python program to add two matrices using nested loop
# x=[[12,6,10],
#    [3,14,15],
#    [10,5,15]]
# y=[[4,18,20],
#    [5,30,20],
#    [21,16,3]]
# result=[[0,0,0],
#         [0,0,0],
#         [0,0,0]]
# print(len(x))
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j]=x[i][j]+y[i][j]
# for r in result:
#       print(r)

#python program to detect number of local variables declared in a function
# def aruna():
#   a=10
#   b=20
#   s="anjali"
#   #f=4.4
# print(aruna.__code__.co_nlocals)

#Python program to compute all the permutations of a string
# def get_permutations(string,i=0):#('run',0)
#     if i==len(string):# 0==3   1==3 2==3 3==3
#         print("".join(string))
#     for j in range(i,len(string)):#0,3
#         words=[c for c in string]#['r','u','n']
#         print(words[i],words[j])
#         words[i],words[j]=words[j],words[i]
#         get_permutations(words,i+1)
# get_permutations('run')

#write a numpy program to generate a random integer between 1 and 300
# import numpy as np
# x=np.random.randint(low=1,high=300,size=10)
# print(x)

#Program to print half pyramid using *
rows=5
# for i in range(rows):

    # for j in range(i+1):
    #     print("*",end=" ")
    # print()


#Transppse matrics
# x=[[12,6,10],
#    [3,14,15],
#    [10,5,15]]
# result=[[0,0,0],
#         [0,0,0],
#         [0,0,0]]

# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[j][i]=x[i][j]
# for r in result:
#       print(r)

#Find all numbers which are divisible by 7 but are not multiple of 5
# li=[]
# for i in range(1,1000):
#     if i%7==0 and i%5!=0:
#         li.append(i)
# print(li)


#Get current time
# import datetime
# print(datetime.datetime.now())
# import datetime
# print(datetime.datetime.now().time())

#Multiplication table
# num=int(input("Enter a number:"))
# for i in range(1,11):
#    print(num , "x" , i , "=" , num*i)

#Write a python program of recusrsion list sum
# def recursive(data_list):
#     total=0
#     for ele in data_list:
#         if type(ele)==type([]):
#             total=total+recursive(ele)
#         else:
#             total=total+ele
#     return total
# print(recursive([1,2,[3,4],[5,6],1,4]))


#Python program to access index of a list
#Start the index with non zero value
# li=[21,33,44,55,60]
# for index,val in enumerate(li,start=1):
#     print(index,val)


#Python program to check if a string is palidrome or not
# def isPalindrome(str):
#     return str==str[::-1]
# str="madam"
# ans=isPalindrome(str)
# if(ans):
#     print("Paindrome")
# else:
#     print("Not palindrome")


#Remove all white spaces from a text
# import re
# text=" This          is         python           Life"
# print("Original Text:",text)
# print("Without white spaces:",re.sub(r'\s+','',text))

#Accept hyphen seperated sequence of words as input and print sorted words
# items=[n for n in input("enter a string:").split("-")]
# print(items)
# items.sort()
# print("-".join(items))



#Split a string with multiple delimeters
# import re

# text = 'The quick brown\nfox jumps*over the lazy dog.'
# print(re.split(r'; |, |\*|\n', text))


#Python program to triple all numbers of list of integers using map
# num=(1,2,3,4,5,6,7,8)
# result=map(lambda x:x+x+x,num)
# print(list(result))


#Check if a number is prime or not
# def isPrime(num):
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 return "not a prime"
#         return "Prime"
#     return "Not a prime"
# print(isPrime(11))


#Check if the given year is leap year or not
def check(year):
    return (((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)))
year=2024
if check(year):
    print("Leap Year")
else:
    print("Not a Leap Year")