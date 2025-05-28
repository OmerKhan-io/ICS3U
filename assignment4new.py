#Creating an array to store each line of the file as values
arr = []
#Creating array that holds date in number format from the file
arr_date = []
arr_word= []
arr_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

try:
    fh = open("wordle (1).dat", "r")
    line = fh.readline().strip() #goes through each line of the file
    while line != "":
    #When an empty line is reached
        #This splits the line and gets rid of the white spaces
        arr.append(line.split(" "))
        # Reads the next line
        line = fh.readline().strip()      
#Closes the file once its done reading it
    fh.close()

except OSError as err:
  # Handles file not found error and prints this message for error
  print("OSError: ", err)  

#This defines the function which converts the dates to integer
def merge_date(month,day,year):
  # Turns year into YYYY0000
  year = int(year) * 10000
  # Turns month name to MM00
  month = (arr_months.index(month) + 1) * 100  
  day = int(day)
  # Now combines the year, month, and the day 
  return year + month + day  

i = 0
# Loops through each row in arr to fill arr_date and arr_word
while i < len(arr): # This goes through as long as i is less than length of the array
  # Converts the date to int and appends to arr_date
  arr_date.append(merge_date(arr[i][0], arr[i][1], arr[i][2]))
  # Appends the word (third item in the row)b
  arr_word.append(arr[i][3])
  i += 1 #adds one to the value of i

#Creates a function that searches for a word. If the word is found in the file that date is returned
def word_match(user_input_word):
  for word in arr_word: #cycles through every word in arr_word
     # Checks if equal to uppercase version of the input 
    if word == user_input_word.upper():
      return arr_date[arr_word.index(user_input_word.upper())]
  return 0 # If the word is not found, return 0

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
   user_month =int(input("Enter the month: ")) 
   #The user enters the day of the date
   user_day = int(input("Enter the day: "))
   if 20210619 <= merge_date(user_month, user_day, user_year) <= 20240421:
      print("The word you entered on", merge_date(user_month, user_day, user_year), "was", merge_date(user_month, user_day, user_year))
      # If date too early
   elif 20210619 > merge_date(user_month, user_day, user_year): 
    # Prints given date is too early
    print(merge_date(user_month, user_day, user_year), "is too early. No wordles occurred before 20210619. Enter a later date.")
   # If date too late
   else:
    # Prints given date is too recent
    print(merge_date(user_month, user_day, user_year), "is too recent. Our records only go as late as 20240421. Please enter an earlier date.")


    
  

   
   
   
