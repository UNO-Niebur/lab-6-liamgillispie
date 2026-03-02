#WordIndex.py
#Name:Liam Gillispie
#Date:3/1/2026
#Assignment:Lab 6
#Purpose: Build an index mapping each word to a list of line numbers where it appears

def main():
  textFile = open("fish.txt", 'r')
  
  words = {} #create an empty dictionary
  lineNum=0
  for line in textFile:
    lineNum=lineNum+1
    wordList=line.split()
    for w in wordList:
      w=w.lower()
      w=w.replace(",", "")
      w=w.replace(".", "")
      if w in words:
        if lineNum not in words[w]:
          words[w].append(lineNum)
      else:
        words[w]=[lineNum]

  for word in words:
    print(words, words[word])

if __name__ == '__main__':
  main()
