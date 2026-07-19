# li = [1,4,5,8,9,'aruna']
# print(type(li))
# print(li[2])
# print(li[-1])
# print(li[0:4:2])

'''

append
extend 
count 
insert
pop
remove
index

'''
li = [1,4,5,8,9,'aruna']
#li.append("python")
li.extend([10,2,8,"anjali",True])
print(li)
print(li.count(8))
li.remove(9)#element
print(li)
li.pop(2)#index
print(li)
print(li.index('aruna'))
li.insert(0,"xyz")
print(li)


for i in [1,4,5,8,9,'aruna']:
    print(i)