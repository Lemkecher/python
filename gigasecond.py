#calculate the gigasecond anniversary 

from datetime import timedelta
from datetime import datetime

def giga(birthday):
    birthday = datetime.strptime(birthday, "%Y/%m/%d %H:%M:%S")
    print ( birthday + timedelta ( seconds = 10e8))

giga( "1993/05/07 18:30:00" )
