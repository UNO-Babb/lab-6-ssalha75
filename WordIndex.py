#WordIndex.py
#Name: Sara Salha
#Date: 2/26/25
#Assignment: WordIndex.py

def main():
  textFile = open("gettysberg.txt", 'r')

  wordList = {} #create an empty dictionary
  lineNum = 0
  for line in textFile:
    lineNum += 1
    words = line.split()
    for word in words:
      #process word to make uniform
      word = word.lower()
      word = word.replace("," , "")
      word = word.replace("." , "")
      word = word.replace("\n" , "")
      word = word.replace("!" , "")

      if word in wordList:
        wordList[word].append(lineNum) #add to existing entry
      else:
        wordList[word] = [lineNum]     #add word to list
  #print results
  for word in wordList:
    print(word, wordList[word])
 
if __name__ == '__main__':
  main()
