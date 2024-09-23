from abc import ABC, abstractmethod
class Phuongtien:
    def __init__(self, xangtrongxe, muctieuthu):
        self.xangtrongxe = xangtrongxe
        self.muctieuthu = muctieuthu
    @abstractmethod
    def drive (self,distance):
        pass
    @abstractmethod
    def refuel (self,fuel):
        pass

class car(Phuongtien):
    def drive (self, distance):
        xangcan = (self.muctieuthu + 0.9) * distance
        if xangcan <= self.xangtrongxe:
            self.xangtrongxe -= xangcan
        else:
            print("hết xăng rồi")
    def refuel (self,fuel):
        self.xangtrongxe += fuel

class truct(Phuongtien):
    def drive (self, distance):
        xangcan = (self.muctieuthu + 0.9) * distance
        if xangcan <= self.xangtrongxe:
            self.xangtrongxe -= xangcan
        else:
            print("hết xăng rồi")
    def refuel (self,fuel):
        self.xangtrongxe += fuel

Vinfast = car (20, 5)
Vinfast.drive(3)
print(Vinfast.xangtrongxe)
Vinfast.refuel(10)
print(Vinfast.xangtrongxe)




