from __future__ import print_function
import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    print("id\tchr\tpos\tref\talt\tfreq")
    for line in f:
        minorallelecount = 0;
        refallelecount = 0;
        if line.startswith('#'):
            continue
        line = line.rstrip()
        fields = line.split("\t")
        genotypes =fields[9:len(fields)]
        chr = fields[0]
        pos = fields[1]
        id = fields[2]
        ref = fields[3]
        alt = fields[4]
        for sample in genotypes:
            genos = genotypes
            for geno in genos:
                if geno!="0":
                    minorallelecount+=1
                elif geno=="0":
                    refallelecount+=1
                else:
                    print('missing' + geno)
        freq = float(minorallelecount)/(float(refallelecount+minorallelecount)*2)
        print(id + '\t'+chr+'\t' +pos+'\t'+ref+'\t'+alt + '\t' + str(freq))
