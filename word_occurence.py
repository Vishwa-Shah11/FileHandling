def get_freq(filename):
    """
    Extract frequency information from the file

    Argument:
        filename: string, path to file
    Return:
        result: dictionary; keys are strings, values are integers
    """
    f = open(filename, 'r')
    d = {}
    for line in f:
      line = line.strip()
      words = line.split("\n")
      for word in words:
          if word in d:
              d[word] = d[word] + 1
          else:
              d[word] = 1
    return d

print(get_freq('word_occurence.txt'))