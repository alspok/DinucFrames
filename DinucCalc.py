from copy import deepcopy
import statistics as stat
import random
from Classes.InitValues import InitValues as iv
from Classes.OligoFrames import OligoFrames
from Classes.SeqInput import SeqInput
from Classes.OligoList import OligoList
from Classes.OligoRandom import OligoRandom
from Classes.SqliteDB import SqliteDB

def dinucCalc():
    # seq = "aaacagatcacccgctgagcgggttatctgtt"
    # seq = "aaacagatcacccgctgagcgggttatctgttnaaacagatcacccgctgagcgggttatctgtt"
    # seq = "agagacagggtagtcacagtgactagagcagagatgatggtttcaacgaag"
    # seq = "agagacagggtagtcacagtgactagagcagagatgatggtttcaacgaagagagacagggtagtcacagtgactagagcagagatgatggtttcaacgaag"
    # seq_path = "C:\\Users\\hp\\source\\repos\\Sequencies\\Procaryote\\"
    
    # seq_record = SeqInput().seqInputGB("NC_000913.3, SYNPBR322, J01749")
    # seq_record = SeqInput().seqInputFile(f"{iv.seq_path}pBR322_HepB.fasta,{iv.seq_path}HepB_geneX.fasta")
    # seq_record = SeqInput().seqInputFile(f"{iv.seq_path}pBR322_HepB.fasta")
    # seq_record = SeqInput().seqInputFile(f"{iv.seq_path}HepB_geneC.fasta")
    # seq_record = SeqInput().seqInputFile(f"{iv.seq_path}pBR322.fasta")
    # seq_record = SeqInput().seqInputFile(f"{iv.seq_path}pUC19.fasta")
    seq_record = SeqInput().seqInputFile(f"{iv.seq_path}HepB.fasta")
    seq_record = SeqInput().seqInputFile(f"{iv.seq_path}E.coli_K12.fasta")
    # seq_record = SeqInput().seqInputFile(f"{iv.seq_path}Test.fasta")
    
    for record in seq_record:
        iv.db_dict = {}
        iv.db_dict['name'] = record.name
        iv.db_dict['description'] = record.description
        iv.db_dict['seq'] = record.seq
        
        print(f"{record}")
        seq = str(record.seq.lower())
        iv.db_dict['gc_percent'] = round((seq.count('g') + seq.count('c')) * 100 / len(seq), 2)
        
        di_frq = OligoFrames(seq).diFrame()
        di_diff = f"{stat.mean(di_frq):.6f}, {stat.stdev(di_frq):.6f}"
        diff_split = di_diff.split(',')
        print(f"             Seq dinuc diff\tmean {diff_split[0]} stdev {diff_split[1]}")
        iv.db_dict['di_diff'] = di_diff
        
        sholigo = {'mono': 1, 'di': 2, 'tri': 3}
        for key, value in sholigo.items():
            oligo_list = OligoList().seqToList(seq, value)
            random.shuffle(oligo_list)
            shuffle_seq = ''.join(oligo_list)
            shuffle_di_frq = OligoFrames(shuffle_seq).diFrame()
            shuffle_diff = f"{stat.mean(shuffle_di_frq):.6f}, {stat.mean(shuffle_di_frq):.6f}"
            shuffle_diff_split = shuffle_diff.split(',')
            print(f"Shuffle {key} seq dinuc diff\tmean {shuffle_diff_split[0]} stdev {shuffle_diff_split[1]}")
            iv.db_dict[f'{key}_shuffle_di_diff'] = shuffle_diff
        
        SqliteDB(iv.db_name, iv.db_table).initTable().insertRow()
        print()
        
    pass

if __name__ == "__main__":
    dinucCalc()