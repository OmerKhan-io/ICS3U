#Creating an array to store each line of the file as values
arr_index = []
#Creating array that holds date in number format from the file
arr_date = []
arr_word= []
arr_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

try:
    fh = open("wordle.dat", "r")
    line = fh.readline().strip() #goes through each line of the file
    while != " ": #When an empty line is reached
    #This splits the line and gets rid of the white spaces
    arr.append(line.split(" "))
    


