import shutil
import colorManager as MKUtils

_SCRIPT_NAME : str = "component generator"
_SCRIPT_COLOR : str = "BRIGHT_MAGENTA"

def execute(file = None):
    shutil.copyfile("preset/preset.md", "./output.md")
    fileLocation = MKUtils.MKinput("enter component title : ", _SCRIPT_NAME, _SCRIPT_COLOR)
