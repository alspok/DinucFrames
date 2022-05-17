import subprocess
import json
import zipfile
import os
import pathlib
from Bio import SeqIO
from Classes.InitValues import InitValues as iv


class NCBIData():
    def __init__(self) -> None:
        pass
    
    def ncbiGenomeData(self, taxon_name: str) -> int:
        """Download taxon assembly accession numbers to summary.json file from nsbi"""        
        print(f"Downloading {taxon_name} assembly accessions...")
        os.chdir(iv.path)
        subprocess.run(f".\\bin\\datasets summary genome taxon {taxon_name} \
                        --as-json-lines \
                        --reference \
                        --assmaccs \
                        --assembly-level complete_genome,chromosome \
                        > .\\temp\\summary.dat", shell=True)
        
        """Make list of assembly accession numbers"""
        assmbl_list = []
        with open(f".\\temp\\summary.dat", "r") as datafh:
            data_list = [line.rstrip("\n") for line in datafh.readlines()]
            for item in data_list:
                item = json.loads(item)
                assmbl_list.append(item["assembly_accession"])
        
        """Save assembly accesion numbers to file"""
        with open(f".\\dbresults\\{taxon_name}_assembly_nr.acc", "w") as accfh:
            for item in assmbl_list:
                accfh.write(item + "\n")
            
            
        return len(assmbl_list)
        
    """Download sequencies of particular accession numbers"""
    def ncbiSeqData(self, assembly_access: str) -> list:
        os.chdir(iv.path)
        try:
            subprocess.run(f".\\bin\\datasets download genome accession {assembly_access} \
                            --exclude-rna \
                            --exclude-gff3 \
                            --exclude-protein \
                            --exclude-genomic-cds \
                            --filename .\\temp\\ncbi_dataset.zip", shell=True)
        except Exception as e:
            print
                       
        try:
            os.chdir(iv.path)
            seq_files = []
            with zipfile.ZipFile(".\\temp\\ncbi_dataset.zip") as ziph:
                for zip_info in ziph.infolist():
                    if pathlib.Path(zip_info.filename).suffix == ".fna":
                        zip_info.filename = os.path.basename(zip_info.filename)
                        ziph.extract(zip_info, ".\\temp")
                        seq_files.append(zip_info.filename)
                    else:
                        continue
        except Exception as e:
            print(e)
            pass
            
        return seq_files
    
    """Append file with calculated assembly numbers"""
    def assemblyDone(self, taxon_name: str, accembly_nr: str) -> None:
        with open(f".\\dbresults\\{taxon_name}_assembly_done.acc", "a") as daccfh:
            daccfh.write(f"{accembly_nr} calc done.")
        
        pass
        