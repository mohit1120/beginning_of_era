import threading
import time

class printnumber:
    def print1to50():            #printing a number 1 to 50
        for i in range(1,51):
            print(i,end=" ")
            time.sleep(0.1)
        return
    def print50to1():            #printing a number 50 to 1
        for i in range(50,0,-1):
            print(i,end=" ")
        return
class child1(threading.Thread):
    def run(self):
        printnumber.print1to50()
        return
class child2(threading.Thread):
    def run(self):
        printnumber.print50to1()
        return
class timecheck:
    def main():
        thread1=child1()             #thread creation
        thread2=child2()
        s=time.time()                #starting time 
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        e=time.time()                #ending time
        print("Time taken=",round(e-s))
        return
if __name__=="__main__":
    timecheck.main()
