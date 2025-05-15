sarr = []

try:
    fh = open("wordle.dat")
    eof = False
    while not eof:
        sarr.append(fh.readline())
        last= len(sarr ) - 1
        eof = (sarr[last] == "")
    fh.close()
except OSError as err:
    print("OSError: File not found ", err)
except EOFError as err2:
    print("EOFError: ", err2)
    fh.close()
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#s = "Apr 29 2025"
for i in sarr:
    dateL = s.split()
    mo = months.index(dateL[0]) + 1
    day = int(dateL[1])
    year = int(dateL[2]) 

    date = year*10000 + mo*100 + day

print(dateL, date)

if user == "w":
    word = input("Enter a word: ")
    for i in sarr:
        if word in i:
            print(i)
elif user == "d":
    date = input("Enter a date in the format mm/dd/yyyy: ")
    for i in sarr:
        if date in i:
            print(i)
print(dateL, date)
print("Welcome to the Wordle Database!")
user = input("Enter w if you are looking for a word, or d for a word on a certain date: ")

if user == "w":
    uword = input("Enter a word: ")
elif user == "d"
    uyear = input("Enter a date")
    umonth = input("Enter the month ( (3-letter abbreviation, as in 'Jan' for 'January'): ") ")
    udate = input("Enter the day: ")a
    print("The word entered on ")
