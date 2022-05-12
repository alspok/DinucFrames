from Classes.InitValues import InitValues as iv

class GCCount():
    def __init__(self) -> None:
        pass
    
    def gcCount(self, seq: str) -> float:
        gCount = seq.lower().count("g")
        cCount = seq.lower().count("c")
        
        return round(((gCount + cCount) / len(seq) ) * 100, 2)