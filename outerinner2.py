class outer:                         #factorial in outer class
    def m1():
        class localinner():      
            def test():
                f=1
                for i in range(1,5):
                    f=f*i
                print("factorial of",i , f)    
        localinner.test()
        return
    def m2():
        class localinner():          # sum of 1 to 10 numbers in inner class.
            def test():
                s=0
                for i in range(1,11):
                    s+=i
                print("sum of 1 to 10 no.s",s)
            
                return
        localinner.test()
        return
    def main():
        outer.m1()
        outer.m2()
        return
if __name__=="__main__":
    outer.main()
    
