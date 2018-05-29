class Rectangle(object):
    def __init__(self, x, y, w, h):
            self.x = x 
            self.y = y
            self.w = w #width of rectangle
            self.h = h #height of rectangle
    def area(self):
        return self.width * self.height
    def __str__(self):
        return('Rectangle(' + str(self.x) + ',' + str(self.y) + ','
                                    + str(self.w) + ',' + str(self.h)+')')
    def right(self):
        return self.x + self.w

    def bottom(self):
        return self.y + self.h

    def size(self):
        return self.w,self.h

    def position(self):
        return self.x,self.y

    def area(self):
        return self.w * self.h

    def expand(self, offset):
        return('Rectangle(' + str(self.x-offset) + ',' + str(self.y-offset) + ','
                            + str(self.w+2*offset) + ',' + str(self.h+2*offset)+')')
    
    def contains_point(self, x, y):
        return(x >= self.x and x <= self.x + self.w and y >= self.y and y <= self.y + self.h)

r2 = Rectangle(5, 10, 50, 100)
    
print(r2)


r3 = Rectangle(3,5,10,20)
r3.right()
print(r3.right())

r4 = Rectangle(12,10,72,35)
r4.right()
print(r4.right())


r5 = Rectangle(5, 7, 10, 6)
r5.bottom()
print(r5.bottom())

r5.y+=12
r5.bottom()
print(r5.bottom())

r6 = Rectangle(1,2,3,4)
r6.size()
print(r6.size())

r6.position()
print(r6.position())

r6.area()
print(r6.area())

r = Rectangle(30,40,100,110)
print(r)

r1 = r.expand(offset = 3)
print (r1)
print (r)

print (r.expand(-5))

r = Rectangle(30, 40, 100, 110)

print(r.contains_point(50,50))
print(r.contains_point(30,40))
print(r.contains_point(130, 150))
print(r.contains_point(131, 50))
print(r.contains_point(0,0))









