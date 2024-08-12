class student:
    name="ammu"
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @staticmethod
    def info():
        return "name"
print(student.info())
s=student(10,20)
print(s.a+s.b)
        
