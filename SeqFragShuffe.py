from ntpath import join
from Classes.OligoFrames import OligoFrames
from Classes.SeqInput import SeqInput
import statistics as stat
import random

def seqFragShuffle() -> None:
    seq_path = "C:\\Users\\hp\\source\\repos\\Sequencies\\Procaryote\\"
    seq_record = SeqInput().seqInputFile(f"{seq_path}pBR322.fasta")
    
    for record in seq_record:
        seq = str(record.seq.lower())
        # print(seq[:1276])
        # print(seq[1276:1904])
        # print(seq[1904:])
        
        di_frq = OligoFrames(seq).diFrame()
        seq_mean = stat.mean(di_frq)
        seq_stdev = stat.stdev(di_frq)
        print(f"Seq dinuc diff         mean {seq_mean:.6f} stdev {seq_stdev:.6f}\n")
        
        sseq = str(seq[1276:1904])
        for i in range(1000000):
            shuffle_seq_frag = ''.join(random.sample(sseq, len(sseq)))
            shuffle_seq = seq[:1276] + shuffle_seq_frag + seq[1904:]
            di_frq = OligoFrames(shuffle_seq).diFrame()
            if stat.mean(di_frq) < seq_mean:
                print(f"Shuffle seq dinuc diff mean {stat.mean(di_frq):.6f} stdev {stat.stdev(di_frq):.6f}")
                seq_mean = stat.mean(di_frq)
            
    pass

if __name__ == "__main__":
    seqFragShuffle()