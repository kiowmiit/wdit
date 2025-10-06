from datetime import datetime
from datetime import UTC
import calendar

current_datetime = datetime.now()
current_datetime_utc = datetime.now(UTC)

print(current_datetime)
print(current_datetime_utc)

past_datetime = datetime(year=2001, month=9, day=11, hour=12, minute=20)
print(past_datetime)

time_difference = current_datetime - past_datetime
print(time_difference)

print(calendar.month_name[current_datetime.month])