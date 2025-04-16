"""
  Author : Omer Khan
  Student Number : 753619
  Revison date : 15 April 2025
  Program : Even or Odd
  Description : A program that determines whether the word is a palindrome or not
VARIABLE DICTIONARY
  ar(list) = a list of words that will be checked to see if they are palindromes
  word(string) = The current word being check in teh for loop
  letter_match(int) = Counts how many letters (from start and end) are matching
  letter_positon(int) = the index used to move from the beginning of the word to its centre
  midway = the halfway point of the word. The point to stop checking for letters in a word
"""
print("Welcome to the Palindrome Program")
ar = ["noon", "racecar", "civic", "madam", "desk", "kayak", "soccer", "level", "school", "radar"]

#Create loops that c=goes through each word
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
  #Checks to see if all the compared letters matched, then the word is a palindrome
  if letter_match == midway:
   
    print(word, "is a palindrome")
  else:
    print(word, "is not a palindrome")
print("Goodbye")
    
  
  
  # 2

print("Welcome to the Palindrome Program")
ar = [ "noon", "racecar", "civic", "madam", "desk", "kayak", "soccer", "level", "school", "radar"]

#Create loops that c=goes through each word
for word in ar:
  max_index = len(word) // 2
  # This determines the halfway point of the word, as an integer
  for i in range(max_index): #loop goes from index 0 to max_inedex -1
  #i will be used to compare characters from the front and back of the word.
    while word
    if word[i] == word[len(word) - 1 - i]:
      print("It's a Palindrome")
    else: 
      print("Not a Palindrome")
  print( 
