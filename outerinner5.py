class outerclass:     #outer class 
    def m1():
        class innerclass:    #inner class
            def fun():
                print("INNER CLASS")
        innerclass.fun()        
    def m2():
         print("OUTER CLASS")
    def main():
         outerclass.m1()
         outerclass.m2()
if __name__=="__main__":
    outerclass.main()
         
