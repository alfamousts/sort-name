import sys

class fileParser: #class for read file data and parse every lines in file into a list of string
    
    def __init__(self , filename):
        self.filename = filename
        self.listOfNames = []
    
    def getListOfNames(self):
        return self.listOfNames #return the variable list consisted in this class

    def parser(self):
        f = open(self.filename, "r") #read file
        strBuff = f.read() #saved into buffer string
        self.listOfNames = strBuff.split("\n") #parse the string into list

class listSorter:

    def __init__(self, inputedList):
        self.inputedList = inputedList
        self.lastNameList =[]
        self.sortedList =[]
    
    def sortList(self):
        #this loop is used to find the last names and then append every last name into lastNameList
        for name in self.inputedList:
            listBuff = name.split(" ")
            self.lastNameList.append(listBuff[len(listBuff)-1])
        
        #zip the lastNameList and inputedList become a tupple variable
        #sort the tupple by using lastNameList
        #then zip into a tupple
        #x and y is a temporary tupple variable that returned after sorting by tupple mechanism, x is equivalent to lastNameList that has been sorted and
        #y is equivalent to inputedList that has been sorted
        x , y = zip(*sorted(zip(self.lastNameList, self.inputedList)))
        self.sortedList = list(y) #convert the y (tupple) into a list variable

    def getSortedList(self): #return the sortedList variable
        self.sortList()
        return self.sortedList


class fileWriter: # a class for displaying the list and rewrite file based on the inputed list

    def __init__(self,inputedList,filename):
        self.inputedList = inputedList
        self.filename = filename
    
    def displayList(self):
        outputFile = open(self.filename,"w")
        i = 0
        totalName = len(self.inputedList)
        for name in self.inputedList:
            print(name)
            if(i < totalName-1):
                outputFile.write(name + "\n")
            else :
                outputFile.write(name)
            i += 1
        outputFile.close()

#sys.argv is a list that come from command line argument , the index 0 always refer to python file name that want to be executed. 
#e.g : python sortName.py ./unordered-name-list.txt , sys.argv[0] = sortName.py and sys.argv[1] = ./unordered-name-list.txt
inputFileName = sys.argv[1]
objectParse = fileParser(inputFileName)   
objectParse.parser()
listOfNames = objectParse.getListOfNames()

objectSorter = listSorter(listOfNames)
sortedListOfNames = objectSorter.getSortedList()

objectDisplay = fileWriter(sortedListOfNames,inputFileName)
objectDisplay.displayList()
