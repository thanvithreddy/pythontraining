class Engineer:
    def __init__(self):
        pass
    def work(self):
        print("Engineer is working")
class SoftwareEngineer(Engineer):
    def __init__(self):
        super().__init__()
    def work(self):
        print("Software Engineer is coding")
    e1=Engineer()
        
        