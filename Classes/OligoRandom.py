from copy import deepcopy
from email import utils
from Classes.InitValues import InitValues as iv
import random

"""Generate or shuffle string"""
class OligoRandom():
    def __init__(self) -> None:
        pass
    
    """Make random seq of particular length"""
    def oligoRandom(self, seq_length: int) -> str:
        rand_seq = ''
        while len(rand_seq) < seq_length:
            rand = random.uniform(0, 1)
            if rand <= iv.nuc_frq_dict['a']:
                rand_seq += 'a'
                continue
            elif rand <= iv.nuc_frq_dict['c']:
                rand_seq += 'c'
                continue
            elif rand <= iv.nuc_frq_dict['g']:
                rand_seq += 'g'
                continue
            elif rand <= iv.nuc_frq_dict['t']:
                rand_seq += 't'
                continue
            else:
                print("Something wrong making random seq.")
                break
        return rand_seq
    
    """Make random seq of particular length with some oligo frequencies"""
    def foligoRundom(self, oligo_frq_dict: dict, seq_length: int) -> str:
        rand_seq = ''
        while len(rand_seq) <= seq_length:
            rand = random.uniform(0, 1)
            for key, value in oligo_frq_dict.items():
                if rand <= value[-1]:
                    rand_seq += key
                    break
        return rand_seq
                
    """Count nucleotides in seq"""
    def monoCount(self, seq: str) -> dict:
        nuc = deepcopy(iv.nuc_count_dict)
        temp = 0
        for key in nuc:
            nuc[key][0] = seq.count(key)
            nuc[key][1] = nuc[key][0] / len(seq)
            nuc[key][2] = nuc[key][1] + temp
            temp = nuc[key][2]
        return nuc
    
    """Convert seq to list of particular oligo length"""
    def seqToList(self, seq: str, oligo: int) -> list:
        seq_list = []
        for i in range(0, len(seq) - oligo, oligo):
            seq_list.append(seq[i:i+oligo])
        return seq_list
    
    """Shuffle seq by oligo length substring"""
    def seqListShuffle(self, seq: str, oligo: int) -> str:
        seq_list = self.seqToList(seq, oligo)
        random.shuffle(seq_list)
        return ''.join(seq_list)
   