AA_dict = {
'ALA': 'A', 'ARG': 'R',
'ASN': 'N', 'ASP': 'D',
'CYS': 'C', 'GLU': 'E',
'GLN': 'Q', 'GLY': 'G',
'HIE': 'H', 'HID': 'H',
'HIS': 'H', 'ILE': 'I',
'LEU': 'L', 'LYS': 'K',
'MET': 'M', 'PHE': 'F',
'PRO': 'P', 'SER': 'S',
'THR': 'T', 'TRP': 'W',
'TYR': 'Y', 'VAL': 'V',
'SEC': 'U', 'PYL': 'O',
'CYX': 'C',
}

def pdb2seq(file):
    assert file.lower().endswith('.pdb'), "Accepts PDB files only!"
    seq_number_prev = -2
    aa_sequence = ''
    code_insert_residue_prev = None
    aa_seq_list = []
    aa_num_list = []
    with open(file, 'r') as f:
        for line in f:
            # only accepts ATOM for amino acid PDB
            # HETATM is not contained in PDB
            if not line.startswith('ATOM'):
                continue
            residue = line[17:20]
            # Residue sequence number + Code for insertions of residues
            seq_number = int(line[22:26])
            code_insert_residue = line[26:27]
            if seq_number_prev == seq_number and \
                code_insert_residue_prev == code_insert_residue:
                continue
            else:
                # do not repeat '/' in sequence
                # if sequence number stops / breaks from a continous list
                if seq_number_prev + 1 < seq_number and seq_number_prev > 0 \
                    and aa_sequence[-1] != '/':
                    aa_sequence += '/'
                aa_sequence += AA_dict[residue]
                aa_seq_list.append(AA_dict[residue])
                # if code_insert_residue appears
                if code_insert_residue != " " \
                    and aa_sequence[-1] != '/':
                    aa_sequence += '/'
                
                seq_number_prev = seq_number
                code_insert_residue_prev = code_insert_residue
                aa_num_list.append(str(seq_number)+code_insert_residue.strip())
    return aa_sequence, aa_seq_list, aa_num_list
