class swift:
    def start(self):
        print("swift starts")
    def accerlarate(self):
        print("swift accelarate method")
    def stop(self):
        print("swift stop")

class seltos:
    def start(self):
        print("seltos starts")
    def accerlarate(self):
        print("seltos accelarate method")
    def stop(self):
        print("seltos stop")

class person:
    def drive(self,car):
        car.start()
        car.accerlarate()
        car.stop()
sw=seltos()
p=person()
p.drive(sw)