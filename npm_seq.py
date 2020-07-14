#!/usr/bin/env python

mut_dict = {'NPM1_Mut_A': ['TCTCTGTCTGGCAGTG', 0], # Start Grupp 1
            'NPM1_Mut_B': ['TCTCTGCATGGCAGTG', 0],
            'NPM1_Mut_D': ['TCTCTGCCTGGCAGTG', 0],
            'NPM1_Mut_H': ['TCTCTGAGGAGCAGTG', 0],
            'NPM1_Mut_I': ['TCTCTGCTTGGCAGTG', 0],
            'NPM1_Mut_L': ['TCTCTGTTTGGCAGTG', 0],
            'NPM1_Mut_K': ['TCTCTGCCAGGCAGTG', 0],
            'NPM1_Mut_N': ['TCTCTGTCGGGCAGTG', 0],
            'NPM1_Mut_R': ['TCTCTGTATGGCAGTG', 0],
            'NPM1_Mut_X': ['TCTCTGTTCCGCAGTG', 0],
            'NPM1_Mut_Y': ['TCTCTGCCGAGCAGTG', 0],
            'NPM1_Mut_Z': ['TCTCTGTAGGGCAGTG', 0],
            'NPM1_Mut_Ivey-1': ['tctctgCAGGgcagtg', 0],
            'NPM1_Mut_Ivey-2': ['tctctgCGTGgcagtg', 0],
            'NPM1_Mut_Ivey-3': ['tctctgCAAAgcagtg', 0],
            'NPM1_Mut_Ivey-4': ['tctctgCTCGgcagtg', 0],
            'NPM1_Mut_Ivey-5': ['tctctgCCGGgcagtg', 0],
            'NPM1_Mut_Ivey-6': ['tctctgTTCGgcagtg', 0],
            'NPM1_Mut_DD-2': ['tctctgCTGGgcagtg', 0],
            'NPM1_Mut_DD-3': ['tctctgCAGAgcagtg', 0],
            'NPM1_Mut_DD-4': ['tctctgTGTGgcagtg', 0],
            'NPM1_Mut_DD-5': ['tctctgTCAGgcagtg', 0],
            'NPM1_Mut_DD-7': ['tctctgTAAGgcagtg', 0],
            'NPM1_Mut_COSMIC-5': ['tctctgGCCAgcagtg', 0],
            'NPM1_Mut_COMSIC-9': ['tctctgCAAGgcagtg', 0],
            'NPM1_Mut_Ivey-7': ['tctctgCCGTTcagtg', 0],
            'NPM1_Mut_RB-9': ['tctctgTAGCgcagtg', 0],
            'NPM1_Mut_RB-10': ['tctctgCCACgcagtg', 0],
            'NPM1_Mut_RB-16': ['tctctgTCATgcagtg', 0],
            'NPM1_Mut_RB-17': ['tctctgCTTGgcagtg', 0],
            'NPM1_Mut_RB-24': ['tctctgTACGgcagtg', 0],
            'NPM1_Mut_RB-26': ['tctctgCGGAgcagtg', 0],
            'NPM1_Mut_RB-20': ['tctctgCGCCgcagtg', 0],
            'NPM1_Mut_COSMIC-6': ['aagatcGCTGtctggc', 0],
            'NPM1_Mut_Ivey-10': ['gatctcACAAtggcag', 0],
            'NPM1_Mut_RB-7': ['atctctCCCGggcagt', 0],
            'NPM1_Mut_RB-19': ['agatctATGCgcagtg', 0],
            # Start Grupp 2
            'NPM1_Mut_DD-9': ['tggcagAGGAtggagg', 1],
            'NPM1_Mut_DD-10': ['tggcagAGAAtggagg', 1],
            'NPM1_Mut_DD-11': ['tggcagAGACtggagg', 1],
            'NPM1_Mut_DD-12': ['tggcagCGCTtggagg', 1],
            'NPM1_Mut_Ivey-12': ['tggcagCGGAtggagg', 1],
            'NPM1_Mut_COSMIC-10': ['tggcagCGGCtggagg', 1],
            'NPM1_Mut_RB-28': ['tggcagCGTTCggagg', 1],
            'NPM1_Mut_RB-15': ['tggcagTCCAtggagg', 1],
            'NPM1_Mut_ZD': ['TGGCAGAGGCTGGAGG', 1],
            # Start Grupp 3
            'NPM1_Mut_S': ['CTGGCAGTGTTTTTCTCGAGGAAGT', 2],
            'NPM1_Mut_T': ['CTGGCAGTGCATGGCTCGAGGAAGT', 2],
            'NPM1_Mut_RB-1': ['ctggcagtCTCTTGCCCaagtctct', 2],
            'NPM1_Mut_RB-2': ['ctggcagtCCCTGGAGAaagtctct', 2],
            'NPM1_Mut_RB-3': ['ctggcagtCCCTCGCCCaagtctct', 2],
            'NPM1_Mut_RB-4': ['ctggcagtGCTTCGCCaagtctctt', 2],
            'NPM1_Mut_RB-5': ['ctggcagtGTTTTTCAAaagtctct', 2],
            'NPM1_Mut_RB-6': ['ctggcagtCTCTTTCTAaagtctct', 2],
            'NPM1_Mut_RB-8': ['ctggcagtCCCTTTCCAaagtctct', 2],
            'NPM1_Mut_RB-11': ['ctctggcagCGTTTCCaggaagtct', 2],
            'NPM1_Mut_RB-21': ['tggcagtgCTGCTCCCaagtctctt', 2],
            'NPM1_Mut_RB-22': ['ctggcagtTATTTTCCCaagtctct', 2],
            'NPM1_Mut_RB-23': ['ctggcagtCTTTCTCCCaagtctct', 2],
            'NPM1_Mut_Ivey-13': ['tggcagtCTTTCGCTCACgtctctt', 2],
            'NPM1_Mut_Ivey-14': ['tggcagtgTTTTGCTCaagtctctt', 2],
            'NPM1_Mut_Ivey-15': ['tggcagtgTTTTTCCCaagtctctt', 2],
            'NPM1_Mut_RB-25': ['ctggcagCggaTGGCCgaagtctct', 2],
            'NPM1_Mut_RB-27': ['ctggcagCggaTTCCggaagtctct', 2],
            'NPM1_Mut_RB-29': ['ctggcagtggaTGGAggaagtctct', 2],
            'NPM1_Mut_RB-30': ['ctctggcTCCGATTTGCggaagtct', 2],
            'NPM1_Mut_Ivey-8': ['ctctgTCAAGACTTTCTTAaagtct', 2],
            'NPM1_Mut_Ivey-9': ['tctgTCGGAGTCTCGGCGGACtctc', 2],
            'NPM1_Mut_DD-13': ['tggcagGGGGTGGGGAATCtctctt', 2],
            'NPM1_Mut_RB-31': ['ctggcagtATCTGGGGGCCCtctct', 2],
            'NPM1_Mut_RB-18': ['ctggcaAGATTTCTTAATTCgtctc', 2],
            'NPM1_Mut_XI': ['CTGGCAGGGGTTGGCCCGGGTCTCT', 2], # added 190527
            'NPM1_Mut_YU': ['CTGGCAGTGGTTGGCGGAAGTCTCT', 2], # added 190527
            'NPM1_Mut_XC': ['TGGCAGCGTTTCGGGGACATCTCTT', 2], # added 190527
            'NPM1_Mut_XK': ['CTGGCAGTCGGTTTCTTTGCTCTCTTT', 2], # added 190527
            'NPM1_Mut_KI-1': ['CTGGCAGCGGTTCGGGGCAGTCTCT', 2], # added 191106
            # Start Grupp 4
            'NPM1_Mut_ZF': ['ACTCTGGCAGCTTCTCCATGGAGGA', 3],
            'NPM1_Mut_ZG': ['CTCTGGCAGCGGATGGCTGGAGGAA', 3],
            'NPM1_Mut_Ivey-11': ['agatctcTCCATGCTCCtggaggaa', 3],
            'NPM1_Mut_RB-12': ['agatctctgTACCTTCCtggaggaa', 3],
            'NPM1_Mut_RB-13': ['aagatctctgCCGCGGagtggagga', 3],
            'NPM1_Mut_2UM': ['AGATCTCTGTCACCTAGTGGAGGAA', 3], # added 190527
            'NPM1_Mut_2YQ': ['AGATCTCTGCAGAAAAGTGGAGGAA', 3], # added 190527
            'NPM1_Mut_KI-2': ['ATCTCTGGCAAAAAATGGAGGAAGT', 3], # added 200714
            'NPM1_Mut_KGG-1': ['AGATCTCTGCACAGTTATGGAGGAA', 3]} # added 200714


