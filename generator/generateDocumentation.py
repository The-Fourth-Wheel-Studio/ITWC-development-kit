import os
import colorManager as MKUtils
import dialogueManager as dm
import importlib


ok : bool = False


while not ok:
    fileLocation = MKUtils.MKinput("enter script path : ", "Documentation Generator", "YELLOW")
    file = None
    try:
        file = open(fileLocation, "r")
    except:
        MKUtils.MKprint("this file doesn't exist >:(", "Documentation Generator", "YELLOW")
    if file != None:
        ok = True


presetArray = os.listdir("preset")

if len(presetArray) > 0:
    MKUtils.MKprint("select a preset : ", "Documentation Generator", "YELLOW")
    presetList = dm.List(presetArray, "CYAN", 3)
    ok = False
    while not ok:
        try:
            ans = presetList.execute()
            module = importlib.import_module("preset."+ans[:-3]) #thanks momoDeckstop
            module.execute(file)
            ok = True
        except:
            MKUtils.MKprint("no preset name this way, did you forget '.py' ?", "Documentation Generator", "YELLOW")
else:
    MKUtils.MKprint("no preset available", "Documentation Generator", "YELLOW")
