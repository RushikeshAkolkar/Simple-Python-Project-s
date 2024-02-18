class Teacher:
    id = None
    name = None
    address = None
    data = None

    def read1():
             
        f1=open("ABC1.txt","w")

        f2=open("ABC.txt","r")

        data = f2.read()

        return data
    
    def write(data):
        for lines in data:
            f1.writelines(line)
            print(line)

obj=Teacher()

data=obj.read1(self)

obj.write(data)
    