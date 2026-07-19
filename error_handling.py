# a=10
# print(b)

# try:
#     print(b)
# except:
#     print("Error")
# else:
#     print("No Error")
# finally:
#     print("Always")


try:
    print('a'+123)
except TypeError:
    print("type error")
except ValueError:
    print("value error")