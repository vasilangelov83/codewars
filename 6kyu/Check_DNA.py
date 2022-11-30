def check_DNA(seq1, seq2):
    shroter = seq1
    longer = seq2
    if len(seq1) > len(seq2):
        shroter = seq2
        longer = seq1
    ref_dict = {"A": "T", "C": "G","G": "C","T":"A"}

    if ''.join([ref_dict[x] for x in reversed(shroter)]) in longer:

        return True
    else: return False
check_DNA('GCGCTGCTAGCTGATCGA','ACGTACGATCGATCAGCTAGCAGCGCTAC')
