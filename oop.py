class Student():
    
    def __init__(self,reg=0,name=0):
        self.reg=reg
        self.name=name
        self.marks=[0,0,0]
    
    def setMarks(self,maths,phy,chem):
        
        self.marks[0]=maths
        self.marks[1]=phy
        self.marks[2]=chem
        
    def calAvg(self):
        
        return sum(self.marks)/3.0
    
    def printDetails(self):
        
        print('name:',self.name)
        print('reg no:',self.reg)
        print('marks:',self.marks)
        print('avg:',self.calAvg())
        
    def writeDetails(self,fileName):
        
        file=open(fileName,'a')
        
        avg=self.calAvg()
        
        file.write(str([self.name,self.reg,self.marks,avg])+'\n')
        file.close()

std1=Student(1,'John')
std1.setMarks(88,91,92)
std1.printDetails()
std1.writeDetails('student.txt')