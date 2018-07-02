class outer:                  #outer class
    def m1(self):
        print("outer class m1")
        return
    class inner:              #inner class
        def m2(self):
            print("inner class m2")
            return
    def main():
        Outer=outer()
        Outer.m1()
        Inner=outer.inner()
        Inner.m2()
        return
if __name__=="__main__":
    
    outer.main()
