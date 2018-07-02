class samsungGuru:
    def call(self):
        print("Calling Guru:")
        return
    def camera(self):
        print("Guru-2mp:")
        return
class samsungGalaxy(samsungGuru):    #accessing existing functionality(call)
     def videocall(self):
         print("Videocall-Galaxy:")
         return
     def camera(self):               #override-update
         print("Galaxy-8mp:")
         return
mobile=samsungGalaxy()
mobile.call()
mobile.videocall()
mobile.camera()
