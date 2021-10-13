
def is_mutant(dna):
    secuencias = 0
    matches = 0 
    COUNT = 3
    while matches < COUNT:
        for i in dna:
            for j in range(len(i)-1):
                if matches == 3:
                    secuencias += 1
                    matches = 0
                if i[j] == i[j+1]:
                    matches += 1
                elif matches < 3:
                    matches = 0
    
        for x in range(len(dna)-1):
            for y in range(len(dna[x])-1):
                
                if matches == 3:

                    secuencias += 1
                    print(dna[y][x])
                    matches = 0
                    
                if dna[y][x] == dna[y+1][x]:
                    
                    matches += 1
                elif matches < 3:
                    matches = 0
    
        if secuencias > 1:
            print(secuencias)
            return 'mutant'
                                

print(is_mutant(["ATGCGA","CAGTGC","TTATGT","AGAAGT","CCLLT","TCACTT"]))