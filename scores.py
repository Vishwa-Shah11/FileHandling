def do_something(filename, sub):
    f = open(filename, 'r')
    # Ignore the header
    f.readline()	
    # we are now at the beginning of the second line of the file
    val, count = 0, 0
    
    for line in f:
        sno, name, gender, ct, python, pdsa = line.strip().split(',')
        sno, ct, python, pdsa = int(sno), int(ct), int(python), int(pdsa)
        if sub == 'CT':
            val = val + ct
        elif sub == 'Python':
            val = val + python
        elif sub == 'PDSA':
            val = val + pdsa
        count = count + 1
        
    f.close()
    return val / count

# Hint: int(1.5) is 1
print(int(do_something('scores.csv', 'Python')))

def get_scores(filename, index):
    f = open(filename, 'r')
    # Ignore the header
    f.readline()	
    # we are now at the beginning of the second line of the file
    
    scores = [ ]
    line = f.readline()
    while line != '':
        L = line.strip().split(',')
        scores.append(int(L[index]))
        line = f.readline()
    
    f.close()
    return scores

print(get_scores('scores.csv', 3))

def do_something(L):
    L.sort()
    mid = len(L) // 2
    if len(L) % 2 == 0:
        return (L[mid] + L[mid - 1]) // 2
    else:
        return L[mid]
    
print(do_something(get_scores('scores.csv', 4)))

def do_something(infile, gender, outfile):
    f = open(infile, 'r')
    g = open(outfile, 'w')
    header = f.readline()
    # we are now at the beginning of the second line of the file
    # 'good,M,great'.replace(',M,', ',')
    # returns 'good,great'
    header = header.replace(',Gender,', ',')
    g.write(header)
    
    for line in f.readlines():
        fields = line.strip().split(',')
        gender_in_file = fields[2]
        if gender_in_file == gender:
            out_line = line.replace(f',{gender},', ',')
            g.write(out_line)
    
    f.close()
    g.close()
    
do_something('scores.csv', 'F', 'out.csv')