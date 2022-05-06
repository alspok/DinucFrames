import os
class DelFiles():
    def __init__(self) -> None:
        pass
    
    def delFiles(self) -> None:
        cwd = os.getcwd()
        path = f"{cwd}\\temp"
        os.chdir(path)
        for file in os.listdir(path):
                os.remove(file)
        
        pass