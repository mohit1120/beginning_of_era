class test:                 #accessing class level private variable with in the class.
    def __init__(self,a):
        self.__a=a
        return
    def access(self):
        print("private a:",self.__a)
        return
obj=test(10)
obj.access()
    
