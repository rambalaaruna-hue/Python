#calculating length of a string without using built-in function

# str="This is Python"
# def length(str):
#     count = 0;
#     for char in str:
#         count += 1
#     return count
# print(length(str))

#python function that accepts a string and countno of Upper case letters and lower case letters
# def String_test(s):
#     d = {"Upper_case":0,"Lower_case":0}
#     for i in s:
#         if i.isupper():
#             d["Upper_case"]+=1
#         elif i.islower():
#             d["Lower_case"]+=1
#         else:
#             pass


#     print("Upper case leteers:",d["Upper_case"])
#     print("Lower case letters:",d["Lower_case"])

# String_test("This Is Python Life")



#Check if the first and last number of a list is same or not
# numbers = [10,50,40,20,10]
# def fun(numbers):
#     first = numbers[0]
#     last = numbers[-1]
#     if first == last:
#         return True
#     else:
#         return False
# print(fun(numbers))


#Python program to check if a key is already in the dictionary or not
# dict={"name":"aruna","age":20,"branch":"CSE"}
# if "age" in dict:
#     print("Present")
# else:
#     print("Not there")


#Count the number of occurences of each word in a given sentence
# def count_word(str):
#     counts=dict()
#     words=str.split()
#     for word in words:
#         if word in counts:
#             counts[word]+=1
#         else:
#             counts[word]=1
#     return counts
# print(count_word("the quick brown fox jumps over the lazy dog."))


#create empty dictionaries in list
# d=10
# s=[{} for _  in range(d)]
# print(s)

#print([{} for _ in range(10)])

#Extend a list without append
l1=[1,2,3]
l2=[3,4,5]
l1[:0]=l2
print(l1)