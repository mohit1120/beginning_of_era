
class singlethreaded:
    def printnumber():
        for i in range(1,51):
            print("i :",i,end="\t")
        return    
    def main():
        singlethreaded.printnumber()
        for j in range(1,51):
            print("j :"+str(j),end="\t")
        return
if __name__=="__main__":
    singlethreaded.main()
