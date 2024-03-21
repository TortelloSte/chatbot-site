from pytz import timezone, utc
from datetime import datetime, timedelta


def SetCustomTimeInLogger(*args):
    utc_dt = utc.localize(datetime.utcnow())
    my_tz = timezone("Europe/Rome")
    converted = utc_dt.astimezone(my_tz)
    return converted.timetuple()