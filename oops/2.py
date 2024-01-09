class Car:
    wheels = 4
    def __init__(s):
        s.mil =10
        s.com = "BMW"
    @staticmethod
    def p():    
        print("piyush")
cl=Car ()
c2= Car ()
cl.mil = 8
Car.wheels = 56
c2.wheels =7
Car.p()
# cl.p()
print (cl.com, cl.mil, cl.wheels)
print (c2.com, c2.mil, c2.wheels)
# djdjdjdjdj