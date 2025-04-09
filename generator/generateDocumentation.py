import os
import colorManager as MKUtils
import dialogueManager as dm
import importlib

_SCRIPT_NAME : str = "Documentation Generator"
_SCRIPT_COLOR : str = "YELLOW"
ok : bool = False


while not ok:
    fileLocation = MKUtils.MKinput("enter script path : ", _SCRIPT_NAME, _SCRIPT_COLOR)
    file = None
    try:
        file = open(fileLocation, "r")
    except:
        MKUtils.MKprint("this file doesn't exist >:(", _SCRIPT_NAME, _SCRIPT_COLOR)
    if file != None:
        ok = True


presetArray = os.listdir("preset")

if len(presetArray) > 0:
    MKUtils.MKprint("select a preset : ", _SCRIPT_NAME, _SCRIPT_COLOR)
    temp = []
    for i in presetArray:
        if i.endswith('.py'):
            temp.append(i)
    presetArray = temp
    presetList = dm.List(presetArray, "CYAN", 3)
    
    ok = False
    while not ok:
        try:
            ans = presetList.execute()
            module = importlib.import_module("preset."+ans[:-3]) #thanks momoDeckstop
            ok = True
        except:
            MKUtils.MKprint("no preset name this way, did you forget '.py' ?", _SCRIPT_NAME, _SCRIPT_COLOR)
        try:
            module.execute(file)
        except:
            MKUtils.MKprint("the preset is broken, did tender wrote this one ?", _SCRIPT_NAME, _SCRIPT_COLOR)
else:
    MKUtils.MKprint("no preset available", "Documentation Generator", "YELLOW")
