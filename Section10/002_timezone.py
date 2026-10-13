from datetime import timezone,datetime,timedelta

x=datetime.now(timezone.utc)
y=datetime.now()
print(x.strftime('%Y - %m - %d - %H - %M --%S'))
print(datetime.strptime("2022-12-19","%Y-%m-%d"))