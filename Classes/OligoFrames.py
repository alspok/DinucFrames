from copy import deepcopy
from Classes.InitValues import InitValues as iv

class OligoFrames():
    def __init__(self, seq: str) -> None:
        self.calc_seq = seq + seq[:6] # seq elongation by 6bp to calc up to 6 nuc frames
        self.seq_length = len(seq)
        pass
    
    def diFrame(self) -> list:
        dinuc_dict = deepcopy(iv.dinuc_dict)
        dinuc_frq_diff = []
        di_length = self.seq_length // 2
        
        for i in range(self.seq_length):
            di = self.calc_seq[i:i+2]
            if di in dinuc_dict:
                if i % 2 == 0:
                    dinuc_dict[di][0] += 1
                else:
                    dinuc_dict[di][1] += 1
            else: continue
            
        for di in dinuc_dict:
            dinuc_frq_diff.append(abs(dinuc_dict[di][0] - dinuc_dict[di][1]) / di_length)
        
        # iv.db_dict['di_diff'] = ', '.join(f"{diff:.6f}" for diff in dinuc_frq_diff)
        
        return dinuc_frq_diff
    
    def diFrameFrq(self) -> dict:
        dinuc_dict = deepcopy(iv.dinuc_dict)
        sol = self.seq_length // 2 # sol - seq oligo length. seq length in dinucleotides
        
        for i in range(len(self.calc_seq) + 1):
            di = self.calc_seq[i:i+2]
            if di in dinuc_dict:
                if i % 2 == 0 and di in dinuc_dict:
                    dinuc_dict[di][0] += 1
                    dinuc_dict[di][2] += dinuc_dict[di][0] / sol
                else:
                    dinuc_dict[di][1] += 1
                    dinuc_dict[di][3] += dinuc_dict[di][1] / sol
            else:
                continue
            
        dinuc_diff = 0
        for key in dinuc_dict:
            dinuc_dict[key][2] = abs(dinuc_dict[key][0] - dinuc_dict[key][1])
            dinuc_dict[key][5] = abs(dinuc_dict[key][3] - dinuc_dict[key][4])
            dinuc_diff += dinuc_dict[key][5]
            
        return dinuc_dict, dinuc_diff