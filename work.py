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
