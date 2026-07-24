'''

Single Inheritance
Multilevel Inheritance
Multiple Inheritance
Heirarchical Inheritance

'''
#Single Inheritance

# class Parent():
#     def output(self):
#         print("Iam the Parent")

# class Child(Parent):
#     def outputc(self):
#         print("Iam the child")
# c=Child()
# c.outputc()#Child method
# c.output()#Parent method

#Multilevel Inheritance

# class GrandFather():
#     def outputgf(self):
#         print("Iam the GrandFather")

# class Parent(GrandFather):
#     def output(self):
#         print("Iam the Parent")

# class Child(Parent):
#     def outputc(self):
#         print("Iam the child")
# c=Child()
# c.outputc()#Child method
# c.output()#Parent method
# c.outputgf()#GrandFather method

#Multiple Inheriatnce
# class Father():
#     def outputf(self):
#         print("Iam the Father")

# class Mother():
#     def outputm(self):
#         print("Iam the Mother")

# class Child(Father,Mother):
#     def outputc(self):
#         print("Iam the child")
# c=Child()
# c.outputc()#Child method
# c.outputf()#Father method
# c.outputm()#Mother method



#Heirarchical Inheritance

class Father():
    def outputf(self):
        print("Iam the Father")

class Child1(Father):
    def outputc1(self):
        print("Iam the Child1")

class Child2(Father):
    def outputc2(self):
        print("Iam the child2")
c1=Child1()
c2=Child2()
c1.outputc1()
c1.outputf()
c2.outputc2()
c2.outputf()