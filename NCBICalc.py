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
      
   """Change for folder to working"""   
   # os.chdir(os.path.dirname(os.path.abspath(__file__)))
   
   """Make .\\temp folder empty"""
   DelFiles().delFiles()
   
   """Download letest version of datasets.exe file"""   
   # DownloadDatasets().downloadDatasets()
         
   """Get list of assembly access list of taxon from ncbi"""
   assmbl_list = NCBIData().ncbiGenomeData(taxon_name)
   # [print(f"{i+1}\t {assmbl}") for (i, assmbl) in enumerate(assmbl_list)]
   
   i = 1
   for accession in assmbl_list:
      print(f"\nTaxon {taxon_name}: assembly {i} of {len(assmbl_list)}")
      seq_files = NCBIData().ncbiSeqData(accession)
      seq_oblect = SeqParse().seqParse(seq_files) 
      for seq_obj in seq_oblect:
         seq_dict = {}
         print(f"{seq_obj.description}\t{repr(seq_obj.seq)}")
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