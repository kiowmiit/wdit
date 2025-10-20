from datetime import datetime
from datetime import UTC
import calendar

current_datetime = datetime.now()
current_datetime_utc = datetime.now(UTC)

print(f"current_datetime: {current_datetime}")
print(f"current_datetime_utc: {current_datetime_utc}")

past_datetime = datetime(year=2001, month=9, day=11, hour=12, minute=20)
print(f"past_datetime: {past_datetime}")

# timedelta
time_delta = current_datetime - past_datetime
print(f"time_delta: {time_delta}")

print(f"Current month name: {calendar.month_name[current_datetime.month]}")