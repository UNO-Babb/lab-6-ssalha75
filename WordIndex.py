#WordIndex.py
#Name: Sara Salha
#Date: 2/26/25
#Assignment: WordIndex.py

def main():
  textFile = open("fish.txt", 'r')
  
  words = {} #create an empty dictionary
  
  
  print ("fish" in words) #is a word already in the dictionary?
  words["fish"] = [2]     #add a list to the dictionary
  print ("fish" in words) #is the word there now?
  words["fish"].append(5) #add to an existing list
  print(words)


if __name__ == '__main__':
  main()
