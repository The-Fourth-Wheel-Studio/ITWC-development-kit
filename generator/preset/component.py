import shutil

def execute(file):
    shutil.copyfile("preset.md", "./output.md")
    print(file)