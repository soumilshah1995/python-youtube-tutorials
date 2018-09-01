"""

Assingment number 1

I have started walking to home at 7:30 AM for the first mile at slow step (8 min:15 sec
per mile), then 3 miles at speed (7 min:12 sec per mile), what time do I get home for
breakfast? (format output in hh: min)

SOUMIL SHAH
Bachelor in Electronic Engineering
Master in Electrical Engineering
Master in Computer Engineering


"""

import datetime

walk = datetime.datetime(2018, 8, 1,7, 30, 00)

# 1 mile 8 MIN  15 SEC
walk_1 = walk + datetime.timedelta(0,minutes=8,seconds=15)

# 3 mile it takes 7 Min 12 sec per Mile
# 2 nd mile calculate
walk_2 = walk_1 + datetime.timedelta(0,minutes= 7, seconds= 12)

# walk 3 mile
walk_3 = walk_2 + datetime.timedelta(0, minutes=7, seconds=12)

# last Mile
walk_4 = walk_3 + datetime.timedelta(0, minutes=7, seconds=12)

print("You Will reach for BreakFast at {} ".format(walk_4))