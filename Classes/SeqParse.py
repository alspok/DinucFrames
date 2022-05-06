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
                            "jahley", "smom", "nw",
                            "jaal", "jabw", "aace",
                            "wbvu", "jabmlo", "jahhpk",
                            "rrcj", "ltoo", "jaiwoz",
                            "jakvpt"
                        ]
        for seq_file in seq_files:
            with open(f".\\temp\\{seq_file}", 'r') as seqfh:
                for seq_record in SeqIO.parse(seqfh, "fasta"):
                    desc = seq_record.description.lower()
                    id = seq_record.id.lower()
                    if (any(item in desc for item in exept_description_list) or
                        any(item in id for item in exept_id_list)):
                        continue
                    else:
                        yield seq_record