#Convert the time entered in hh,min and sec into seconds.
print("Enter time in hh mm ss")
hh = int(input("Enter number of hours as hh:"))
mm = int(input("Enter number of minutes as mm:"))
ss = int(input("Enter number of seconds as ss:"))
time = hh*3600 + mm*60 +ss
print("Time in seconds is:", time ,"seconds")