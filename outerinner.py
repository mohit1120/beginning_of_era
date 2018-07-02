class outer:                 #outer class
    def m1():
        print("outer class m1")
        return
    class inner:             #inner class
        def m2():
            print("Inner class m2")
            return    
    def main():
        outer.m1()
        outer.inner.m2()
        return
if __name__=="__main__":
    outer.main()
