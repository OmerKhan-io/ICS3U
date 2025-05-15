date = 0
def merge_date(mo,day,year):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    mo = int(mo)  
    date = year*10000 + mo*100 + day
    return date
    

sarr = []
dateL = ""

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

print(dateL, date)
print("Welcome to the Wordle Database!")
user = input("Enter w if you are looking for a word, or d for a word on a certain date: ")

if user == "w":
    uword = input("Enter a word: ")
elif user == "d"
    uyear = input("Enter a date")
    umonth = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
    udate = input("Enter the day: ")
    print("The word entered on ")


    






