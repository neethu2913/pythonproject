class student:
    def set_student(self,roll,name,total):
        self.roll=roll
        self.name=name
        self.total=total
    def print_student(self):
        print(self.roll)
        print(self.name)
        print(self.total)

obj=student()
obj.set_student(11,"raj",222)
obj.print_student()
