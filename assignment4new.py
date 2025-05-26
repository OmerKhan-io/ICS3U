#Creating an array to store each line of the file as values
arr = []
#Creating array that holds date in number format from the file
arr_date = []
arr_word= []
arr_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

try:
    fh = open("wordle.dat", "r")
    line = fh.readline().strip() #goes through each line of the file
    while != " ": 
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
def merge_date(mo,day,year):
  # Turns year into YYYY0000
  year = int(year) * 10000
  # Turns month name to MM00
  month = (months.index(month) + 1) * 100  
  day = int(day)
  # Now combines the year, month, and the day 
  return year + month + day  

i = 0
# Loops through each row in arr to fill arr_date and arr_word
while i < len(arr): # This goes through as long as i is less than length of the array
  # Converts the date to int and appends to arr_date
  date_arr.append(merge(arr[x][0], arr[x][1], arr[x][2]))
  # Appends the word (third item in the row)b
  word_arr.append(arr[x][3])
  i += 1 #adds one to the value of i

#Creates a function that searches for a word. If the word is found in the file that date is returned
def word_match(user_input_word):
    for word in arr_word: #cycles through every word in arr_word
       
       if word = user_input_word.upper():
            return arr_date[word_arr.index(user_word.upper())]
       return 0 # If the word is not found, return 0

def date_match(user_input_date):
    for date in arr_date: #cycles through every date in arr_date
        if date == user_input_date:
            return arr_word[arr_date.index(user_input_date)]

print("Welcome to the Wordle game!")
print("Enter w to find a word or enter d to find a word on a certain date.")    

# If the user wants to find a word
if choice == "w":  
   w - input("Enter a word") 
   
   
   
