'''
Wrapping od variables and methods into a single unit is called Encapsulation
public
private__
protected_ 

'''
# class demo():
#     __a=2
#     _b=5
#     print(__a)
#     print(_b)


class demo():
    def __init__(self,a,b):
     self.__a=a#private
     self._b=b#protected
class demo2(demo):
   def output(self):
       print(self._b)
d=demo2(3,4)
d.output()