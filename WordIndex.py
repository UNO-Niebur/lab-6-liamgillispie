#WordIndex.py
#Name:Liam Gillispie
#Date:3/1/2026
#Assignment:Lab 6
#Purpose: Build an index mapping each word to a list of line numbers where it appears

def main():
  valid_files=["fish.txt","gettysberg.txt"]
  fileName=input(f"Enter your chosen file here({', '.join(valid_files)}): (either 'gettysberg.txt' or 'fish.txt')")
  
  if fileName in valid_files:
    try:
      with open(fileName, 'r') as file:
        print(f"Successfully opened {fileName}!")
        words = {} #create an empty dictionary
        lineNum=0
        for line in file:
          lineNum+=1
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
          print(f"Word:{word}, Line numbers:{words[word]}")
    except FileNotFoundError:
      print(f"Error: The file'{fileName}' was found in the list but not in the system.")
  else:
    print(f"Error:'{fileName}' is not a valid option.")
if __name__ == '__main__':
  main()
