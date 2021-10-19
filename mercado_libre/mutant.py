import re


def is_mutant(dna):
    
    length = len(dna[0])
    string = ' '.join(dna)
    diag_steps = re.escape(str(length+1))
    vert_steps = re.escape(str(length))
    diag_inv_steps = re.escape(str(length-1))

    matches = 0
    
    horizontal_pattern = r'([ACTG])(.{0}\1){3}'
    diag_pattern = r'([ACTG])(.{' + diag_steps + r'}\1){3}'
    vert_pattern = r'([ACTG])(.{' + vert_steps  + r'}\1){3}'
    diag_inv_pattern = r'([ACTG])(.{' + diag_inv_steps + r'}\1){3}'
    
    
    list_of_regex = [horizontal_pattern, diag_pattern, vert_pattern, diag_inv_pattern]

    for pattern in list_of_regex:
        regex = re.findall(pattern, string)
        if regex:
            matches += len(regex)
    
    if matches > 1:
        return 'is mutant'
    
    elif matches < 2:
        return 'is not mutant'

