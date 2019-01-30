# from itertools import count,accumulate,takewhile
#
# # numbers = [11,12,13,14]
#
# num = list(accumulate(range(10)))
# print(list(takewhile(lambda x:x<22,num)))
#
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         x  = self.x + other.x
#         y = self.y + other.y
#         return Point(x,y)
#
#     def __str__(self):
#         return "([01,{2})".format(self.x,self.y)
#
# point1 = Point(5,10)
# point2 = Point(10,15)
# print(point1+point2)

class matrix:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z

        return matrix(x,y,z)

    def __str__(self):
        return "({0},{1},{2})".format(self.x,self.y,self.z)

per = matrix(5,5,3)
per1 = matrix(6,6,2)
print(per * per1)

