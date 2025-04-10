import colorManager as MKUtils

_SCRIPT_NAME : str = "component generator"
_SCRIPT_COLOR : str = "BRIGHT_MAGENTA"
final = ""

def execute(file = None):
    global final
    title = MKUtils.MKinput("enter a title : ", _SCRIPT_NAME, _SCRIPT_COLOR)
    final += '# <img src="" width="30"> ' + title
    final += "\n"
    final += "## How to use "
    final += "\n"
    final += "\n"
    final += "## Attributes"
    final += "\n"
    f = open("./"+title+".md", "w")
    attribute = getAllAttributeAndMethods(file)
    addAttribute(attribute[0])
    final += "\n"
    final += "## Methods"
    addMethods(attribute[1])
    final += "\n"
    final += "## Additional notes"
    f.write(final)
    f.close()

def getAllAttributeAndMethods(file):
    temp = []
    temp2 = []
    print(file)
    for item in file:
        if item.startswith('@export var'):
            temp.append(item)
        if item.startswith('func'):
            temp2.append(item)
    return [temp,temp2]


def addAttribute(attributeList):
    global final
    for i in attributeList:
        name = "unknow"
        typeVar = "None"
        a = i.split(" ")
        for j in range(len(a)):
            if a[j] == "var":
                name = a[j+1]
            if a[j] == ":":
                typeVar = a[j+1]
        print(name, type)
        final += "\n"
        final += f"- ### {name} : {typeVar}"

def addMethods(methodsList):
    global final
    isParameter = False
    for i in methodsList:
        name = "unknow"
        typeVar = "None"
        param = []
        a = i.split(" ")
        for j in range(len(a)):
            if a[j] == "func":
                name = a[j+1]
            if a[j] == "->":
                if a[j+1][0] != ":":
                    typeVar = a[j+1]
                else:
                    typeVar = a[j+1][:-1]
            if a[j] == "(":
                isParameter = True
            if a[j] == ")":
                isParameter = False
            if isParameter:
                if a[j+1] == ":":
                    param.append([a[j],a[j+2]])
                else:
                    param.append([a[j],"Variant"])
                    
        print(name, type)
        final += "\n"
        final += f"- ### {name} : {typeVar}"
        final += "    - #### parameter"
        final += "\n"
        for i in param:
            final += "\n"
            final += f"        - ##### {i[0]} : i[1]"
            