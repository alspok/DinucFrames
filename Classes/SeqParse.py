import os
from Bio import SeqIO

class SeqParse():
    def __init__(self) -> None:
        pass
    
    def seqParse(self, seq_files: list) -> None:
        exept_description_list = [
                            "plasmid", "unknow", "mitochond",
                            "scaffold", "contig", "unlocal",
                            "unacchore", "unplace", "unplace",
                            "chloroplast", "partial"
                        ]
        exept_id_list = [
                            "aace",
                            "jahley", "jaal", "jabw",
                            "jabmlo", "jahhpk", "jaiwoz",
                            "jakvpt", "jafkak", "jaifh",
                            "jaiwqd", "jaifhz", "jahne",
                            "jagks",
                            "ltoo",
                            "nw",
                            "pesf"
                            "rrcj", "rcwq",
                            "smom", "sthe", "sthd",
                            "sthb", "sthf", "stha" #last
                            "vahf",
                            "wnkj", "wnkj", "wbvu",
                        ]
        exept_seq_length = 50000

        for seq_file in seq_files:
            with open(f".\\temp\\{seq_file}", 'r') as seqfh:
                for seq_record in SeqIO.parse(seqfh, "fasta"):
                    desc = seq_record.description.lower()
                    id = seq_record.id.lower()
                    if (any(item in desc for item in exept_description_list) or
                        any(item in id for item in exept_id_list) or
                        len(seq_record.seq) < exept_seq_length):
                        continue
                    else:
                        yield seq_record