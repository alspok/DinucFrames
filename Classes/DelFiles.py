import os
class DelFiles():
    def __init__(self) -> None:
        pass
    
    def delFiles(self) -> None:
        if os.path.exists("Temp"):
            cwd = os.getcwd()
            path = f"{cwd}\\temp"
            os.chdir(path)
            for file in os.listdir(path):
<<<<<<< HEAD
                os.remove(file)
=======
                    os.remove(file)
        
>>>>>>> 56325930bd488dd8a888bec1e8cf20de2ac9abb5
        pass