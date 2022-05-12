from Classes.DelFiles import DelFiles
from Classes.GCCount import GCCount
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
         
   """Get list of assembly access list of taxon from ncbi and seve to file"""
   assembly_list_len = NCBIData().ncbiGenomeData(taxon_name)
   # [print(f"{i+1}\t {assmbl}") for (i, assmbl) in enumerate(assmbl_list)]
   
   """Read assembly numbers from file and calculate dinuc frequencies"""
   with open(f".\\DBResults\\{taxon_name}_assembly_nr.acc", "r") as accfh:
      i = 1
      for accession in accfh:
         print(f"\nTaxon {taxon_name}: assembly {i} of {assembly_list_len}")
         seq_files = NCBIData().ncbiSeqData(accession.rstrip("\n"))
         seq_oblect = SeqParse().seqParse(seq_files) 
         for seq_obj in seq_oblect:
            seq_dict = {}
            print(f"{seq_obj.description}\t{repr(seq_obj.seq)}\t{len(seq_obj.seq)} bp")
            seq_dict["name"] = seq_obj.id
            seq_dict["description"] = seq_obj.description
            seq_dict["seq_length"] = len(seq_obj.seq)
            seq_dict["gc_percent"] = GCCount().gcCount(seq_obj.seq)
            
            sqliteDB = SqliteDB(iv.db_name, iv.db_table).initTable()
            sqliteDB.insertRow(seq_dict)
            
         DelFiles().delFiles()
         i += 1
         
   pass 

if(__name__ == "__main__"):
    ncbiCalc()