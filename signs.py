x = 1
while x==1:
 m = (input("enter your month "))
 month = m.lower()
 
 date =int(input("enter your date"))

 if month == "january" and date<19 and date<=19  or month == "december" and date>=22 and date>31:
     print("capricorn")

 elif month =="january"and date<=20  and date<=31 or month == "february" and date>= 22 and date<=18:
     print("aquarius")

 elif month=="february"and date>=19 and date<=29  or month == "march"  and   date<=1  and date<20:
     print("pisces")

 elif month =="march" and date>=21  and date<=31  or month == "april"  and  date<=1  and date<=19:
     print("aries")

 elif month =="april" and date>=20  and date<=30  or month == "may"    and    date>=1  and date<=20:
     print("taurus")

 elif month =="may"   and date>=21  and date<= 31 or month == "june"   and   date>=1  and date<=20:
     print("gemini")

 elif month =="june" and date>=21   and date<=30   or month =="july"    and   date>= 1 and date<=22:
     print("cancer")

 elif month=="july" and date>=23   and date<= 31 or month == "august"  and    date>=1 and date<=22:
     print("leo")

 elif month =="august"and date>=23 and date<=31  or month =="september" and   date>=1  and date<=22:
            print("virgo")

 elif month=="september" and date>=23 and date <=30 or month=="october"  and   date>= 1 and date<=22:
     print("libra")

 elif month == "october" and date>=23 and date<=31 or  month =="november" and date >=1  and date<=21:
            print("scorpio")

 elif month == "november"  and date>=22 and date<=30 or month== "december" and  date >= 1  and date<=21:
            print("sagittarius")
 else:
    print("system print")

 x = int(input("press 1 for continue and 0 for exit"))
 if x ==0:
  break