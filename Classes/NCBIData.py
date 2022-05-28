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
    
    """Download taxon assembly accession numbers to summary.dat as json lines file from nsbi"""        
    def ncbiGenomeData(self, taxon_name: str) -> int:
        print(f"Downloading {taxon_name} assembly accessions...")
        os.chdir(iv.ROOT_DIR)
        subprocess.run(f".\\bin\\datasets summary genome taxon {taxon_name} \
                        --reference \
                        --assembly-level complete_genome,chromosome \
                        > .\\temp\\summary.json", shell=True)
        
        """Make list of assembly accession numbers"""
        assmbl_list = []
        with open(f".\\temp\\summary.json", "r", encoding="utf8") as jsonfh, \
             open(f".\\dbresults\\{taxon_name}_assembly_nr.acc", "w") as accfh:
            # data_list = [line.rstrip("\n") for line in datafh.readlines()]
            json_data = json.load(jsonfh)
            for item in json_data["assemblies"]:
                assmbl_list.append(f"{item['assembly']['assembly_accession']}\t{item['assembly']['org']['sci_name']}\n")
            accfh.writelines(assmbl_list)
        
        return len(assmbl_list)
    
    """Download sequencies of particular accession numbers"""
    def ncbiSeqData(self, assembly_access: str) -> list:
        os.chdir(iv.ROOT_DIR)
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
            os.chdir(iv.ROOT_DIR)
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
        accembly_nr = accembly_nr.rstrip("\n")
        with open(f".\\dbresults\\{taxon_name}_assembly_done.acc", "a") as daccfh:
            daccfh.write(f"{accembly_nr}\n")
        
        pass
    
    """Find *_assembly_done.acc file and read last line"""
    def assemblyBreak(self, taxon_name: str) -> str:
        os.chdir(f"{iv.ROOT_DIR}\\DBResults")
        file_list = os.listdir()
        acc_file = f"{taxon_name}_assembly_done.acc"
        if acc_file in file_list:
            with open(acc_file, "r") as accfh:
                last_line = accfh.readlines()[-1]
                return last_line.split("\t")[0]
        else:
            return "no_acc_file"
        
        
        