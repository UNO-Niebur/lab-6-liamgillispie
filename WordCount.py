#WordCount.py
#Name:Liam Gillispie
#Date:3/1/2026
#Assignment:Lab 6
#Purpose: Implement a simplified word count program
import glob

def main():
  textFile = glob.glob("gettysberg.txt","fish.txt")
  valid_files=["fish.txt","gettysberg.txt"]
  fileName=input(f"Enter your chosen file here({', '.join(valid_files)}): (either 'gettysberg.txt' or 'fish.txt')")
  
  if fileName in valid_files:
    try:
      with open(fileName, 'r') as file:
        print(f"Successfully opened {fileName}!")
        lineCount=0
        wordCount=0
        letterCount=0
        for line in textFile:
          lineCount=lineCount+1
          words=line.split()
          for w in words:
            wordCount=wordCount+1
            for char in w:
              if char.isalpha():
                letterCount=letterCount+1
        print("Lines:",lineCount)
        print("Words:",wordCount)
        print("Letters:",letterCount)
    except FileNotFoundError:
      print(f"Error: The file'{fileName}' was found in the list but not in the system.")
  else:
    print(f"Error:'{fileName}' is not a valid option.")
if __name__ == '__main__':
  main()
