from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast.Applications import NcbimakeblastdbCommandline


path_subjects = ""
path_query = ""



cline_make = NcbimakeblastdbCommandline(dbtype="prot",
                                        input_file="NC_005816.faa")

cline_blast = NcbiblastpCommandline(query="rosemary.pro", db="nr",
                                    evalue=0.001, remote=True, ungapped=True)



                    
class Blastp:
    def __init__(self,path_qy, path_sbj, path_db):
        self.query = path_qy
        self.subject = path_sbj
        self.db = path_db

    def makeblastDB(path_db, type):
        cline_make
        return
        