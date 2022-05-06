import random

"""Class to shuffle seq by oligo length nuclaotides.
"""
class OligoList():
    def __init__(self) -> None:
        pass
    
    """Split seq string to oligo length nucleotides list
       adding appropriate nucs to circle seq.
       Return shuffled and joined seq string.
    """
    def seqToListRand(self, seq: str, oligo_len: int) -> str:
        oligoList = []
        for i in range(0, len(seq), oligo_len):
            oligos = seq[i:i+oligo_len]
            if len(oligos) == oligo_len:
                oligoList.append(oligos)
            else:
                oligoList.append(oligos + seq[:oligo_len - len(oligos)])
        
        random.shuffle(oligoList)
        
        return ''.join(oligoList)
    
    """Split seq string to oligo length nucleotides list
       adding appropriate nucs to circle seq.
       Return splited seq list.
    """
    def seqToList(self, seq: str, oligo_len: int) -> list:
        oligoList = []
        for i in range(0, len(seq), oligo_len):
            oligos = seq[i:i+oligo_len]
            if len(oligos) == oligo_len:
                oligoList.append(oligos)
            else:
                oligoList.append(oligos + seq[:oligo_len - len(oligos)])
        
        return oligoList