#calculating length of a string without using built-in function

str="This is Python"
def length(str):
    count = 0;
    for char in str:
        count += 1
    return count
print(length(str))

#python function that accepts a string and countno of Upper case letters and lower case letters
def String_test(s):
    d = {"Upper_case":0,"Lower_case":0}
    for i in s:
        if i.isupper():
            d["Upper_case"]+=1
        elif i.islower():
            d["Lower_case"]+=1
        else:
            pass


    print("Upper case leteers:",d["Upper_case"])
    print("Lower case letters:",d["Lower_case"])
    
String_test("This Is Python Life")
