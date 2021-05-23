from datetime import datetime 

--- To find the execution time 

now=datetime.today()   - adatetime object

later=datetime.today()

diff=later-now

--- only date 

from datetime import date

system_date = date.today()

custom_date = date(2019, 4, 13)
print(custom_date)

date_diff = system_date - custom_date

print(date_diff)   --0:00:12.412493

---- To covert string to date 

date_passed = '2018-11-23'
date_new = datetime.strptime(date_passed, '%Y-%m-%d')




--- To print only date part

now=datetime.today()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
today_dat= now.strftime("%Y-%m-%d")
print("date and time:",date_time)


--- To find datediff

from datetime import datetime, timedelta
    
d = datetime.today() - timedelta(days=days_to_subtract)   // to add or subtract days

date_passed = '2018-11-23'
date_new = datetime.strptime(date_passed, '%Y-%m-%d')

print((d - date_new).days)                               // difference between two dates    


past_date_before_2hours = ini_time_for_now - timedelta(hours = 2)



--- Sleep

import time

time.sleep(n)