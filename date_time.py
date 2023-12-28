from datetime import datetime, timedelta
import time


dt = datetime.now()
my_dt = datetime(2023, 11, 21) + timedelta(days=5)

duration = dt-my_dt
print(duration.days)
print(duration.seconds)

print(my_dt)
is_old = dt > my_dt
print(is_old)
timestamp = time.time()
print(datetime.fromtimestamp(timestamp))
print(dt.strftime("%Y/%m/%d"))