# Wildtypes: Grupp 1, Grupp 2, Grupp 3, Grupp 4 
wildtypes = ["AAGATCTCTGGCAGTG", "tctggcagtggaggaa", "TCTCTGGCAGTGGAGGAAGTCTCTT", "AAGATCTCTGGCAGTGGAGGAAGTC"]

# List of the mutation names that will be looped through
mut_list = ['NPM1_Mut_A', 'NPM1_Mut_B', 'NPM1_Mut_D', 'NPM1_Mut_H', 'NPM1_Mut_I', 'NPM1_Mut_L', 'NPM1_Mut_K', 'NPM1_Mut_N', 'NPM1_Mut_R', 'NPM1_Mut_X', 'NPM1_Mut_Y', 'NPM1_Mut_Z', 'NPM1_Mut_COSMIC-6', 'NPM1_Mut_Ivey-10', 'NPM1_Mut_Ivey-1', 'NPM1_Mut_Ivey-2', 'NPM1_Mut_Ivey-3', 'NPM1_Mut_Ivey-4', 'NPM1_Mut_Ivey-5', 'NPM1_Mut_Ivey-6', 'NPM1_Mut_DD-2', 'NPM1_Mut_DD-3', 'NPM1_Mut_DD-4', 'NPM1_Mut_DD-5', 'NPM1_Mut_DD-7', 'NPM1_Mut_COSMIC-5', 'NPM1_Mut_COMSIC-9', 'NPM1_Mut_Ivey-7', 'NPM1_Mut_RB-9', 'NPM1_Mut_RB-10', 'NPM1_Mut_RB-16', 'NPM1_Mut_RB-17', 'NPM1_Mut_RB-24', 'NPM1_Mut_RB-26', 'NPM1_Mut_RB-20', 'NPM1_Mut_RB-7', 'NPM1_Mut_RB-19', 'NPM1_Mut_DD-9', 'NPM1_Mut_DD-10', 'NPM1_Mut_DD-11', 'NPM1_Mut_DD-12', 'NPM1_Mut_Ivey-12', 'NPM1_Mut_COSMIC-10', 'NPM1_Mut_RB-28', 'NPM1_Mut_RB-15', 'NPM1_Mut_ZD', 'NPM1_Mut_RB-11', 'NPM1_Mut_DD-13', 'NPM1_Mut_S', 'NPM1_Mut_T', 'NPM1_Mut_RB-1', 'NPM1_Mut_RB-2', 'NPM1_Mut_RB-3', 'NPM1_Mut_RB-4', 'NPM1_Mut_RB-5', 'NPM1_Mut_RB-6', 'NPM1_Mut_RB-8', 'NPM1_Mut_RB-22', 'NPM1_Mut_RB-23', 'NPM1_Mut_Ivey-14', 'NPM1_Mut_Ivey-15', 'NPM1_Mut_RB-21', 'NPM1_Mut_Ivey-13', 'NPM1_Mut_RB-31', 'NPM1_Mut_RB-29', 'NPM1_Mut_RB-25', 'NPM1_Mut_RB-27', 'NPM1_Mut_RB-18', 'NPM1_Mut_XI', 'NPM1_Mut_YU', 'NPM1_Mut_XC', 'NPM1_Mut_XK', 'NPM1_Mut_RB-30', 'NPM1_Mut_Ivey-8', 'NPM1_Mut_Ivey-9', 'NPM1_Mut_RB-12', 'NPM1_Mut_RB-13', 'NPM1_Mut_Ivey-11', 'NPM1_Mut_ZG', 'NPM1_Mut_ZF', 'NPM1_Mut_2UM', 'NPM1_Mut_2YQ', 'NPM1_Mut_KI-1', 'NPM1_Mut_KI-2', 'NPM1_Mut_KGG-1']
