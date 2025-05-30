"""
Author : Omer Khan
Student number: 753619
Course code: ICS3U
Revision date : May 17, 2025
Program : Wordle Database Search
Description : A program the searches for words and date entered by the users in the Wordle Database File 
    

VARIABLE DICTIONARY :
  arr (list) =  stores each line of the file as an array list
  arr_date (list) = stores every line of the dates in the file as an array list
  arr_word (list) = stores all the words from the file 
  arr_months (list) = this array contains all the months of the year
  fh (file object) = File handle used to open/read the "wordle (1).dat" file
  line (str) = Stores one line of text read from the file, stripped of whitespace
  month (str) = stores the three letter abbreviation of the month
  day (str) = stores the day portion of a date
  year (str) = stores the year portion of a date
  date (int) = temporary variable wehn looping through arr_date
  i (int) = Loop index variable for going through the arr list
  user_input_word (str) = the user input string for searching a word in the file 
  word (str) = temporary varaible used when looping through the arr_word list
  user_input_date (int) = 	the user input integer date in YYYYMMDD format, used to find the corresponding word on that date
  user_choice (str) = User input to choose search mode: "w" for word search, "d" for date search
  w (str) = user input word for search 
  user_year (int) = User input year for date search
  user_month (str) = stores the month input by the user when searching by date
  user_day (str) = stores the day input by the user when searching by date 
"""

#Creating an empty array to store each line of the file as values
arr = []
#Creating an array that holds date in number format from the file
arr_date = [] 
#creates an array with all the words from the "wordle.date" file
arr_word= []
#Creates an array for all the months abbreviation
arr_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

try:
    #Opens the file to read
    fh = open("wordle (1).dat", "r")
    #goes through each line of the file
    line = fh.readline().strip() 
    #Continues to read uptil an empty line is reached (EOF)
    while line != "": #When an empty line is reached
        #This splits the line and gets rid of the white spaces and appends to arr
        arr.append(line.split(" "))
        # Reads the next line
        line = fh.readline().strip()      
    # Closes the file once its done reading it
    fh.close()

except OSError as err:
  # Handles file not found error and prints this message for error
  print("OSError: ", err)  

#This defines the function which converts the dates to integer
def merge_date(month,day,year):
  # Turns year into YYYY0000
  year = int(year) * 10000
  # Turns month name to MM00
  month = (arr_months.index(month)+1) * 100  
  day = int(day)
  # Now combines the year, month, and the day 
  return year + month + day  

i = 0
# Loops through each row in arr to fill arr_date and arr_word
while i < len(arr): # This goes through as long as i is less than length of the array
  # Converts the date to int and appends to arr_date
  arr_date.append(merge_date(arr[i][0], arr[i][1], arr[i][2]))
  # Appends the word (third item in the row)
  arr_word.append(arr[i][3])
  i += 1 #adds one to the value of i

#Creates a function that searches for a word. If the word is found in the file, then the date on which it occured is returned
def word_match(user_input_word):
  # cycles through every word in arr_word
  for word in arr_word: 
     # Checks if equal to uppercase version of the input 
    if word == user_input_word.upper():
      #Returns the date on the same index on which the user_input_word in the arr_word occured 
      return arr_date[arr_word.index(user_input_word.upper())]
  return 0 # If the word is not found i the arr_word, return 0

def date_match(user_input_date):
    for date in arr_date: #cycles through every date in arr_date
        if date == user_input_date:
            return arr_word[arr_date.index(user_input_date)]

print("Welcome to the Wordle game!")
user_choice = input("Enter w to find a word or enter d to find a word on a certain date: ")    

# If the user wants to find a word
if user_choice == "w":  
   #Gets the word input from the user
   w = input("Enter the word you are looking for: ") 
   #Checks if the word is a matching date
   if word_match(w) > 0:
      #displays the date on which the word was on
      print("The word", w.upper(), "is the correct answer to the puzzle on", word_match(w) )
   else: 
      #If the word is not found in the database
      print(w.upper()," was not found Wordle File")

#In the case of user wanting to enter a date
elif user_choice == "d":
   #The user enters the year of the date 
   user_year = int(input("Enter the year: "))
   #The user enters the month of the date
   user_month =input("Enter the month (Month name abbriviation): ").capitalize()
   #The user enters the day of the date
   user_day = int(input("Enter the day: "))
   if 20210619 <= merge_date(user_month, user_day, user_year) <= 20240421:
      print("The word you entered on", merge_date(user_month, user_day, user_year), "was", date_match(merge_date(user_month, user_day, user_year)))
      # If date too early
   elif 20210619 > merge_date(user_month, user_day, user_year): 
    # Prints given date is too early
    print(merge_date(user_month, user_day, user_year), "is too early. No wordles occurred before 20210619. Enter a later date.")
   # If date too late
   else:
    # Prints given date is too recent
    print(merge_date(user_month, user_day, user_year), "is too recent. Our records only go as late as 20240421. Please enter an earlier date.")


    
  

   
   
   
