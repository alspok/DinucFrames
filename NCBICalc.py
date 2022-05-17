from Classes.DelFiles import DelFiles
from Classes.GCCount import GCCount
from Classes.InitValues import InitValues as iv
from Classes.NCBIData import NCBIData
from Classes.DownloadDatasets import DownloadDatasets
from Classes.OligoFrames import OligoFrames
import sys
import os
import statistics as stat
from Classes.OligoFrames import OligoFrames
from Classes.OligoRandom import OligoRandom

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
      i = j = 1
      for accession in accfh:
         print(f"\nTaxon {taxon_name}: assembly {i} of {assembly_list_len}")
         seq_files = NCBIData().ncbiSeqData(accession.rstrip("\n"))
         seq_oblect = SeqParse().seqParse(seq_files) 
         for seq_obj in seq_oblect:
            seq_dict = {}
            print(f"{j}  {seq_obj.description}\n{repr(seq_obj.seq)}\t{len(seq_obj.seq)} bp")
            seq_dict["name"] = seq_obj.id
            seq_dict["description"] = seq_obj.description
            seq_dict["seq_length"] = len(seq_obj.seq)
            seq_dict["gc_percent"] = GCCount().gcCount(seq_obj.seq)
            
            seq = str(seq_obj.seq.lower())
            
            """Count seq dinuc frq differencies mean and standart deviation"""
            dinuc_frq_diff = OligoFrames(seq).diFrame()
            mean = seq_dict["di_diff_mean"] = round(stat.mean(dinuc_frq_diff), 6)
            stdev = seq_dict["di_diff_stdev"] = round(stat.stdev(dinuc_frq_diff), 6)
            print(f"             Dinuc diff\tmean {mean}\tstdev {stdev}")
            
            """Coun seq dinuc frq differecies mean and standart deviation of shuffled seq"""
            """Mononuc shuffle seq"""
            shuffle_seq = OligoRandom().seqListShuffle(seq, 1)
            dinuc_frq_diff = OligoFrames(shuffle_seq).diFrame()
            mean = seq_dict["mono_shuffle_di_diff_mean"] = round(stat.mean(dinuc_frq_diff), 6)
            stdev = seq_dict["mono_shuffle_di_diff_stdev"] = round(stat.stdev(dinuc_frq_diff), 6)
            print(f"Mono shuffle Dinuc diff\tmean {mean}\tstdev {stdev}")
            
            """Dinuc shuffle seq"""
            shuffle_seq = OligoRandom().seqListShuffle(seq, 2)
            dinuc_frq_diff = OligoFrames(shuffle_seq).diFrame()
            mean = seq_dict["di_shuffle_di_diff_mean"] = round(stat.mean(dinuc_frq_diff), 6)
            stdev = seq_dict["di_shuffle_di_diff_stdev"] = round(stat.stdev(dinuc_frq_diff), 6)
            print(f"  Di shuffle Dinuc diff\tmean {mean}\tstdev {stdev}")
            
            """Trinuc shuffle seq"""
            shuffle_seq = OligoRandom().seqListShuffle(seq, 3)
            dinuc_frq_diff = OligoFrames(shuffle_seq).diFrame()
            mean = seq_dict["tri_shuffle_di_diff_mean"] = round(stat.mean(dinuc_frq_diff), 6)
            stdev = seq_dict["tri_shuffle_di_diff_stdev"] = round(stat.stdev(dinuc_frq_diff), 6)
            print(f" Tri shuffle Dinuc diff\tmean {mean}\tstdev {stdev}")
            print()
            
            sqliteDB = SqliteDB(iv.db_name, iv.db_table).initTable()
            sqliteDB.insertRow(seq_dict)
            j += 1
            NCBIData().assemblyDone(taxon_name, accession, seq_obj.description)
            
         DelFiles().delFiles()
         i += 1
      
   pass 

if(__name__ == "__main__"):
    ncbiCalc()