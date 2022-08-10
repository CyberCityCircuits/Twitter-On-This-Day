#Twitter - On This Day Script

import webbrowser
from datetime import datetime as dt

print ('Twitter - On This Day')
print ('Cyber City Circuits - @MakeAugusta')

#Search Example: 'https://twitter.com/search?q=(from%3AMakeAugusta)%20until%3A2018-03-08%20since%3A2018-01-08&src=typed_query&f=top'

year = dt.now().year
month = dt.now().month
day = dt.now().day

#Put in the year that you joined Twitter
oldest_year = 2018

#Put Your Name Below
username = 'MakeAugusta'

def open_twitter(search_year, search_month, search_day):
    start_date = str(search_year) + '-' + str(search_month).zfill(2) + '-' + str(int(search_day)-1).zfill(2)
    end_date = str(search_year) + '-' + str(search_month).zfill(2) + '-' + str(int(search_day)+1).zfill(2)
    search_string = 'https://twitter.com/search?q=(from%3A' + username + ')%20until%3A'+ end_date +'%20since%3A' + start_date + '&src=typed_query&f=top'
    webbrowser.open_new(search_string)

years = range(oldest_year, year)
for n in years:
    open_twitter(str(n), month, day)
