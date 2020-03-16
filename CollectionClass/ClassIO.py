

class IO:
    @staticmethod
    def funRead(choise):
        choise=choise
        arrayOb = []
        if choise==1:
            fileRead=open("File\\BallFile.txt","r")
            varstr=fileRead.readline()
            while varstr:
                arrayOb.append(varstr)
                varstr = fileRead.readline()
            fileRead.close()
            return arrayOb
        elif choise==2:
            fileRead=open("File\\BenchFile.txt","r")
            varstr=fileRead.readline()
            while varstr:
                arrayOb.append(varstr)
                varstr=fileRead.readline()
            fileRead.close()
            return arrayOb
        elif choise==3:
            fileRead=open("File\\MatesFile.txt","r")
            varstr=fileRead.readline()
            while varstr:
                arrayOb.append(varstr)
                varstr=fileRead.readline()
            fileRead.close()
            return arrayOb
        elif choise==4:
            fileRead=open("File\\SkidsFile.txt","r")
            varstr=fileRead.readline()
            while varstr:
                arrayOb.append(varstr)
                varstr=fileRead.readline()
            fileRead.close()
            return arrayOb
        del arrayOb

