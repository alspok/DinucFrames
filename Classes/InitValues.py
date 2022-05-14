import os

"""Class of init values"""
class InitValues():
    taxon_name = "Methanomassiliicoccaceae"
    #taxon_name = "Viridiplantae"
    # taxon_name = "Chlorophyta"
    # taxon_name = "Homo"
    # taxon_name = "Escherichia coli"
    # taxon_name = "Escherichia"
    # taxon_name = "Bacillus"
    # taxon_name = "Archaea"
    # taxon_name = "Bacteria"
    # taxon_name = "Eukaryotae"
    # taxon_name = "Viruses"
    # taxon_name = "Fungi"
    taxon_name = "Dikarya"
    
    # path = "C:\\Users\\hp\\source\\repos\\DinucFrames"
    path = os.getcwd()
    
    # seq_path = "C:\\Users\\hp\\source\\repos\\Sequencies\\Procaryote\\Plasmids\\"
    seq_path = os.getcwd()
    db_name = f".\\dbresults\\{taxon_name}_dinuc.sqlite3"
    db_table = "dinuc"
    oligo_length = 2
    db_dict = {}
    
    nuc_frq_dict = {'a': 0.2, 'c': 0.5, 'g': 0.8, 't': 1}
    
    # list of nucleotides
    nuc_list = ['a', 'c', 'g', 't']
    
    # list of possible dinucleotides
    dinuc_list = []
    for n1 in nuc_list:
        for n2 in nuc_list:
            dinuc_list.append(n1 + n2)
    
    # dictionary of dinucleotides as key. counts as values
    dinuc_dict = {key:[0, 0] for key in dinuc_list}
    
    # ductuibart of dinucleotides as key. count, frequencies, diff in diframes as values
    dinuc_frq_dict = {key:[0, 0, 0, 0] for key in dinuc_list}
    
    # list of possible trinucleotides 
    trinuc_list = []
    for n1 in nuc_list:
        for n2 in nuc_list:
            for n3 in nuc_list:
                trinuc_list.append(n1 + n2 + n3)
    
    # dictionary of trinucleotides as key. counts and counts differencies in triframe as value
    trinuc_dict = {key:[0, 0, 0] for key in trinuc_list}
    
    #list of possible tetranucleotides
    tetranuc_list = []
    for n1 in nuc_list:
        for n2 in nuc_list:
            for n3 in nuc_list:
                for n4 in nuc_list:
                    tetranuc_list.append(n1 + n2 + n3 +n4)

    #dictionary of tetranucleotides as key. counts and differencies in tetraframe as value
    tetranuc_dict = {key:[0, 0, 0, 0] for key in tetranuc_list}
    
    #list of possible pentanucleotides
    pentanuc_list = []
    for n1 in nuc_list:
        for n2 in nuc_list:
            for n3 in nuc_list:
                for n4 in nuc_list:
                    for n5 in nuc_list:
                        pentanuc_list.append(n1 + n2 + n3 + n4 + n5)

    #dictionary of pentanucleotides as key. counts and differencies in pentaframe as value
    pentanuc_dict = {key:[0, 0, 0, 0, 0] for key in pentanuc_list}
    
    #list of possible hexanuclaotides
    hexanuc_list = []
    for n1 in nuc_list:
        for n2 in nuc_list:
            for n3 in nuc_list:
                for n4 in nuc_list:
                    for n5 in nuc_list:
                        for n6 in nuc_list:
                            hexanuc_list.append(n1 + n2 + n3 + n4 + n5 + n6)

    #dictionary of hexanucleotides as key. counts and differencies in hexaframe as value
    hexanuc_dict = {key:[0, 0, 0, 0, 0, 0] for key in hexanuc_list}
    