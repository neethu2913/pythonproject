class pycharm:
    def create_file(self):
        print("pycharm created file")
    def executed_file(self):
        print("pycharm execued file")

class vscode:
    def create_file(self):
        print("vscode created file")
    def executed_file(self):
        print("vscode executed file")

class programmer:
    def coding(self,ide):
        ide.create_file()
        ide.executed_file()
py=vscode()
p=programmer()
p.coding(py)
