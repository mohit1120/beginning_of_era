class first:
    def __init__(self,a,b):
        self.a=a
        self.__b=b
        return
class second:
    def display():
        print("Displaying variables:")
        obj=first(10,20)
        print("first class public-a",obj.a)
        print("first class private-b",obj.b)         # We can't access object level private variable from another class.
        return
second.display()    
