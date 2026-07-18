'''
String is a collection of characters

'''

a='pythonlife'
b="pythonlife"
c='''pythonlife'''
print(type(a),type(b),type(c))

'''

lower
upper
count
replace
startswith
endswith
split
strip
lstrip
rstrip
removeprefix
removesuffix
index
find

'''

# a="Python Life"
# print(a.upper())
# print(a.lower())


# a="python life"
# print(a.startswith("python"))
# print(a.endswith("e"))


# a="python language"
# print(a.replace("language","programming"))

# a="python language"
# print(a.index("thon"))#if the word not found it throws error
# print(a.find("something"))#if the word not found it returns -1


# a="python language"
# print(a.count('p'))
# print(a.count('a'))
# print(a.count('c'))


# a="python language"
# print(a.removeprefix("pyth"))
# print(a.removesuffix("language"))


# a="python programming language"
# print(a.split())#It converts it into list


a="       python language   "
print(a)
print(len(a))

s=a.strip()
print(len(s))

l=a.lstrip()
print(len(l))

r=a.rstrip()
print(len(r))



