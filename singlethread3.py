import threading
import time
class printnumber:
    def printnumber1to50():
        for i in range(1,50):
            print("i :"+str(i),end="\t")
            time.sleep(.01)              #to delay
    def printnumber50to1():
        for j in range(50,0,-1):
            print("j :"+str(j),end="\t")
            time.sleep(.01)              #to delay
class Timecheck:
    def main():
       start=time.time()              #starting time
       printnumber.printnumber1to50()
       printnumber.printnumber50to1()
       end=time.time()                #ending time
       print("Time taken:",end-start)
      
if __name__=="__main__":
    Timecheck.main()
