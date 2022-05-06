import random
import statistics
from collections import defaultdict
from SeqInput import SeqInput
from InitValues import InitValues as iv
from OligoList import OligoList


class OligoFrame():
    def __init__(self) -> None:
        pass

    def oligoCalcM1(self, seq: str, oligo = iv.oligo_length) -> dict:
        if oligo == 1:
            count_list = iv.nuc_list
        elif oligo == 2:
            count_list = iv.dinuc_list
        elif oligo == 3:
            count_list = iv.trinuc_list
        elif oligo == 4:
            count_list = iv.tetranuc_list
        oligo_count_dict = defaultdict()
        
        oligo_list = OligoList().seqToList(seq, oligo)
        temp_frq = 0
        oligo_count = 0
        no_oligo = []
        for item in count_list:
            temp_list = [0, 0, 0]
            temp_list[0] = oligo_list.count(item)
            if temp_list[0] == 0:
                no_oligo.append(item)
                continue
            oligo_count += temp_list[0]
            temp_list[1] = temp_list[0] / (len(seq) // oligo)
            temp_list[2] = temp_list[1] + temp_frq
            temp_frq = temp_list[2]
            oligo_count_dict[item] = temp_list
        
        return oligo_count_dict
    
    def diCalc(self, seq: str, oligo_length = iv.oligo_length):
        seq = seq + seq[:1]
        oligo_count_dict = defaultdict(lambda: [0, 0, 0, 0, 0])
        for i in range(0, len(seq)):
            oligo = seq[i:i+oligo_length]
            if len(oligo) == oligo_length:
                if i % 2 == 0:
                    oligo_count_dict[oligo][0] += 1
                    oligo_count_dict[oligo][2] = oligo_count_dict[oligo][0] / (len(seq) // 2)
                else:
                    oligo_count_dict[oligo][1] += 1
                    oligo_count_dict[oligo][3] = oligo_count_dict[oligo][1] / (len(seq) // 2)
                    
        di_diff = []
        di_diff_sum = 0
        for key in oligo_count_dict:
            oligo_count_dict[key][4] = abs(oligo_count_dict[key][2] -  oligo_count_dict[key][3])
            di_diff.append(oligo_count_dict[key][4])
            di_diff_sum += oligo_count_dict[key][4]
                    
        return oligo_count_dict, di_diff, di_diff_sum
    
    
def main():
    seq_record = SeqInput().seqInputFile(f"{iv.seq_path}hepb.fasta")
    seq_record = SeqInput().seqInputFile(f"{iv.seq_path}pbr322_hepb.fasta")
    seq_record = SeqInput().seqInputFile(f"{iv.seq_path}e.coli_k12.fasta")
    seq_record = SeqInput().seqInputFile(f"{iv.seq_path}puc19.fasta")
    seq_record = SeqInput().seqInputFile(f"{iv.seq_path}pbr322.fasta")

    for record in seq_record:
        print(f"{record}")
        seq = str(record.seq.lower())
        print(f"Len: {len(seq)} bp")
        # oligo_count = OligoFrame().oligoCalcM1(seq)
        # for _ in range(10):
        #     rand_seq = OligoRandom().foligoRundom(oligo_count, 100)
        #     print(f"Rand seq: {rand_seq} len {len(rand_seq)}")
    
        di_dict, di_diff, di_diff_sum = OligoFrame().diCalc(seq)
        # for key, value in sorted(di_dict.items()):
        #     print(f"{key} {value}")
        print(f"  Dinuc diff mean: {statistics.mean(di_diff):.6f} stdev: {statistics.stdev(di_diff):.6f} didiffsum {di_diff_sum:.6f}")
        for _ in range(6):
            oligo = 2
            seq_list = OligoList().seqToList(seq, oligo)
            random.shuffle(seq_list)
            shuffle_seq = ''.join(seq_list)
            _, di_diff, di_diff_sum = OligoFrame().diCalc(shuffle_seq)
            print(f"Shuffle by {oligo} mean: {statistics.mean(di_diff):.6f} stdev: {statistics.stdev(di_diff):.6f} didiffsum {di_diff_sum:.6f}")    
    
    pass

if __name__ == "__main__":
    main()