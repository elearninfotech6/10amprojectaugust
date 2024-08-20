class p1:
    def m1(self):
        print('parent1')

class p2:
    def m2(self):
        print('parent2')

class c(p1,p2):
    def m3(self):
        print('child')

class d(c):
    def m4(self):
        print('extra cls')

obj=c()
obj.m1()
obj.m2()
