def line_count(fileName):
  """ Counts the number of lines in the file 'fileName' """
  count = 0
  theFile = open(fileName)
  theLines = theFile.readlines()
  for aLine in theLines:
    count=count+1
  theFile.close()
  return count

print line_count("ASH.txt")

def word_count(fileName):
  """ Counts the number of words in the file 'fileName' """
  count = 0
  theFile = open(fileName)
  theLines = theFile.readlines()
  for aLine in theLines:
    words = aLine.split()
    count=count+len(words)
  theFile.close()
  return count

print word_count("ASH.txt")

def count_thes(fileName):
  """ 'Slowly' count the number of 'the's appearing in the file 'fileName' """
  count = 0
  theFile = open(fileName)
  theLines = theFile.readlines()
  for aLine in theLines:
    words = aLine.split()
    for aWord in words:
      if (aWord == "the"):
        count=count+1
  theFile.close()
  return count

print count_thes("ASH.txt")

def word_histogram(fileName):
  """ Build a histogram (frequency) of the words in the file 'fileName' """
  hist = {}
  theFile = open(fileName)
  theLines = theFile.readlines()
  for aLine in theLines:
    words = aLine.split()
    for aWord in words:
      if aWord in hist:
        hist[aWord]+=1
      else:
        hist[aWord]=1
  theFile.close()
  return hist

dict = word_histogram("ASH.txt")

def quickly_count_thes(fileName):
  """ Quickly count the number of 'the's appearing in the file 'fileName' """
  dict = word_histogram(fileName)
  return dict['the']

print quickly_count_thes("ASH.txt")

def quickly_count_a_word(fileName,theWord):
  """ Quickly count a number of times 'theWord' appears in the file 'fileName' """
  dict = word_histogram(fileName)
  if ( theWord in dict ):
    return dict[theWord]
  else:
    return 0

print quickly_count_a_word("ASH.txt","there")

def print_words_that_occur_more_than_N_times(fileName,n):
  """ Quickly count the number of 'the's appearing in the file 'fileName' """
  dict = word_histogram(fileName)
  for theWord in dict:
    if (dict[theWord] > n):
      print theWord + ": " + str(dict[theWord])

print_words_that_occur_more_than_N_times("ASH.txt",1000)

def most_used(hist):
  max = 0
  word = ""
  for key in hist:
    if (hist[key]>max):
      word = key
      max = hist[key]
  return word, max

dict = word_histogram("ASH.txt")
print most_used(dict)
