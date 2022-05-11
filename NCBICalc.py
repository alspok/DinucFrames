from Classes.DelFiles import DelFiles
from Classes.InitValues import InitValues as iv
from Classes.NCBIData import NCBIData
from Classes.DownloadDatasets import DownloadDatasets
import sys
import os

from Classes.SeqParse import SeqParse
from Classes.SqliteDB import SqliteDB

def ncbiCalc():
   """Run script from command line with taxon name as argument or edit taxon_name in InitValues class """
   if len(sys.argv) == 1:
      taxon_name = iv.taxon_name
   else:
      taxon_name = sys.argv[1]
      
   """Creat or not temp folder"""
   if not os.path.exists("Temp"):
      os.mkdir("Temp")
   
   """Make .\\temp folder empty"""
   DelFiles().delFiles()
   
   """Download letest version of datasets.exe file"""   
   # DownloadDatasets().downloadDatasets()
         
   """Get list of assembly access list of taxon from ncbi"""
   assembly_list_len = NCBIData().ncbiGenomeData(taxon_name)
   # [print(f"{i+1}\t {assmbl}") for (i, assmbl) in enumerate(assmbl_list)]
   
   with open(f".\\dbresults\\{taxon_name}_access_number.acc", "r") as accfh:
      accession_list = [line.rstrip("\n") for line in accfh.readlines()]
      i = 1
      for accession in accession_list:
         if "#" not in accession:
            print(f"\nTaxon {taxon_name}: assembly {i} of {assembly_list_len}")
            seq_files = NCBIData().ncbiSeqData(accession)
            seq_oblect = SeqParse().seqParse(seq_files) 
            for seq_obj in seq_oblect:
               seq_dict = {}
               print(f"{seq_obj.description}\t{repr(seq_obj.seq)}\t{len(seq_obj.seq)} bp")
               seq_dict["name"] = seq_obj.id
               seq_dict["description"] = seq_obj.description
               seq_dict["seq_length"] = len(seq_obj.seq)
               
               sqliteDB = SqliteDB(iv.db_name, iv.db_table).initTable()
               sqliteDB.insertRow(seq_dict)
         
         DelFiles().delFiles()
         i += 1
      
   pass 

if(__name__ == "__main__"):
    ncbiCalc()