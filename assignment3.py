"""
  Author : Omer Khan
  Student Number : 753619
  Revison date : 25 April 2025
  Program : Palindrome Checker
  Description : A program that determines whether the words in the given list is a palindrome or not
VARIABLE DICTIONARY
  ar(list) = a list of words that will be checked to see if they are palindromes
  word(str) = The current word being check in teh for loop
  letter_match(int) = Counts how many letters (from start and end) are matching
  letter_positon(int) = the index used to move from the beginning of the word to its centre
  midway(int) = the halfway point of the word. The point to stop checking for letters in a word
"""
print("Welcome to the Palindrome Program")
ar = ["noon", "racecar", "civic", "madam", "desk", "kayak", "soccer", "level", "school", "radar"]

#Create loops that goes through each word
for word in ar:
  letter_match = 0
  letter_position =  0
  midway = len(word) // 2
  
  # This loop keeps running as long as we're before the halfway point
  while letter_position < midway: 
    if word[letter_position] == word[len(word) - 1 - letter_position]:
      #Checks if letters match
      #Checks if the letter from the beginning matching the letter from the end of the word
      letter_match +=1 
      #if letter matches; then increase the count to next set of letters
    letter_position += 1 
      #Move to the next letter position
  
  #After checking all letters upto the midway point
  #Checks to see If all mirrored letters matched up to midway, it's a palindrome
  if letter_match == midway:
   
    print(word, "is a palindrome")
  else:
    print(word, "is NOT a palindrome")
print("Goodbye")
    
  
  

