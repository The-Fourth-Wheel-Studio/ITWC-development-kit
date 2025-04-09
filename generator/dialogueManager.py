import colorManager as MKUtils

class Line():
    def execute(self) -> None:
        """
        execute when line is display
        """
        if self.nextSpeech != None:
            self.nextSpeech.execute()
    
class Input(Line):
    
    def __init__(self, nextSpeech = None) -> None:
        self.nextSpeech = nextSpeech
        
    def execute(self):
        result : str = self.dprint()
        Line.execute(self)
        return result
        
    def dprint(self) -> None:
        """
        print the line
        """
        return(input())

class List(Line):
    
    def __init__(self, action : list, color : str = "DEFAULT", nbrOfWordPerRaw = 1):
        self.action = action
        self.color = color
        self.nbrOfWordPerRaw = nbrOfWordPerRaw

    def execute(self):
        self.dprint()
        return Input(None).execute()
        
    def dprint(self):
        self.printList(self.nbrOfWordPerRaw)
    
    def printList(self,objectPerRaw : int) -> None:
        for i in range(int(len((self.action)) / objectPerRaw + 1)):
            self.printRaw(self.action[i * objectPerRaw:((i+1) * objectPerRaw)])
            
    def printRaw(self, listToPrint : list):
        result = "	"
        for i in listToPrint:
            self.pprint(i, self.color)
            MKUtils.printColoredWithoutNewLine("	", "DEFAULT")
        print("\n")
    
    def setNextSpeech(self,n):
        self.nextSpeech = n
    
    def pprint(self,name, color):
        MKUtils.printColoredWithoutNewLine(str(name), color)