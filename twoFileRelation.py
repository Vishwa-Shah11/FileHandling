def relation(file1, file2):
    """
    Determine the relationship between two files

    Arguments:
        file1, file2: strings, paths to two files
    Return:
        string: 'Equal', 'Subset' or 'No Relation'
    """
    f1 = open(file1,'r')
    f2 = open(file2, 'r')
    result = 'No Relation'
    if f1 in f2:
        result = 'Subset'
    if f1 == f2:
        result = 'Equal'
      
    return result
    f1.close()
    f2.close()

print(relation('file1.txt','file2.txt'))