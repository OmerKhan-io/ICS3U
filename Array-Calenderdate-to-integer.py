months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Nov", "Dec"]
s = "Apr 29 2025"
Sarr = s.split()
mo = months.index(Sarr[0]) + 1
day = int(Sarr[1])
year = int(Sarr[2]) 

date = year*10000 + mo*100 + day
# multiply year by ten thousand to get 4 place values after it for the month and date
# multiply month by 100 to get 2 place values for the date 
print(date)

