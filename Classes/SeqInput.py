from posixpath import split
from Bio import SeqIO
from Bio import Entrez

class SeqInput():
    def __init__(self) -> None:
        pass
    
    def seqInputGB(self, ids: str) -> object:
        id_list = ids.split(',')
        for id in id_list:
            Entrez.email = "alspok@gmail.com"
            with Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id=id) as handle:
                seq_record = SeqIO.read(handle, "fasta")
            yield seq_record
            
    def seqInputFile(self, files: str) -> list:
        file_list = files.split(',')
        for file in file_list:
            for seq_record in SeqIO.parse(file, "fasta"):
                yield seq_record